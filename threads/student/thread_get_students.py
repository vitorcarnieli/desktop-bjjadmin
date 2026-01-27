from datetime import date

from PySide6.QtCore import QObject, Signal, QThread

from dtos.student_dto import StudentDto
from engine import Session
from models import Lesson
from repositories.lesson_repository import LessonRepository
from services.student_service import StudentService
from repositories.student_repository import StudentRepository



class ThreadGetStudentsSignals(QObject):
    signal_student_dtos = Signal(list)


class ThreadGetStudents(QThread):
    def __init__(self):
        super(ThreadGetStudents, self).__init__()
        self.lesson_repository = None
        self.signals = ThreadGetStudentsSignals()

        self.session = None
        self.student_repository: StudentRepository = None
        self.lessons = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)
        self.lesson_repository = LessonRepository(self.session)


        students = self.student_repository.get_all()
        student_dtos = [StudentService.get_dto(student) for student in students]

        self.lessons = self.lesson_repository.get_all()
        for dto in student_dtos:
            student = next((s for s in students if s.id == dto.id), None)
            if not student.is_inactive:
                latest_record = self._most_recent_payment_record(student.payment_records)
                dto.latest_payment_status = latest_record.payment_status
            else:
                dto.latest_payment_status = None
            dto.frequency = self.get_frequency(dto)





        self.signals.signal_student_dtos.emit(student_dtos)
        Session.remove()

    def _most_recent_payment_record(self, records):
        return max(records, key=lambda r: r.opened_at)

    def _student_in_lesson(self, student, lesson):
        return next((True for s in lesson.students if s.id == student.id), False)

    def filter_lessons_by_student(self, lessons, student):
        lessons_to_return = []
        for l in lessons:
            for s in l.students:
                if s.id == student.id:
                    lessons_to_return.append(l)
                    break
        return lessons_to_return

    def to_percent(self, value: float) -> str:
        return f"{value * 100:.0f}%"

    def up_to_x_months(self, lessons, x):
        today = date.today()

        def months_diff(d1, d2):
            months = (d1.year - d2.year) * 12 + (d1.month - d2.month)
            if d1.day < d2.day:
                months -= 1
            return months

        return [
            l for l in lessons
            if 0 <= months_diff(today, l.date) <= x
        ]

    def get_frequency(self, student: StudentDto):
        periods = {
            "Todo período": self.lessons,
            "Anual": self.up_to_x_months(self.lessons, 12),
            "Semestral": self.up_to_x_months(self.lessons, 6),
            "Mensal": list(filter(lambda l: l.date.month == date.today().month, self.up_to_x_months(self.lessons, 6)))
        }

        frequencies = {}

        for label, period_lessons in periods.items():
            total_num = len(period_lessons)
            student_lessons = self.filter_lessons_by_student(period_lessons, student)
            student_num = len(student_lessons)
            frequencies[label] = f"{int((student_num * 100) / total_num) if total_num else 0}%"

        return frequencies



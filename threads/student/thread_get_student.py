from datetime import date

from PySide6.QtCore import QObject, Signal, QThread

from dtos.student_dto import StudentDto
from engine import Session
from repositories.lesson_repository import LessonRepository
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


class ThreadGetStudentSignals(QObject):
    signal_student_dto = Signal(StudentDto)


class ThreadGetStudent(QThread):
    def __init__(self, id):
        super(ThreadGetStudent, self).__init__()
        self.lesson_repository = None
        self.lessons = None
        self.signals = ThreadGetStudentSignals()

        self.session = None
        self.id = id
        self.student_repository: StudentRepository = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)
        self.lesson_repository = LessonRepository(self.session)

        self.lessons = self.lesson_repository.get_all()
        student = self.student_repository.get_by_id(self.id)
        student_dto = StudentService.get_dto(student)
        student_dto.frequency = self.get_frequency(student_dto)

        self.signals.signal_student_dto.emit(student_dto)
        Session.remove()

    def up_to_x_months(self, lessons, x):
        today = date.today()

        def months_diff(d1, d2):
            return (d1.year - d2.year) * 12 + (d1.month - d2.month)

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


    def filter_lessons_by_student(self, lessons, student):
        lessons_to_return = []
        for l in lessons:
            for s in l.students:
                if s.id == student.id:
                    lessons_to_return.append(l)
                    break
        return lessons_to_return
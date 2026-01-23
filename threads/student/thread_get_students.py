from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from services.student_service import StudentService
from repositories.student_repository import StudentRepository



class ThreadGetStudentsSignals(QObject):
    signal_student_dtos = Signal(list)


class ThreadGetStudents(QThread):
    def __init__(self):
        super(ThreadGetStudents, self).__init__()
        self.signals = ThreadGetStudentsSignals()

        self.session = None
        self.student_repository: StudentRepository = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)

        students = self.student_repository.get_all()
        student_dtos = [StudentService.get_dto(student) for student in students]
        for dto in student_dtos:
            student = next((s for s in students if s.id == dto.id), None)
            latest_record = self._most_recent_payment_record(student.payment_records)
            dto.latest_payment_status = latest_record.payment_status


        self.signals.signal_student_dtos.emit(student_dtos)
        Session.remove()

    def _most_recent_payment_record(self, records):
        return max(records, key=lambda r: r.opened_at)

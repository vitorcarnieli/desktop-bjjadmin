from PySide6.QtCore import QObject, Signal, QThread

from dtos.student_dto import StudentDto
from engine import Session
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


class ThreadEditStudentSignals(QObject):
    signal_student_dto = Signal(StudentDto)


class ThreadEditStudent(QThread):
    def __init__(self, dto: StudentDto):
        super(ThreadEditStudent, self).__init__()
        self.signals = ThreadEditStudentSignals()

        self.session = None
        self.updatable_student_dto = dto
        self.student_repository: StudentRepository = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)

        student = self.student_repository.get_by_id(self.updatable_student_dto.id)
        student.name = self.updatable_student_dto.name
        student.phone = self.updatable_student_dto.phone
        student.belt = self.updatable_student_dto.belt
        student.observation = self.updatable_student_dto.observation
        student.date_of_birth = self.updatable_student_dto.date_of_birth
        student.sex = self.updatable_student_dto.sex
        student.plan_id = self.updatable_student_dto.plan_id
        student.class_id = self.updatable_student_dto.class_id
        student.is_inactive = self.updatable_student_dto.is_inactive

        self.student_repository.update(student)
        dto = StudentService.get_dto(student)
        latest_record = self._most_recent_payment_record(student.payment_records)
        dto.latest_payment_status = latest_record.payment_status

        self.signals.signal_student_dto.emit(
            dto
        )
        Session.remove()

    def _most_recent_payment_record(self, records):
        return max(records, key=lambda r: r.opened_at)
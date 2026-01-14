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
        student.plan_id = self.updatable_student_dto.plan_id
        student.class_id = self.updatable_student_dto.class_id
        student.observation = self.updatable_student_dto.observation

        self.student_repository.update(student)

        self.signals.signal_student_dto.emit(
            StudentService.get_dto(student)
        )
        Session.remove()

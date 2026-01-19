from PySide6.QtCore import QObject, Signal, QThread

from dtos.student_dto import StudentDto
from engine import Session
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


class ThreadGetStudentSignals(QObject):
    signal_student_dto = Signal(StudentDto)


class ThreadGetStudent(QThread):
    def __init__(self, id):
        super(ThreadGetStudent, self).__init__()
        self.signals = ThreadGetStudentSignals()

        self.session = None
        self.id = id
        self.student_repository: StudentRepository = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)

        student = self.student_repository.get_by_id(self.id)
        student_dto = StudentService.get_dto(student)

        self.signals.signal_student_dto.emit(student_dto)
        Session.remove()

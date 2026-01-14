from PySide6.QtCore import QObject, Signal, QThread

from dtos.message import Message
from dtos.student_dto import StudentDto
from engine import Session
from enums.message_type import MessageType
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


class ThreadAddStudentSignals(QObject):
    signal_student_dto = Signal(StudentDto)
    signal_message = Signal(Message)


class ThreadAddStudent(QThread):
    def __init__(self, student_dto: StudentDto = None):
        super(ThreadAddStudent, self).__init__()
        self.signals = ThreadAddStudentSignals()

        self.session = None
        self.student_dto = student_dto
        self.student_repository: StudentRepository = None

    def run(self):
        try:
            self.session = Session()
            self.student_repository = StudentRepository(self.session)

            student = StudentService.get_model(self.student_dto)
            self.student_repository.add(student)

            self.student_dto.id = student.id
            self.signals.signal_student_dto.emit(self.student_dto)
        except Exception as e:
            self.signals.signal_message.emit(
                Message(MessageType.ERROR, str(e))
            )
        Session.remove()

from PySide6.QtCore import QObject, Signal, QThread

from dtos.message import Message
from dtos.student_dto import StudentDto
from engine import Session
from enums.message_type import MessageType
from repositories.class_repository import ClassRepository
from repositories.plan_repository import PlanRepository
from repositories.student_repository import StudentRepository
from services.class_service import ClassService
from services.plan_service import PlanService
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
        self.class_repository: ClassRepository = None
        self.plan_repository: PlanRepository = None

    def run(self):
        try:
            self.session = Session()
            self.student_repository = StudentRepository(self.session)

            student = StudentService.get_model(self.student_dto)
            self.student_repository.add(student)

            self.student_dto.id = student.id

            self.plan_repository = PlanRepository(self.session)
            plan = PlanService.get_dto(self.plan_repository.get_by_id(self.student_dto.plan_id))

            self.class_repository = ClassRepository(self.session)
            lesson_class = ClassService.get_dto(self.class_repository.get_by_id(self.student_dto.class_id))

            self.student_dto.plan = plan
            self.student_dto.lesson_class = lesson_class



            self.signals.signal_student_dto.emit(self.student_dto)
        except Exception as e:
            print(e)
            self.signals.signal_message.emit(
                Message(MessageType.ERROR, str(e))
            )
        Session.remove()

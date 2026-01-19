from PySide6.QtCore import QObject, Signal, QThread

from dtos.class_dto import ClassDto
from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from repositories.class_repository import ClassRepository
from services.class_service import ClassService

class ThreadAddClassSignals(QObject):
    signal_class_dto = Signal(ClassDto)
    signal_message = Signal(Message)


class ThreadAddClass(QThread):
    def __init__(self, class_dto: ClassDto=None):
        super(ThreadAddClass, self).__init__()
        self.signals = ThreadAddClassSignals()

        self.session = None
        self.class_dto = class_dto
        self.class_repository: ClassRepository = None
    
    def run(self):
        try:
            self.session = Session()
            self.class_repository = ClassRepository(self.session)

            lesson_class = ClassService.get_model(self.class_dto)
            self.class_repository.add(lesson_class)
            self.class_dto.id = lesson_class.id
            self.signals.signal_class_dto.emit(self.class_dto)
        except Exception as e:
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))
        Session.remove()

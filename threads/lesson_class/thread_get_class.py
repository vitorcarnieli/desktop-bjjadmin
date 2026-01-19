from PySide6.QtCore import QObject, Signal, QThread

from dtos.class_dto import ClassDto
from engine import Session
from repositories.class_repository import ClassRepository
from services.class_service import ClassService


class ThreadGetClassSignals(QObject):
    signal_class_dto = Signal(ClassDto)


class ThreadGetClass(QThread):
    def __init__(self, id):
        super(ThreadGetClass, self).__init__()
        self.signals = ThreadGetClassSignals()

        self.session = None
        self.class_dto = None
        self.id = id
        self.class_repository: ClassRepository = None

    def run(self):
        self.session = Session()
        self.class_repository = ClassRepository(self.session)
        lesson_class = self.class_repository.get_by_id(self.id)
        self.class_dto = ClassService.get_dto(lesson_class)
        self.signals.signal_class_dto.emit(self.class_dto)
        Session.remove()

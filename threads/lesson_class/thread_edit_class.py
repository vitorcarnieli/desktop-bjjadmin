from PySide6.QtCore import QObject, Signal, QThread

from dtos.class_dto import ClassDto
from engine import Session
from repositories.class_repository import ClassRepository
from services.class_service import ClassService


class ThreadEditClassSignals(QObject):
    signal_class_dto = Signal(ClassDto)


class ThreadEditClass(QThread):
    def __init__(self, dto):
        super(ThreadEditClass, self).__init__()
        self.signals = ThreadEditClassSignals()

        self.session = None
        self.updatable_class_dto = dto
        self.class_dto = None
        self.class_repository: ClassRepository = None

    def run(self):
        self.session = Session()
        self.class_repository = ClassRepository(self.session)

        lesson_class = self.class_repository.get_by_id(self.updatable_class_dto.id)
        lesson_class.name = self.updatable_class_dto.name
        lesson_class.observation = self.updatable_class_dto.observation
        self.class_repository.update(lesson_class)

        self.signals.signal_class_dto.emit(ClassService.get_dto(lesson_class))
        Session.remove()

from PySide6.QtCore import QObject, Signal, QThread

from dtos.class_dto import ClassDto
from engine import Session
from repositories.class_repository import ClassRepository
from services.class_service import ClassService


class ThreadGetClassesSignals(QObject):
    signal_class_dtos = Signal(ClassDto)


class ThreadGetClasses(QThread):
    def __init__(self):
        super(ThreadGetClasses, self).__init__()
        self.signals = ThreadGetClassesSignals()

        self.session = None
        self.class_dtos = None
        self.class_repository: ClassRepository = None

    def run(self):
        self.session = Session()
        self.class_repository = ClassRepository(self.session)

        class_dtos = self.class_repository.get_all()
        self.class_dtos = [ClassService.get_dto(c) for c in class_dtos]
        self.signals.signal_class_dtos.emit(self.class_dtos)
        Session.remove()

from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.class_repository import ClassRepository


class ThreadRemoveClassSignals(QObject):
    signal_finished = Signal(int)


class ThreadRemoveClass(QThread):
    def __init__(self, id):
        super(ThreadRemoveClass, self).__init__()
        self.signals = ThreadRemoveClassSignals()

        self.session = None
        self.id = id
        self.class_repository: ClassRepository = None

    def run(self):
        self.session = Session()
        self.class_repository = ClassRepository(self.session)
        lesson_class = self.class_repository.get_by_id(self.id)
        self.class_repository.delete(lesson_class)
        self.signals.signal_finished.emit(self.id)
        Session.remove()

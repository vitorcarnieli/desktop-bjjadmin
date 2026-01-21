from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.class_repository import ClassRepository
from repositories.lesson_repository import LessonRepository
from repositories.student_repository import StudentRepository


class ThreadRemoveLessonSignals(QObject):
    signal_finished = Signal(int)


class ThreadRemoveLesson(QThread):
    def __init__(self, id):
        super(ThreadRemoveLesson, self).__init__()
        self.signals = ThreadRemoveLessonSignals()

        self.session = None
        self.id = id
        self.lesson_repository: LessonRepository = None

    def run(self):
        self.session = Session()
        self.lesson_repository = LessonRepository(self.session)
        lesson = self.lesson_repository.get_by_id(self.id)

        self.lesson_repository.delete(lesson)
        print(self.id)
        self.signals.signal_finished.emit(int(self.id))
        Session.remove()

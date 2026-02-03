from PySide6.QtCore import QObject, Signal, QThread

from dtos.class_dto import ClassDto
from dtos.lesson_dto import LessonDto
from engine import Session
from repositories.class_repository import ClassRepository
from repositories.lesson_repository import LessonRepository
from services.class_service import ClassService
from services.lesson_service import LessonService


class ThreadGetLessonsSignals(QObject):
    signal_lesson_dtos = Signal(LessonDto)


class ThreadGetLessons(QThread):
    def __init__(self):
        super(ThreadGetLessons, self).__init__()
        self.signals = ThreadGetLessonsSignals()

        self.session = None
        self.lesson_dtos = None
        self.lesson_repository: LessonRepository = None

    def run(self):
        self.session = Session()
        self.lesson_repository = LessonRepository(self.session)

        lesson_dtos = self.lesson_repository.get_all()
        self.lesson_dtos = [LessonService.get_dto(l) for l in lesson_dtos]
        self.signals.signal_lesson_dtos.emit(self.lesson_dtos)
        Session.remove()

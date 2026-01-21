from PySide6.QtCore import QObject, Signal, QThread
from dtos.lesson_dto import LessonDto
from engine import Session
from repositories.lesson_repository import LessonRepository
from services.lesson_service import LessonService


class ThreadGetLessonsByDateSignals(QObject):
    signal_lesson_dtos = Signal(LessonDto)


class ThreadGetLessonsByDate(QThread):
    def __init__(self, date):
        super(ThreadGetLessonsByDate, self).__init__()
        self.signals = ThreadGetLessonsByDateSignals()

        self.session = None
        self.lesson_dtos = None
        self.date = date
        self.lesson_repository: LessonRepository = None

    def run(self):
        try:
            self.session = Session()
            self.lesson_repository = LessonRepository(self.session)

            lesson_dtos = self.lesson_repository.get_by_date(self.date)
            self.lesson_dtos = [LessonService.get_dto(l) for l in lesson_dtos]
            self.signals.signal_lesson_dtos.emit(self.lesson_dtos)
            Session.remove()
        except Exception as e:
            print(e)


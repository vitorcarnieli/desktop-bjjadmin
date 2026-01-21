from datetime import date

from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.lesson_repository import LessonRepository


class ThreadGetLessonDatesSignals(QObject):
    signal_dates = Signal(date)


class ThreadGetLessonDates(QThread):
    def __init__(self):
        super(ThreadGetLessonDates, self).__init__()
        self.signals = ThreadGetLessonDatesSignals()

        self.session = None
        self.dates = None
        self.lesson_repository: LessonRepository = None

    def run(self):
        self.session = Session()
        self.lesson_repository = LessonRepository(self.session)

        dates = self.lesson_repository.get_lesson_dates()
        self.signals.signal_dates.emit(dates)
        Session.remove()

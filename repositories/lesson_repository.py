from datetime import date

from engine import Session
from models import Lesson
from repositories.base_repository import BaseRepository


class LessonRepository(BaseRepository):

    def __init__(self, session: Session):
        super(LessonRepository, self).__init__(session, Lesson)

    def get_by_month_and_year(self, year_, month_):
        start = date(year_, month_, 1)

        if month_ == 12:
            end = date(year_ + 1, 1, 1)
        else:
            end = date(year_, month_ + 1, 1)

        return (
            self.session
            .query(Lesson)
            .filter(Lesson.date >= start)
            .filter(Lesson.date < end)
            .all()
        )

    def get_by_month(self, month_):
        today = date.today()
        year = today.year

        start = date(year, month_, 1)

        if month_ == 12:
            end = date(year + 1, 1, 1)
        else:
            end = date(year, month_ + 1, 1)

        return (
            self.session
            .query(Lesson)
            .filter(Lesson.date >= start)
            .filter(Lesson.date < end)
            .all()
        )

    def get_by_year(self, year_):
        start = date(year_, 1, 1)
        end = date(year_ + 1, 1, 1)

        return (
            self.session
            .query(Lesson)
            .filter(Lesson.date >= start)
            .filter(Lesson.date < end)
            .all()
        )

    def get_by_date(self, date_):
        return (
            self.session
            .query(Lesson)
            .filter(Lesson.date == date_)
            .all()
        )

    def get_lesson_dates(self):
        return (
            self.session
            .query(Lesson.date)
            .distinct()
            .order_by(Lesson.date)
            .all()
        )

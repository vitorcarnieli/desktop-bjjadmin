from engine import Session
from models import LessonClass
from repositories.base_repository import BaseRepository


class ClassRepository(BaseRepository):

    def __init__(self, session: Session):
        super(ClassRepository, self).__init__(session, LessonClass)
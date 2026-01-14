from engine import Session
from models import Student
from repositories.base_repository import BaseRepository


class StudentRepository(BaseRepository):

    def __init__(self, session: Session):
        super(StudentRepository, self).__init__(session, Student)
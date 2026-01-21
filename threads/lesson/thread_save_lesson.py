from PySide6.QtCore import QObject, Signal, QThread
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from dtos.lesson_dto import LessonDto
from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from models import lesson_students, Student
from repositories.class_repository import ClassRepository
from repositories.lesson_repository import LessonRepository
from repositories.student_repository import StudentRepository
from services.class_service import ClassService
from services.lesson_service import LessonService
from services.student_service import StudentService


class ThreadSaveLessonSignals(QObject):
    signal_lesson_dto = Signal(LessonDto)
    signal_message = Signal(Message)


class ThreadSaveLesson(QThread):
    def __init__(self, lesson_dto: LessonDto = None):
        super(ThreadSaveLesson, self).__init__()
        self.signals = ThreadSaveLessonSignals()

        self.session: Session = None
        self.lesson_dto = lesson_dto
        self.lesson_repository: LessonRepository = None

    def run(self):
        try:
            self.session = Session()
            self.lesson_repository = LessonRepository(self.session)


            lesson = LessonService.get_model(self.lesson_dto)
            lesson.students = []
            if lesson.id:
                lesson = self.session.merge(lesson)
            else:
                self.session.add(lesson)
                self.session.flush()

            lesson.students = [
                self.session.get(Student, s.id)
                for s in self.lesson_dto.students
            ]
            self.session.commit()

            self.lesson_dto.id = lesson.id
            self.lesson_dto.lesson_class = self._get_class()
            self.lesson_dto.students = self._get_students()

            self.signals.signal_lesson_dto.emit(self.lesson_dto)

        except Exception as e:
            self.session.rollback()
            print(e)
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

    def _get_class(self):
        class_repository = ClassRepository(self.session)
        return ClassService.get_dto(class_repository.get_by_id(self.lesson_dto.lesson_class_id))

    def _get_students(self):
        student_repository = StudentRepository(self.session)
        stmt = select(lesson_students).where(
            lesson_students.c.lesson_id == self.lesson_dto.id
        )
        results = self.session.execute(stmt).all()
        student_ids = [s.student_id for s in results]
        return [StudentService.get_dto(student_repository.get_by_id(id)) for id in student_ids]

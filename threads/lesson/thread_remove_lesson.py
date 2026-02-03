from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.class_repository import ClassRepository
from repositories.lesson_repository import LessonRepository
from repositories.student_repository import StudentRepository
from services.file_service import FileService


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
        for file_name in FileService.list_file_names("./profile_photos/lesson"):
            id_in_file_name = int(file_name.split(".")[0])
            if id_in_file_name == int(self.id):
                FileService.remove_file(f"./profile_photos/lesson/{file_name}")
                break

        self.signals.signal_finished.emit(int(self.id))
        Session.remove()

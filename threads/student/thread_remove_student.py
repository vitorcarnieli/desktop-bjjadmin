from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.student_repository import StudentRepository
from services.file_service import FileService


class ThreadRemoveStudentSignals(QObject):
    signal_finished = Signal(int)


class ThreadRemoveStudent(QThread):
    def __init__(self, id):
        super(ThreadRemoveStudent, self).__init__()
        self.signals = ThreadRemoveStudentSignals()

        self.session = None
        self.id = id
        self.student_repository: StudentRepository = None

    def run(self):
        self.session = Session()
        self.student_repository = StudentRepository(self.session)

        student = self.student_repository.get_by_id(self.id)
        for file_name in FileService.list_file_names("./profile_photos/student"):
            id_in_file_name = int(file_name.split(".")[0])
            if id_in_file_name == self.id:
                FileService.remove_file(f"./profile_photos/student/{file_name}")
                break

        self.student_repository.delete(student)

        self.signals.signal_finished.emit(self.id)
        Session.remove()

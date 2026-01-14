from PySide6.QtCore import QObject, Signal, QThread
from PySide6.scripts.metaobjectdump import Signal

from engine import Session
from repositories.student_repository import StudentRepository



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
        self.student_repository.delete(student)

        self.signals.signal_finished.emit(self.id)
        Session.remove()

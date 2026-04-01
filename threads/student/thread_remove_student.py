from PySide6.QtCore import QObject, Signal, QThread
from sqlalchemy import delete

from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from models.lesson_students import lesson_students
from repositories.student_repository import StudentRepository
from services.file_service import FileService


class ThreadRemoveStudentSignals(QObject):
    signal_finished = Signal(int)
    signal_message = Signal(object)


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
        try:
            student = self.student_repository.get_by_id(self.id)
            if not student:
                self.signals.signal_message.emit(
                    Message(MessageType.ERROR, "Aluno não encontrado para exclusão")
                )
                return

            self.session.execute(
                delete(lesson_students).where(lesson_students.c.student_id == self.id)
            )
            self.session.flush()

            profile_photo_dir = "./profile_photos/student"
            if FileService.create_folder(profile_photo_dir):
                for file_name in FileService.list_file_names(profile_photo_dir):
                    try:
                        id_in_file_name = int(file_name.split(".")[0])
                    except (TypeError, ValueError):
                        continue

                    if id_in_file_name == self.id:
                        FileService.remove_file(f"{profile_photo_dir}/{file_name}")
                        break

            self.student_repository.delete(student)
            self.signals.signal_finished.emit(self.id)
        except Exception as e:
            self.session.rollback()
            self.signals.signal_message.emit(
                Message(MessageType.ERROR, f"Não foi possível excluir o aluno: {e}")
            )
        finally:
            Session.remove()

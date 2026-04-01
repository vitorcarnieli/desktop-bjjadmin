from datetime import date

from PySide6.QtCore import QObject, Signal, QThread
from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from enums.payment_status import PaymentStatus
from repositories.class_repository import ClassRepository
from repositories.lesson_repository import LessonRepository
from repositories.payment_record_repository import PaymentRecordRepository
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


class ThreadLoadHomeSignals(QObject):
    signal_payment_infos = Signal(object)
    signal_birth_infos = Signal(object)
    signal_classes_infos = Signal(object)
    signal_lessons_infos = Signal(object)
    signal_message = Signal(Message)


class ThreadLoadHome(QThread):
    def __init__(self):
        super(ThreadLoadHome, self).__init__()
        self.signals = ThreadLoadHomeSignals()

        self.session: Session = None

        self.lesson_repository: LessonRepository = None
        self.student_repository: StudentRepository = None
        self.payment_record_repository: PaymentRecordRepository = None
        self.class_repository: ClassRepository = None

    def run(self):
        try:
            self.session = Session()
            self.signals.signal_payment_infos.emit(self._get_payment_infos())
            self.signals.signal_birth_infos.emit(self._get_birth_day_infos())
            self.signals.signal_classes_infos.emit(self._get_classes_infos())
            self.signals.signal_lessons_infos.emit(self._get_lessons_infos())



        except Exception as e:
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

    def _get_payment_infos(self):
        self.payment_record_repository = PaymentRecordRepository(self.session)
        records = self.payment_record_repository.get_payments_by_month(date.today())
        return {
            "total": len(records),
            "forgiven": sum(
                map(
                    lambda r: float(r.value),
                    filter(
                        lambda r: r.payment_status == PaymentStatus.FORGIVEN,
                        records
                    )
                )
            ),
            "paid": sum(
                        map(
                            lambda r: float(r.value),
                            filter(
                                lambda r: r.payment_status == PaymentStatus.PAID,
                                records
                            )
                        )
                    )
            ,
            "pending": sum(
                map(
                    lambda r: float(r.value),
                    filter(
                        lambda r: r.payment_status in (PaymentStatus.OVERDUE, PaymentStatus.OPEN),
                        records
                    )
                )
            )
        }

    def _get_classes_infos(self):
        self.class_repository = ClassRepository(self.session)

        classes = self.class_repository.get_all()

        total_students = sum(map(lambda c: len(c.students), classes))

        if total_students == 0:
            return []

        result = list(map(
            lambda c: {
                "label": c.name,
                "percent": round((len(c.students) / total_students) * 100, 2)
            },
            classes
        ))

        return result

    def _get_lessons_infos(self):

        self.lesson_repository = LessonRepository(self.session)

        lessons = self.lesson_repository.get_by_month(date.today().month)

        result = [0, 0, 0, 0, 0, 0, 0]

        for lesson in lessons:
            index = lesson.date.weekday()
            result[index] += 1

        return result

    def _get_birth_day_infos(self):
        self.student_repository = StudentRepository(self.session)
        students = self.student_repository.get_all()

        birth_month_students = list(map(lambda s: StudentService.get_dto(s), filter(
            lambda s: s.date_of_birth.month == date.today().month,
            students
        )))

        birth_day_student = list(map( lambda s: StudentService.get_dto(s), filter(
            lambda s: s.date_of_birth.month == date.today().month and s.date_of_birth.day == date.today().day,
            students
        )))

        return {
            "month": birth_month_students,
            "day": birth_day_student
        }





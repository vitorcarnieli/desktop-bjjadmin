from datetime import date

from PySide6.QtCore import QObject, Signal, QThread
from sqlalchemy import select, extract

from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from enums.payment_status import PaymentStatus
from models import PaymentRecord, Student
from repositories.lesson_repository import LessonRepository
from repositories.payment_record_repository import PaymentRecordRepository
from repositories.student_repository import StudentRepository
from services.payment_record_service import PaymentRecordService


class ThreadLoadPaymentRecordsSignals(QObject):
    signal_payment_record_dtos = Signal(object)
    signal_message = Signal(Message)


class ThreadLoadPaymentRecords(QThread):
    def __init__(self, date: date):
        super(ThreadLoadPaymentRecords, self).__init__()
        self.signals = ThreadLoadPaymentRecordsSignals()

        self.session: Session = None
        self.date = date
        self.payment_record_repository: PaymentRecordRepository = None
        self.student_repository: StudentRepository = None
        self.lessons_repository: LessonRepository = None

    def run(self):
        try:
            self.session = Session()

            self.student_repository = StudentRepository(self.session)
            self.payment_record_repository = PaymentRecordRepository(self.session)
            self.lessons_repository = LessonRepository(self.session)

            missing_records = self._students_without_record_this_month()
            if not missing_records:
                records = self._get_already_record_for_this_month()
            else:
                self._create_records_for_this_month(missing_records)
                records = self._get_already_record_for_this_month()

            self.signals.signal_payment_record_dtos.emit(records)

        except Exception as e:
            print(f"{e}")
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

    def _get_already_record_for_this_month(self):
        try:
            records = self.payment_record_repository.get_payments_by_month(self.date)
            for record in records:
                if date.today() >= record.due_date:
                    record.payment_status = PaymentStatus.OVERDUE
                    self.payment_record_repository.update(record)

            return [PaymentRecordService.get_dto(record) for record in records]
        except Exception as e:
            print(e)


    def _create_records_for_this_month(self, students):
        try:
            # filters students who were not present last month
            month = self.date.month - 1 if self.date.month > 1 else 12
            year = self.date.year if self.date.month > 1 else self.date.year - 1
            lessons = self.lessons_repository.get_by_month_and_year(year, month)
            students_present_last_month = [s.id for l in lessons for s in l.students]
            # save if student has created to month
            students_away = list(
                filter(lambda s: s.id not in students_present_last_month and ((s.created_at.date().year, s.created_at.date().month) > (date.today().year, date.today().month)),
                       students))
            for s in students_away:
                s.is_inactive = True
                self.student_repository.update(s)
                if s in students:
                    students.remove(s)
        except Exception as e:
            print(e)



        def create_record(student):
            try:
                record = PaymentRecord()
                record.student_id = student.id
                record.opened_at = date(self.date.year, self.date.month, 1)
                record.due_date = date(self.date.year, self.date.month, 10)
                record.value = student.plan.value
                record.payment_status = PaymentStatus.OPEN
                self.payment_record_repository.add(record)
                return record
            except Exception as e:
                print(e)


        return [PaymentRecordService.get_dto(create_record(student)) for student in students if not student.is_inactive]

    def _exist_records_for_this_month(self):
        try:
            today = date.today()
            stmt = select(PaymentRecord).where(
                extract("month", PaymentRecord.opened_at) == today.month,
                extract("year", PaymentRecord.opened_at) == today.year
            )

            return self.session.execute(stmt).first()
        except Exception as e:
            print(e)


    def _students_without_record_this_month(self) -> list[Student]:
        try:
            subquery = (
                select(PaymentRecord.student_id)
                .where(
                    extract("month", PaymentRecord.opened_at) == self.date.month,
                    extract("year", PaymentRecord.opened_at) == self.date.year
                )
                .distinct()
                .subquery()
            )

            stmt = (
                select(Student)
                .where(~Student.id.in_(select(subquery.c.student_id)))
            )
            students = list(
                filter(
                    lambda s: (
                                  s.created_at.year,
                                  s.created_at.month
                              ) <= (
                                  self.date.year,
                                  self.date.month
                              ),
                    self.session.execute(stmt).scalars().all()
                )
            )

            return students

        except Exception as e:
            print(e)

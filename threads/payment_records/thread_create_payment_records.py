from datetime import date

from PySide6.QtCore import QObject, Signal, QThread
from sqlalchemy import select, extract

from dtos.message import Message
from engine import Session
from enums.message_type import MessageType
from enums.payment_status import PaymentStatus
from models import PaymentRecord
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

    def run(self):
        try:
            self.session = Session()

            self.student_repository = StudentRepository(self.session)
            self.payment_record_repository = PaymentRecordRepository(self.session)
            if self._exist_records_for_this_month():
                records = self._get_already_record_for_this_month()
            else:
                records = self._create_records_for_this_month()

            self.signals.signal_payment_record_dtos.emit(records)
        except Exception as e:
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

    def _get_already_record_for_this_month(self):
        return [PaymentRecordService.get_dto(record) for record in self.payment_record_repository.get_payments_by_month(self.date)]

    def _create_records_for_this_month(self):
        def create_record(student):
            record = PaymentRecord()
            record.student_id = student.id
            to_day = date.today()
            record.opened_at = date(to_day.year, to_day.month, 1)
            record.due_date = date(to_day.year, to_day.month, 10)
            record.value = student.plan.value
            record.payment_status = PaymentStatus.OPEN
            self.payment_record_repository.add(record)
            return record

        return [PaymentRecordService.get_dto(create_record(student)) for student in self.student_repository.get_all()]

    def _exist_records_for_this_month(self):
        today = date.today()
        stmt = select(PaymentRecord).where(
            extract("month", PaymentRecord.opened_at) == today.month,
            extract("year", PaymentRecord.opened_at) == today.year
        )

        return self.session.execute(stmt).first()

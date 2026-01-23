from datetime import date

from PySide6.QtCore import QObject, Signal, QThread
from sqlalchemy import select, extract

from dtos.message import Message
from dtos.payment_record_dto import PaymentRecordDto
from engine import Session
from enums.message_type import MessageType
from enums.payment_status import PaymentStatus
from models import PaymentRecord
from repositories.payment_record_repository import PaymentRecordRepository
from repositories.student_repository import StudentRepository
from services.payment_record_service import PaymentRecordService


class ThreadEditPaymentRecordStatusSignals(QObject):
    signal_updated_record_dto = Signal(object)
    signal_message = Signal(Message)


class ThreadEditPaymentRecordStatus(QThread):
    def __init__(self, record_dto: PaymentRecordDto):
        super(ThreadEditPaymentRecordStatus, self).__init__()
        self.signals = ThreadEditPaymentRecordStatusSignals()

        self.session: Session = None
        self.record_dto = record_dto
        self.payment_record_repository: PaymentRecordRepository = None

    def run(self):
        try:
            self.session = Session()

            self.payment_record_repository = PaymentRecordRepository(self.session)
            record_model = self.payment_record_repository.get_by_id(self.record_dto.id)
            record_model.payment_status = self.record_dto.payment_status
            self.payment_record_repository.update(record_model)

            record_dto = PaymentRecordService.get_dto(record_model)

            self.signals.signal_updated_record_dto.emit(record_dto)
        except Exception as e:
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

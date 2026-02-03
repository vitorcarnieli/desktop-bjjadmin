from PySide6.QtCore import QObject, Signal, QThread

from dtos.message import Message
from dtos.payment_record_dto import PaymentRecordDto
from engine import Session
from enums.message_type import MessageType
from repositories.payment_record_repository import PaymentRecordRepository
from services.payment_record_service import PaymentRecordService


class ThreadEditPaymentRecordSignals(QObject):
    signal_updated_record_dto = Signal(object)
    signal_message = Signal(Message)


class ThreadEditPaymentRecord(QThread):
    def __init__(self, record_dto: PaymentRecordDto):
        super(ThreadEditPaymentRecord, self).__init__()
        self.signals = ThreadEditPaymentRecordSignals()

        self.session: Session = None
        self.record_dto = record_dto
        self.payment_record_repository: PaymentRecordRepository = None

    def run(self):
        try:
            self.session = Session()

            self.payment_record_repository = PaymentRecordRepository(self.session)
            record_model = self.payment_record_repository.get_by_id(self.record_dto.id)

            record_model.payment_status = self.record_dto.payment_status
            record_model.value = self.record_dto.value


            self.payment_record_repository.update(record_model)
            self.session.commit()

            record_dto = PaymentRecordService.get_dto(record_model)

            self.signals.signal_updated_record_dto.emit(record_dto)
        except Exception as e:
            print(e)
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))

        finally:
            Session.remove()

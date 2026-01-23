from PySide6.QtWidgets import QDialog

from dtos.payment_record_dto import PaymentRecordDto
from enums.payment_status import PaymentStatus
from threads.payment_records.thread_edit_payment_record import ThreadEditPaymentRecord
from views.ui.converted.records.ui_edit_record_value import Ui_EditRecordValue


class EditRecordValue(QDialog, Ui_EditRecordValue):

    def __init__(self, parent, to_edit_record_dto: PaymentRecordDto = None):
        super(EditRecordValue, self).__init__(parent)
        self.thread_edit_payment_record = None
        self.setupUi(self)
        self.to_edit_record_dto = to_edit_record_dto
        self.updated_record_dto: PaymentRecordDto = None
        self.pushButton.clicked.connect(self.on_click_btn_save)
        self.set_form_date()

    def set_form_date(self):
        self.doubleSpinBox.setValue(float(self.to_edit_record_dto.value))

    def get_form_data(self):
        self.to_edit_record_dto.value = self.doubleSpinBox.value()
        self.to_edit_record_dto.payment_status = PaymentStatus.OPEN
        return self.to_edit_record_dto

    def on_click_btn_save(self):
        self.to_edit_record_dto = self.get_form_data()
        self.setEnabled(False)
        self.start_thread_edit_payment_record()

    def on_signal_updated_record_dto(self, record_dto):
        self.updated_record_dto = record_dto
        self.accept()
        
    def start_thread_edit_payment_record(self):
        self.thread_edit_payment_record = ThreadEditPaymentRecord(self.to_edit_record_dto)
        self.thread_edit_payment_record.signals.signal_updated_record_dto.connect(self.on_signal_updated_record_dto)
        self.thread_edit_payment_record.start()

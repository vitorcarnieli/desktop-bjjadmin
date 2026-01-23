from dtos.payment_record_dto import PaymentRecordDto
from models import PaymentRecord
from services.student_service import StudentService


class PaymentRecordService:

    @staticmethod
    def get_dto(model: PaymentRecord):
        dto = PaymentRecordDto()
        dto.id = model.id
        dto.student_id = model.student_id

        dto.opened_at = model.opened_at
        dto.due_date = model.due_date
        dto.paid_at = model.paid_at

        dto.value = model.value
        dto.observation = model.observation
        dto.payment_status = model.payment_status

        if model.student:
            dto.student = StudentService.get_dto(model.student)

        return dto

    @staticmethod
    def get_model(dto: PaymentRecordDto):
        model = PaymentRecord()
        model.id = dto.id
        model.student_id = dto.student_id

        model.opened_at = dto.opened_at
        model.due_date = dto.due_date
        model.paid_at = dto.paid_at

        model.value = dto.value
        model.observation = dto.observation
        model.payment_status = dto.payment_status

        if dto.student:
            model.student = StudentService.get_model(dto.student)

        return model

from dtos.plan_dto import PlanDto
from models.plan import Plan


class PlanService:

    @staticmethod
    def get_dto(model: Plan):
        dto = PlanDto()
        dto.id = model.id
        dto.name = model.name
        dto.value = model.value
        dto.observation = model.observation
        dto.students = model.students
        return dto

    @staticmethod
    def get_model(dto: PlanDto):
        model = Plan()
        model.id = dto.id
        model.name = dto.name
        model.value = dto.value
        model.observation = dto.observation
        #model.students = dto.students
        return model

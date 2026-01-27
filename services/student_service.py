from models.student import Student
from dtos.student_dto import StudentDto
from services.class_service import ClassService
from services.plan_service import PlanService


class StudentService:

    @staticmethod
    def get_dto(model: Student):
        dto = StudentDto()
        dto.id = model.id
        dto.name = model.name
        dto.phone = model.phone
        dto.belt = model.belt
        dto.plan_id = model.plan_id
        dto.class_id = model.class_id
        dto.observation = model.observation
        if model.plan:
            dto.plan = PlanService.get_dto(model.plan)
        if model.lesson_class:
            dto.lesson_class = ClassService.get_dto(model.lesson_class)
        dto.sex = model.sex
        dto.date_of_birth = model.date_of_birth
        dto.is_inactive = model.is_inactive

        return dto

    @staticmethod
    def get_model(dto: StudentDto):
        model = Student()
        model.id = dto.id
        model.name = dto.name
        model.phone = dto.phone
        model.belt = dto.belt
        if dto.plan:
            model.plan = PlanService.get_model(dto.plan)
        if dto.lesson_class:
            model.lesson_class = ClassService.get_model(dto.lesson_class)
        model.plan_id = dto.plan_id
        model.class_id = dto.class_id
        model.observation = dto.observation
        model.date_of_birth = dto.date_of_birth
        model.sex = dto.sex
        model.is_inactive = dto.is_inactive
        return model

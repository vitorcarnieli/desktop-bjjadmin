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
        dto.plan = PlanService.get_dto(model.plan)
        dto.lesson_class = ClassService.get_dto(dto.lesson_class)

        return dto

    @staticmethod
    def get_model(dto: StudentDto):
        model = Student()
        model.id = dto.id
        model.name = dto.name
        model.phone = dto.phone
        model.belt = dto.belt
        model.plan_id = dto.plan_id
        model.plan = PlanService.get_model(dto.plan)
        model.class_id = dto.class_id
        model.lesson_class = ClassService.get_model(dto.lesson_class)
        model.observation = dto.observation
        return model

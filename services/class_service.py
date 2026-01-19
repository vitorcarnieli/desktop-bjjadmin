from dtos.class_dto import ClassDto
from models.lesson_class import LessonClass


class ClassService:

    @staticmethod
    def get_dto(model: LessonClass):
        dto = ClassDto()
        dto.id = model.id
        dto.name = model.name
        dto.observation = model.observation
        dto.students = model.students
        return dto

    @staticmethod
    def get_model(dto: ClassDto):
        model = LessonClass()
        model.id = dto.id
        model.name = dto.name
        model.observation = dto.observation
        # model.students = dto.students
        return model

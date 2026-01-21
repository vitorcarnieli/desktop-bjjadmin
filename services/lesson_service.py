from dtos.class_dto import ClassDto
from dtos.lesson_dto import LessonDto
from models import Lesson
from models.lesson_class import LessonClass
from services.class_service import ClassService
from services.student_service import StudentService


class LessonService:

    @staticmethod
    def get_dto(model: Lesson):
            dto = LessonDto()
            dto.id = model.id
            dto.name = model.name
            dto.observation = model.observation
            dto.date = model.date
            dto.start_time = model.start_time
            dto.end_time = model.end_time
            dto.lesson_class_id = model.lesson_class_id
            if model.lesson_class:
                dto.lesson_class = ClassService.get_dto(model.lesson_class)
            if model.students:
                dto.students = [StudentService.get_dto(s) for s in model.students]

            return dto


    @staticmethod
    def get_model(dto: LessonDto):
        model = Lesson()
        model.id = dto.id
        model.name = dto.name
        model.observation = dto.observation
        model.date = dto.date
        model.start_time = dto.start_time
        model.end_time = dto.end_time
        model.lesson_class_id = dto.lesson_class_id
        if dto.lesson_class:
            model.lesson_class = ClassService.get_model(dto.lesson_class)
        if dto.students:
            model.students = [StudentService.get_model(s) for s in dto.students]

        return model


from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from models.base_model import BaseModel

from sqlalchemy.orm import relationship

from models.lesson_students import lesson_students


class Lesson(BaseModel):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    observation = Column(String)
    date = Column(Date, nullable=False)

    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    lesson_class_id = Column(
        Integer,
        ForeignKey("classes.id"),
        nullable=False
    )

    lesson_class = relationship("LessonClass")

    students = relationship(
        "Student",
        secondary=lesson_students,
        back_populates="lessons"
    )

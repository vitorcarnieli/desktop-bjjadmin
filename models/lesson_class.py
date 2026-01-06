from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel

from sqlalchemy.orm import relationship

class LessonClass(BaseModel):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    observation = Column(String)

    students = relationship(
        "Student",
        back_populates="lesson_class",
        cascade="all, delete-orphan"
    )

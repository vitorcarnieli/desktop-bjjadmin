from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum

from enums.belts import Belt
from models.base_model import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

    belt = Column(
        SAEnum(Belt, name="belt_enum"),
        nullable=False
    )

    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    observation = Column(String)

    plan = relationship("Plan", back_populates="students")
    lesson_class = relationship("LessonClass", back_populates="students")

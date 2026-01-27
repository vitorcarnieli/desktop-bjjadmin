from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum

from enums.belts import Belt
from enums.sex import Sex
from models.base_model import BaseModel
from models.lesson_students import lesson_students


class Student(BaseModel):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    is_inactive = Column(Boolean, default=False)

    date_of_birth = Column(Date, nullable=False)

    sex = Column(SAEnum(Sex, name="sex_enum"), nullable=False)
    belt = Column(SAEnum(Belt, name="belt_enum"), nullable=False)

    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False, server_default="1")
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False, server_default="1")

    observation = Column(String)

    plan = relationship("Plan", back_populates="students")
    lesson_class = relationship("LessonClass", back_populates="students")

    payment_records = relationship(
        "PaymentRecord",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    lessons = relationship(
        "Lesson",
        secondary=lesson_students,
        back_populates="students"
    )

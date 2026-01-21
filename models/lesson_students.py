from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base_model import BaseModel

lesson_students = Table(
    "lesson_students",
    BaseModel.metadata,
    Column("lesson_id", Integer, ForeignKey("lessons.id"), primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
)

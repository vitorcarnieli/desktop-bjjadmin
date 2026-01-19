from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

class Plan(BaseModel):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    observation = Column(String)

    students = relationship("Student")

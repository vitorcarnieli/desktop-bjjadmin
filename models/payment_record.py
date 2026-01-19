from sqlalchemy import Column, Integer, String, Date, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from enums.payment_status import PaymentStatus
from models.base_model import BaseModel


def first_day_of_month():
    today = date.today()
    return today.replace(day=1)


def ninth_day_of_month():
    today = date.today()
    return today.replace(day=9)


class PaymentRecord(BaseModel):
    __tablename__ = "payment_records"

    id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    student = relationship("Student", back_populates="payment_records")

    # datas
    opened_at = Column(
        Date,
        nullable=False,
        default=first_day_of_month
    )

    due_date = Column(
        Date,
        nullable=False,
        default=ninth_day_of_month
    )

    paid_at = Column(
        Date,
        nullable=True
    )

    value = Column(String, nullable=False)
    observation = Column(String)

    payment_status = Column(
        SAEnum(PaymentStatus, name="payment_status_enum"),
        nullable=False
    )

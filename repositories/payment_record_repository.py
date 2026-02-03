from datetime import date

from sqlalchemy import select

from engine import Session
from models import PaymentRecord
from repositories.base_repository import BaseRepository


class PaymentRecordRepository(BaseRepository):

    def __init__(self, session: Session):
        super(PaymentRecordRepository, self).__init__(session, PaymentRecord)

    def get_payments_by_month(self, target_date: date) -> list[PaymentRecord]:
        start = target_date.replace(day=1)

        if target_date.month == 12:
            end = date(target_date.year + 1, 1, 1)
        else:
            end = date(target_date.year, target_date.month + 1, 1)

        stmt = select(PaymentRecord).where(
            PaymentRecord.opened_at >= start,
            PaymentRecord.opened_at < end
        )
        return self.session.execute(stmt).scalars().all()

from engine import Session
from models.plan import Plan
from repositories.base_repository import BaseRepository


class PlanRepository(BaseRepository):

    def __init__(self, session: Session):
        super(PlanRepository, self).__init__(session, Plan)
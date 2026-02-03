from PySide6.QtCore import QObject, Signal, QThread

from dtos.plan_dto import PlanDto
from engine import Session
from repositories.plan_repository import PlanRepository
from services.plan_service import PlanService


class ThreadGetPlanSignals(QObject):
    signal_plan_dto = Signal(PlanDto)


class ThreadGetPlan(QThread):
    def __init__(self, id):
        super(ThreadGetPlan, self).__init__()
        self.signals = ThreadGetPlanSignals()

        self.session = None
        self.plan_dto = None
        self.id = id
        self.plan_repository: PlanRepository = None

    def run(self):
        self.session = Session()
        self.plan_repository = PlanRepository(self.session)
        plan = self.plan_repository.get_by_id(self.id)
        self.plan_dto = PlanService.get_dto(plan)
        self.signals.signal_plan_dto.emit(self.plan_dto)
        Session.remove()

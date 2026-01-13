from PySide6.QtCore import QObject, Signal, QThread

from dtos.plan_dto import PlanDto
from engine import Session
from repositories.plan_repository import PlanRepository
from services.plan_service import PlanService


class ThreadEditPlanSignals(QObject):
    signal_plan_dto = Signal(PlanDto)


class ThreadEditPlan(QThread):
    def __init__(self, dto):
        super(ThreadEditPlan, self).__init__()
        self.signals = ThreadEditPlanSignals()

        self.session = None
        self.updatable_plan_dto = dto
        self.plan_dto = None
        self.plan_repository: PlanRepository = None

    def run(self):
        self.session = Session()
        self.plan_repository = PlanRepository(self.session)

        plan = self.plan_repository.get_by_id(self.updatable_plan_dto.id)
        plan.name = self.updatable_plan_dto.name
        plan.value = self.updatable_plan_dto.value
        plan.observation = self.updatable_plan_dto.observation
        self.plan_repository.update(plan)

        self.signals.signal_plan_dto.emit(PlanService.get_dto(plan))
        Session.remove()

from PySide6.QtCore import QObject, Signal, QThread

from dtos.plan_dto import PlanDto
from engine import Session
from repositories.plan_repository import PlanRepository
from services.plan_service import PlanService


class ThreadGetPlansSignals(QObject):
    signal_plan_dtos = Signal(PlanDto)


class ThreadGetPlans(QThread):
    def __init__(self):
        super(ThreadGetPlans, self).__init__()
        self.signals = ThreadGetPlansSignals()

        self.session = None
        self.plan_dtos = None
        self.plan_repository: PlanRepository = None

    def run(self):
        self.session = Session()
        self.plan_repository = PlanRepository(self.session)

        plan_dtos = self.plan_repository.get_all()
        self.plan_dtos = [PlanService.get_dto(plan) for plan in plan_dtos]
        self.signals.signal_plan_dtos.emit(self.plan_dtos)
        Session.remove()

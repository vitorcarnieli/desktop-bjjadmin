from PySide6.QtCore import QObject, Signal, QThread


from dtos.message import Message
from dtos.plan_dto import PlanDto
from engine import Session
from enums.message_type import MessageType
from repositories.plan_repository import PlanRepository
from services.plan_service import PlanService


class ThreadAddPlanSignals(QObject):
    signal_plan_dto = Signal(PlanDto)
    signal_message = Signal(Message)


class ThreadAddPlan(QThread):
    def __init__(self, plan_dto: PlanDto=None):
        super(ThreadAddPlan, self).__init__()
        self.signals = ThreadAddPlanSignals()

        self.session = None
        self.plan_dto = plan_dto
        self.plan_repository: PlanRepository = None
    
    def run(self):
        try:
            self.session = Session()
            self.plan_repository = PlanRepository(self.session)

            plan = PlanService.get_model(self.plan_dto)
            self.plan_repository.add(plan)
            self.plan_dto.id = plan.id
            self.signals.signal_plan_dto.emit(self.plan_dto)
        except Exception as e:
            self.signals.signal_message.emit(Message(MessageType.ERROR, str(e)))
        Session.remove()

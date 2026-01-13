from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.plan_repository import PlanRepository


class ThreadRemovePlanSignals(QObject):
    signal_finished = Signal(int)


class ThreadRemovePlan(QThread):
    def __init__(self, id):
        super(ThreadRemovePlan, self).__init__()
        self.signals = ThreadRemovePlanSignals()

        self.session = None
        self.id = id
        self.plan_repository: PlanRepository = None

    def run(self):
        self.session = Session()
        self.plan_repository = PlanRepository(self.session)
        plan = self.plan_repository.get_by_id(self.id)
        self.plan_repository.delete(plan)
        self.signals.signal_finished.emit(self.id)
        Session.remove()

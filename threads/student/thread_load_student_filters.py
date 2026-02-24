from PySide6.QtCore import QObject, Signal, QThread

from engine import Session
from repositories.class_repository import ClassRepository
from repositories.plan_repository import PlanRepository
from services.class_service import ClassService
from services.plan_service import PlanService
from services.student_service import StudentService
from repositories.student_repository import StudentRepository



class ThreadLoadStudentFiltersSignals(QObject):
    signal_filters = Signal(object)


class ThreadLoadStudentFilters(QThread):
    def __init__(self):
        super(ThreadLoadStudentFilters, self).__init__()
        self.signals = ThreadLoadStudentFiltersSignals()

        self.session = None
        self.student_repository: StudentRepository = None

    def run(self):
        try:
            self.session = Session()
            class_repo = ClassRepository(self.session)
            plan_repo = PlanRepository(self.session)

            filters = {
                "class": [ClassService.get_dto(c) for c in class_repo.get_all()],
                "plan": [PlanService.get_dto(p) for p in plan_repo.get_all()]
            }
            self.signals.signal_filters.emit(filters)

            Session.remove()
        except Exception as e:
            print(e)

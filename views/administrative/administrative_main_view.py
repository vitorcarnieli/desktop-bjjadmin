from PyQt6.QtWidgets import QMainWindow


class AdministrativeMainView:

    def __init__(self, main_view: QMainWindow):
        self.main_view = main_view

        self.tab_plan = AdministrativeTabClassView(self.main_view)
        self.tab_class = AdministrativeTabPlanView(self.main_view)

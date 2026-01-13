from views.administrative.administrative_tab_plan_view import AdministrativeTabPlanView
from views.ui.converted.ui_main_view import Ui_MainWindow


class AdministrativeMainView:

    def __init__(self, main_view: Ui_MainWindow):
        self.main_view = main_view

        self.tab_plan = AdministrativeTabPlanView(self.main_view)
        #self.tab_class = AdministrativeTabPlanView(self.main_view)

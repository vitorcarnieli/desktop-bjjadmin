from PySide6.QtGui import Qt
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from dtos.plan_dto import PlanDto
from threads.plan.thread_get_plans import ThreadGetPlans
from threads.plan.thread_remove_plan import ThreadRemovePlan
from views.administrative.plan.add_plan_view import AddPlanView
from views.confirm_view import ConfirmView
from views.ui.converted.ui_main_view import Ui_MainWindow


class AdministrativeTabPlanView:

    def __init__(self, main_view: Ui_MainWindow):
        self.main_view = main_view

        self.main_view.table_plan.setColumnHidden(0, True)

        self.main_view.btn_add_plan.clicked.connect(self.on_click_btn_add_plan)
        self.main_view.btn_remove_plan.clicked.connect(self.on_click_btn_remove_plan)
        self.main_view.table_plan.doubleClicked.connect(self.on_double_click_table_plan)
        self.thread_get_plans = None
        self.thread_remove_plan = None
        self.plan_dtos = []
        self.start_thread_get_plans()

    # view handlers
    def on_click_btn_add_plan(self):
        add_plan = AddPlanView(self.main_view)
        add_plan.exec()
        if add_plan.saved_plan_dto:
            self.plan_dtos.append(add_plan.saved_plan_dto)
            self.insert_table_plan(add_plan.saved_plan_dto)

    def on_double_click_table_plan(self):
        row = self.main_view.table_plan.currentIndex().row()
        cod = int(self.main_view.table_plan.item(row, 0).text())
        plan_dto = next((dto for dto in self.plan_dtos if dto.id == cod), None)
        if not plan_dto:
            return
        edit_plan_view = AddPlanView(self.main_view, plan_dto)
        edit_plan_view.exec()
        if edit_plan_view.saved_plan_dto:
            updated = edit_plan_view.saved_plan_dto
            self.plan_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.plan_dtos
            ]
            self.insert_table_plan(updated)

    def on_click_btn_remove_plan(self):

        row_position = self.main_view.table_plan.currentRow()
        if row_position >= 0:
            plan_id = int(self.main_view.table_plan.item(row_position, 0).text())
            plan = next((plan for plan in self.plan_dtos if plan.id == plan_id), None)
            confirm_view = ConfirmView(parent=self.main_view, title="Apagar",
                                       text=f"Tem certeza que deseja apara o plano '{plan.name}'?")
            result = confirm_view.exec()
            if result == QMessageBox.Yes:
                self.start_thread_delete_plan(plan_id)

    def insert_table_plan(self, plan_dto: PlanDto):
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.main_view.table_plan.rowCount()):
                cod = int(self.main_view.table_plan.item(r, 0).text())
                if cod == plan_dto.id:
                    row_position = r
                    already_exists_on_table = True
                    break

            if row_position is None:
                row_position = self.main_view.table_plan.rowCount()
                self.main_view.table_plan.insertRow(row_position)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(plan_dto.id))
                item_id.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_plan.setItem(row_position, 0, item_id)

            # Name
            if not already_exists_on_table:
                item_name = QTableWidgetItem(plan_dto.name)
                item_name.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_plan.setItem(row_position, 1, item_name)
            else:
                item_name = QTableWidgetItem(plan_dto.name)
                self.main_view.table_plan.setItem(row_position, 1, item_name)

            # value
            value_str = "GRATUITO" if float(plan_dto.value) < 1 else f"R$ {str(plan_dto.value).replace(".", ",")}"
            if not already_exists_on_table:
                item_value = QTableWidgetItem(value_str)
                item_value.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_plan.setItem(row_position, 2, item_value)
            else:
                item_value = QTableWidgetItem(value_str)
                self.main_view.table_plan.setItem(row_position, 2, item_value)

            # details
            if not already_exists_on_table:
                item_observation = QTableWidgetItem(plan_dto.observation)
                item_observation.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_plan.setItem(row_position, 4, item_observation)
            else:
                item_observation = QTableWidgetItem(plan_dto.observation)
                self.main_view.table_plan.setItem(row_position, 4, item_observation)

            # students amount
            if not already_exists_on_table:
                item_students_amount = QTableWidgetItem(len(plan_dto.students))
                item_students_amount.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_plan.setItem(row_position, 3, item_students_amount)
            else:
                item_students_amount = QTableWidgetItem(len(plan_dto.students))
                self.main_view.table_plan.setItem(row_position, 3, item_students_amount)
        except Exception as e:
            return

    #thread
    def start_thread_get_plans(self):
        self.thread_get_plans = ThreadGetPlans()
        self.thread_get_plans.signals.signal_plan_dtos.connect(self.on_signal_plan_dtos)
        self.thread_get_plans.start()

    def start_thread_delete_plan(self, plan_id):
        self.thread_remove_plan = ThreadRemovePlan(plan_id)
        self.thread_remove_plan.signals.signal_finished.connect(self.on_signal_plan_deleted)
        self.thread_remove_plan.start()

    def on_signal_plan_deleted(self, deleted_plan_id):
        row_position = None
        cod = None
        for i in range(self.main_view.table_plan.rowCount()):
            cod = int(self.main_view.table_plan.item(i, 0).text())
            if cod == deleted_plan_id:
                row_position = i
                break
        if row_position is not None:
            self.main_view.table_plan.removeRow(row_position)
            plan = next((plan for plan in self.plan_dtos if plan.id == cod), None)
            self.plan_dtos.remove(plan)

    def on_signal_plan_dtos(self, plan_dtos):
        self.plan_dtos = plan_dtos
        for plan_dto in plan_dtos:
            self.insert_table_plan(plan_dto)

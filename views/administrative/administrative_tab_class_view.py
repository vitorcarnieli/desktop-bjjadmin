from PySide6.QtGui import Qt
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from threads.lesson_class.thread_get_classes import ThreadGetClasses
from threads.lesson_class.thread_remove_class import ThreadRemoveClass
from views.administrative.lesson_class.class_view import ClassView
from views.confirm_view import ConfirmView
from views.ui.converted.ui_main_view import Ui_MainWindow


class AdministrativeTabClassView:

    def __init__(self, main_view: Ui_MainWindow):
        self.main_view = main_view

        self.main_view.table_class.setColumnHidden(0, True)

        self.main_view.btn_add_class.clicked.connect(self.on_click_btn_add_class)
        self.main_view.btn_remove_class.clicked.connect(self.on_click_btn_remove_class)
        self.main_view.table_class.doubleClicked.connect(self.on_double_click_table_class)
        self.thread_get_classes = None
        self.thread_remove_class = None
        self.class_dtos = []
        self.start_thread_get_classes()

    # view handlers
    def on_click_btn_add_class(self):
        add_class_view = ClassView(self.main_view)
        add_class_view.exec()
        if add_class_view.saved_class_dto:
            self.class_dtos.append(add_class_view.saved_class_dto)
            self.insert_table_classes(add_class_view.saved_class_dto)

    def on_click_btn_remove_class(self):

        row_position = self.main_view.table_class.currentRow()
        if row_position >= 0:
            class_id = int(self.main_view.table_class.item(row_position, 0).text())
            lesson_class = next((c for c in self.class_dtos if c.id == class_id), None)
            confirm_view = ConfirmView(parent=self.main_view, title="Apagar",
                                       text=f"Tem certeza que deseja apara a turma '{lesson_class.name}'?")
            result = confirm_view.exec()
            if result == QMessageBox.Yes:
                self.start_thread_delete_class(class_id)

    def on_double_click_table_class(self):
        row = self.main_view.table_class.currentIndex().row()
        cod = int(self.main_view.table_class.item(row, 0).text())
        class_dto = next((dto for dto in self.class_dtos if dto.id == cod), None)
        if not class_dto:
            return
        edit_class_view = ClassView(self.main_view, class_dto)
        edit_class_view.exec()
        if edit_class_view.saved_class_dto:
            updated = edit_class_view.saved_class_dto
            self.class_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.class_dtos
            ]
            self.insert_table_classes(updated)

    def insert_table_classes(self, class_dto):
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.main_view.table_class.rowCount()):
                cod = int(self.main_view.table_class.item(r, 0).text())
                if cod == class_dto.id:
                    row_position = r
                    already_exists_on_table = True
                    break

            if row_position is None:
                row_position = self.main_view.table_class.rowCount()
                self.main_view.table_class.insertRow(row_position)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(class_dto.id))
                item_id.setTextAlignment(Qt.AlignCenter)
                self.main_view.table_class.setItem(row_position, 0, item_id)

            # Name
            if not already_exists_on_table:
                item_name = QTableWidgetItem(class_dto.name)
                self.main_view.table_class.setItem(row_position, 1, item_name)
            else:
                item_name = QTableWidgetItem(class_dto.name)
                self.main_view.table_class.setItem(row_position, 1, item_name)
            item_name.setTextAlignment(Qt.AlignCenter)

            # students amount
            if not already_exists_on_table:
                item_students_amount = QTableWidgetItem(len(class_dto.students))
                self.main_view.table_class.setItem(row_position, 2, item_students_amount)
            else:
                item_students_amount = QTableWidgetItem(len(class_dto.students))
                self.main_view.table_class.setItem(row_position, 2, item_students_amount)
            item_students_amount.setTextAlignment(Qt.AlignCenter)

            # details
            if not already_exists_on_table:
                item_observation = QTableWidgetItem(class_dto.observation)
                self.main_view.table_class.setItem(row_position, 3, item_observation)
            else:
                item_observation = QTableWidgetItem(class_dto.observation)
                self.main_view.table_class.setItem(row_position, 3, item_observation)
            item_observation.setTextAlignment(Qt.AlignCenter)


        except Exception as e:
            return

    #thread
    def start_thread_get_classes(self):
        self.thread_get_classes = ThreadGetClasses()
        self.thread_get_classes.signals.signal_class_dtos.connect(self.on_signal_class_dtos)
        self.thread_get_classes.start()

    def start_thread_delete_class(self, class_id):
        self.thread_remove_class = ThreadRemoveClass(class_id)
        self.thread_remove_class.signals.signal_finished.connect(self.on_signal_class_deleted)
        self.thread_remove_class.start()

    def on_signal_class_deleted(self, deleted_class_id):
        row_position = None
        cod = None
        for i in range(self.main_view.table_class.rowCount()):
            cod = int(self.main_view.table_class.item(i, 0).text())
            if cod == deleted_class_id:
                row_position = i
                break
        if row_position is not None:
            self.main_view.table_class.removeRow(row_position)
            c = next((c for c in self.class_dtos if c.id == cod), None)
            self.class_dtos.remove(c)

    def on_signal_class_dtos(self, class_dtos):
        class_dtos.pop(0)
        self.class_dtos = class_dtos
        for dto in class_dtos:
            self.insert_table_classes(dto)

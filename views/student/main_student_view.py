from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView

from dtos.student_dto import StudentDto
from enums.payment_status import PaymentStatus
from threads.student.thread_get_students import ThreadGetStudents
from threads.student.thread_load_student_filters import ThreadLoadStudentFilters
from threads.student.thread_remove_student import ThreadRemoveStudent
from views.checkable_combo_box import CheckableComboBox
from views.confirm_view import ConfirmView
from views.student.add_student_view import StudentView
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainStudentView:
    def __init__(self, main_view: Ui_MainWindow, main_payment_record_view):
        self.filters_on = None
        self.combo_student_filters:CheckableComboBox = None
        self.thread_load_student_filters = None
        self.thread_delete_student = None
        self.thread_get_students = None
        self.main_view = main_view
        self.selected_item = None
        self.main_payment_record_view = main_payment_record_view

        self.main_view.btn_add_student.clicked.connect(self.on_click_btn_add_student)
        self.main_view.btn_remove_student.clicked.connect(self.on_click_btn_remove_student)
        self.main_view.table_students.doubleClicked.connect(self.on_double_click_table_students)
        self.main_view.table_students.itemSelectionChanged.connect(self.on_selection_change_table_students)

        self.main_view.table_students.setColumnHidden(0, True)

        self.student_dtos = []
        self.to_display_student_dtos = []
        self.start_thread_get_students()

    # view handlers

    def on_click_btn_add_student(self):
        add_student_view = StudentView(parent=self.main_view)
        add_student_view.exec()
        student_dto = add_student_view.saved_student_dto
        if student_dto:
            self.student_dtos.append(student_dto)
            self.insert_table_students(student_dto)
            self.main_payment_record_view.reset()

    def on_click_btn_remove_student(self):
        confirm_view = ConfirmView(parent=self.main_view, title="Apagar",
                                       text=f"Tem certeza que deseja apara o aluno '{self.selected_item.name}'?")
        result = confirm_view.exec()
        if result == QMessageBox.Yes:
            self.start_thread_delete_student()

    def on_double_click_table_students(self):
        row = self.main_view.table_students.currentIndex().row()
        cod = int(self.main_view.table_students.item(row, 0).text())
        student_dto = next((dto for dto in self.student_dtos if dto.id == cod), None)
        if not student_dto:
            return
        edit_view = StudentView(self.main_view, student_dto)
        edit_view.exec()
        if edit_view.saved_student_dto:
            updated = edit_view.saved_student_dto
            self.student_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.student_dtos
            ]
            self.insert_table_students(updated)

    def on_selection_change_table_students(self):
        selected_items = self.main_view.table_students.selectedItems()
        if not selected_items:
            self.selected_item = None
            self.main_view.btn_remove_student.setEnabled(False)
            return

        row = selected_items[0].row()
        selected_item_id = self.main_view.table_students.item(row, 0).text()
        self.selected_item = next((r for r in self.student_dtos if r.id == int(selected_item_id)), None)
        self.main_view.btn_remove_student.setEnabled(True)


    def insert_table_students(self, student_dto: StudentDto):
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.main_view.table_students.rowCount()):
                cod = int(self.main_view.table_students.item(r, 0).text())
                if cod == student_dto.id:
                    row_position = r
                    already_exists_on_table = True
                    break
            if row_position is None:
                row_position = self.main_view.table_students.rowCount()
                self.main_view.table_students.insertRow(row_position)

            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(student_dto.id))
                set_qt_text_alignment_center(item_id)
                self.main_view.table_students.setItem(row_position, 0, item_id)

            # Name
            item_name = QTableWidgetItem(student_dto.name)
            self.main_view.table_students.setItem(row_position, 1, item_name)
            set_qt_text_alignment_center(item_name)

            # class
            item_students_amount = QTableWidgetItem(student_dto.lesson_class.name)
            self.main_view.table_students.setItem(row_position, 2, item_students_amount)
            set_qt_text_alignment_center(item_students_amount)

            # phone contact
            item_phone = QTableWidgetItem(student_dto.phone)
            self.main_view.table_students.setItem(row_position, 3, item_phone)
            set_qt_text_alignment_center(item_phone)

            # status
            payment_status_friendly = {
                "Open": "Aguardando Pagamento",
                "Paid": "Pagamento Confirmado",
                "Overdue": "Pagamento Atrasado",
                "Forgiven": "Pagamento Perdoado"
            }
            payment_status_style = {
                "Open": QColor("#F9A825"),
                "Paid": QColor("#2E7D32"),
                "Overdue": QColor("#C62828"),
                "Forgiven": QColor("#00838F")
            }
            status_value = student_dto.latest_payment_status.value
            item_payment_status = QTableWidgetItem(payment_status_friendly.get(status_value))
            item_payment_status.setForeground(payment_status_style.get(status_value))
            self.main_view.table_students.setItem(row_position, 4, item_payment_status)
            set_qt_text_alignment_center(item_payment_status)

            header = self.main_view.table_students.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
        except Exception as e:
            print(e)
            return

    # threads
    def start_thread_delete_student(self):
        self.thread_delete_student = ThreadRemoveStudent(self.selected_item.id)
        self.thread_delete_student.signals.signal_finished.connect(self.on_signal_delete_student_finished)
        self.thread_delete_student.start()

    def on_signal_delete_student_finished(self, id):
        row_position = None
        cod = None
        for i in range(self.main_view.table_students.rowCount()):
            cod = int(self.main_view.table_students.item(i, 0).text())
            if cod == id:
                row_position = i
                break
        if row_position is not None:
            self.main_view.table_students.removeRow(row_position)
            c = next((c for c in self.student_dtos if c.id == cod), None)
            self.student_dtos.remove(c)
            if self.to_display_student_dtos:
                self.to_display_student_dtos.remove(c)
            self.set_total_student_label()

    def start_thread_get_students(self):
        self.thread_get_students = ThreadGetStudents()
        self.thread_get_students.signals.signal_student_dtos.connect(self.on_signal_student_dtos)
        self.thread_get_students.start()

    def on_signal_student_dtos(self, student_dtos):
        self.student_dtos = student_dtos
        self.to_display_student_dtos = student_dtos
        for student in student_dtos:
            self.insert_table_students(student)
        self.start_thread_load_student_filters()

    # thread events
    def start_thread_load_student_filters(self):
        self.thread_load_student_filters = ThreadLoadStudentFilters()
        self.thread_load_student_filters.signals.signal_filters.connect(self.on_signal_filters)
        self.thread_load_student_filters.start()

    def on_student_filter_change(self):
        combo = self.combo_student_filters
        combo.blockSignals(True)
        for row in range(combo.model().rowCount()):
            item = combo.model().item(row)
            data = item.data(Qt.UserRole)
            if not data:
                continue
            combo.enable_by_index(row)

        indexes = combo.get_selected_indexes()

        filled_fields = [
            combo.model().item(row).data(Qt.UserRole)
            for row in indexes
            if combo.model().item(row).data(Qt.UserRole)
        ]

        for field in filled_fields:
            for row in range(combo.model().rowCount()):
                item = combo.model().item(row)

                if not (item.flags() & Qt.ItemIsUserCheckable):
                    continue

                data = item.data(Qt.UserRole)
                if not data:
                    continue

                if data.split("_")[0] == field.split("_")[0] and item.checkState() != Qt.Checked:
                    combo.disable_by_index(row)

        filters: dict[str, bool | int | None] = {
            "payment": None,
            "age": None,
            "class": None,
            "plan": None,
            "sex": None
        }

        def get_true_if_greater_zero(num: str) -> bool:
            return True if int(num.split("_")[-1]) > 0 else False

        filled_fields = [str(f) for f in filled_fields]

        for field in filled_fields:
            if "payment" in field:
                filters["payment"] = get_true_if_greater_zero(field)

            if "age" in field:
                filters["age"] = get_true_if_greater_zero(field)

            if "class" in field:
                filters["class"] = int(field.split("_")[-1])

            if "plan" in field:
                filters["plan"] = int(field.split("_")[-1])

            if "sex" in field:
                filters["sex"] = field.split("_")[-1]

        combo.blockSignals(False)
        self.apply_student_filters(filters)

    def on_signal_filters(self, filters):
        self.combo_student_filters = CheckableComboBox()
        self.combo_student_filters.currentTextChanged.connect(self.on_student_filter_change)
        self.combo_student_filters.setMinimumWidth(150)

        self.combo_student_filters.addTitle("Filtros")


        payment_id = "payment_"
        self.combo_student_filters.addTitle("Pagamento")
        self.combo_student_filters.addItem("Pagos", f"{payment_id}1")
        self.combo_student_filters.addItem("Pendentes", f"{payment_id}0")

        age_id = "age_"
        self.combo_student_filters.addTitle("Idade")
        self.combo_student_filters.addItem("+18", f"{age_id}1")
        self.combo_student_filters.addItem("-18", f"{age_id}0")

        sex_id = "sex_"
        self.combo_student_filters.addTitle("Sexo")
        self.combo_student_filters.addItem("Masculino", f"{sex_id}Male")
        self.combo_student_filters.addItem("Feminino", f"{sex_id}Female")

        class_id = "class_"
        self.combo_student_filters.addTitle("Turmas")
        for i,c in enumerate(filters["class"]):
            if i < 1:
                continue
            self.combo_student_filters.addItem(c.name, f"{class_id}{c.id}")

        plan_id = "plan_"
        self.combo_student_filters.addTitle("Planos")
        for i, p in enumerate(filters["plan"]):
            if i < 1:
                continue
            self.combo_student_filters.addItem(p.name, f"{plan_id}{p.id}")


        self.main_view.student_filter_layout.addWidget(self.combo_student_filters)

    def apply_student_filters(self, filters: dict[str, bool | int | None]):
        result = list(self.student_dtos)

        # payment
        payment_filter = filters.get("payment")
        if payment_filter is not None:
            payment_cause = {
                "payed": [PaymentStatus.PAID, PaymentStatus.FORGIVEN],
                "pending": [PaymentStatus.OPEN, PaymentStatus.OVERDUE]
            }
            # case paid
            if payment_filter:
                result = [
                    s for s in result
                    if s.latest_payment_status in payment_cause["payed"]
                ]
            else:
                result = [
                    s for s in result
                    if s.latest_payment_status in payment_cause["pending"]
                ]


        # age
        age_filter = filters.get("age")
        if age_filter is not None:
            def is_18_years_old(birth_date) -> bool:
                today = date.today()
                return (
                        today.year - birth_date.year
                        - ((today.month, today.day) < (birth_date.month, birth_date.day))
                ) >= 18

            result = [
                s for s in result
                if is_18_years_old(s.date_of_birth) == age_filter
            ]

        #sex
        sex_filter = filters.get("sex")
        if sex_filter is not None:
            result = [
                s for s in result
                if s.sex.value == sex_filter
            ]

        # class
        class_filter = filters.get("class")
        if class_filter is not None:
            result = [
                s for s in result
                if s.class_id == int(class_filter)
            ]

        # plan
        plan_filter = filters.get("plan")
        if plan_filter is not None:
            result = [
                s for s in result
                if s.plan_id == int(plan_filter)
            ]
        self.filters_on = True
        self.to_display_student_dtos = result
        self.set_total_student_label()
        self.main_view.table_students.setRowCount(0)
        for s in self.to_display_student_dtos:
            self.insert_table_students(s)


    def set_total_student_label(self):
        if self.to_display_student_dtos or self.filters_on:
            self.main_view.label_student_filter.setText(f"Total: {len(self.to_display_student_dtos)}")
        else:
            self.main_view.label_student_filter.setText(f"Total: {len(self.student_dtos)}")

    def reset(self):
        # limpa tabela
        self.main_view.table_students.setRowCount(0)
        self.main_view.table_students.clearSelection()

        # remove combo de filtros
        if self.combo_student_filters:
            self.combo_student_filters.setParent(None)
            self.combo_student_filters.deleteLater()
            self.combo_student_filters = None

        # estado interno
        self.selected_item = None
        self.student_dtos = []
        self.to_display_student_dtos = []

        # threads
        self.thread_load_student_filters = None
        self.thread_delete_student = None
        self.thread_get_students = None

        # labels
        self.main_view.label_student_filter.setText("Total: 0")
        self.main_view.btn_remove_student.setEnabled(False)

        # recarrega tudo
        self.start_thread_get_students()


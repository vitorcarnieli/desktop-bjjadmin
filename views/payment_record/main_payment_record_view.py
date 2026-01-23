import copy
from calendar import month
from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView

from dtos.payment_record_dto import PaymentRecordDto
from enums.payment_status import PaymentStatus
from threads.payment_records.thread_create_payment_records import ThreadLoadPaymentRecords
from threads.student.thread_load_student_filters import ThreadLoadStudentFilters
from views.checkable_combo_box import CheckableComboBox
from views.student.add_student_view import StudentView
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainPaymentRecordView:
    def __init__(self, main_view: Ui_MainWindow):
        self.records = None
        self.selected_item: PaymentRecordDto = None
        self.thread_load_payment_records = None
        self.thread_load_student_filters = None
        self.main_view = main_view
        self.to_day = date.today()
        self.combo_record_filters: CheckableComboBox = None

        self.main_view.btn_whatsapp.clicked.connect(self.on_click_btn_whatsapp)
        self.main_view.btn_money_on.clicked.connect(self.on_click_btn_money_on)
        self.main_view.btn_money_off.clicked.connect(self.on_click_btn_money_off)
        self.main_view.comboBox_year.currentIndexChanged.connect(self.on_index_change_comboBox_month)
        self.main_view.table_payment_records.itemSelectionChanged.connect(self.on_itemSelectionChanged_table_payment_records)


        self.assemble_ui()
        self.start_thread_load_payment_records()

    def on_itemSelectionChanged_table_payment_records(self):
        selected_items = self.main_view.table_payment_records.selectedItems()
        if not selected_items:
            self.selected_item_id = None
            self.main_view.btn_money_on.setEnabled(False)
            self.main_view.btn_money_off.setEnabled(False)
            self.main_view.btn_money_forgiven.setEnabled(False)
            return None

        row = selected_items[0].row()
        selected_item_id = self.main_view.table_payment_records.item(row, 0).text()
        self.selected_item = next((r for r in self.records if r.id == int(selected_item_id)), None)
        self.main_view.btn_money_forgiven.setEnabled(True)

        if self.selected_item.payment_status is PaymentStatus.PAID:
            self.main_view.btn_money_off.setEnabled(True)
            self.main_view.btn_money_forgiven.setEnabled(True)
        elif self.selected_item.payment_status is PaymentStatus.OPEN or self.selected_item.payment_status is PaymentStatus.OVERDUE:
            self.main_view.btn_money_on.setEnabled(True)
            self.main_view.btn_money_forgiven.setEnabled(True)
        elif self.selected_item.payment_status is PaymentStatus.FORGIVEN:
            self.main_view.btn_money_on.setEnabled(True)
            self.main_view.btn_money_off.setEnabled(True)

        return None


    def on_click_btn_whatsapp(self):
        pass

    def on_click_btn_money_on(self):
        pass

    def on_click_btn_money_off(self):
        pass

    def assemble_ui(self):
        # hidden id column
        self.main_view.table_payment_records.setColumnHidden(0, True)

        # assemble action btns
        self.main_view.btn_whatsapp.setIcon(QIcon("views/icons/whatsapp_unfill.png"))
        self.main_view.btn_money_on.setIcon(QIcon("views/icons/money.png"))
        self.main_view.btn_money_off.setIcon(QIcon("views/icons/un_money_money.png"))
        self.main_view.btn_money_forgiven.setIcon(QIcon("views/icons/money_forgiven.png"))
        self.main_view.btn_reload_records.setIcon(QIcon("views/icons/refresh_white.png"))
        self.main_view.btn_whatsapp.setEnabled(False)
        self.main_view.btn_money_on.setEnabled(False)
        self.main_view.btn_money_off.setEnabled(False)
        self.main_view.btn_reload_records.setEnabled(False)
        self.main_view.btn_money_forgiven.setEnabled(False)


        # assemble combo years
        for y in range(2024, int(self.to_day.year)+1):
            self.main_view.comboBox_year.addItem(str(y))
        self.main_view.comboBox_month.setCurrentIndex(self.to_day.month - 1)
        for i in range(self.main_view.comboBox_year.count()):
            if self.main_view.comboBox_year.itemText(i) == str(self.to_day.year):
                self.main_view.comboBox_year.setCurrentIndex(i)

        #self.start_thread_load_student_filters()





    # view handlers
    def on_index_change_comboBox_month(self, i):

        def toggle_enable_month(item, is_enabled):
            if item:
                item.setEnabled(is_enabled)

        combo_model = self.main_view.comboBox_month.model()

        year_selected_is_current_year = str(self.to_day.year) == self.main_view.comboBox_year.currentText()
        combo_month_range = range(self.main_view.comboBox_month.count())

        if year_selected_is_current_year:
            # disable months that haven't passed yet
            for i in combo_month_range:
                if not i in range(self.to_day.month):
                    toggle_enable_month(combo_model.item(i), False)
        else:
            for i in combo_month_range:
                toggle_enable_month(combo_model.item(i), True)



    def on_click_btn_add_student(self):
        add_student_view = StudentView(parent=self.main_view)
        add_student_view.exec()
        student_dto = add_student_view.saved_student_dto
        if student_dto:
            self.student_dtos.append(student_dto)
            self.insert_table_payment_records(student_dto)

    def on_click_btn_remove_student(self):
        pass

    def on_double_click_table_payment_records(self):
        pass

    def on_selection_change_table_payment_records(self):
        pass

    def insert_table_records(self, record: PaymentRecordDto):
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.main_view.table_payment_records.rowCount()):
                cod = int(self.main_view.table_payment_records.item(r, 0).text())
                if cod == record.id:
                    row_position = r
                    already_exists_on_table = True
                    break
            if row_position is None:
                row_position = self.main_view.table_payment_records.rowCount()
                self.main_view.table_payment_records.insertRow(row_position)

            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(record.id))
                set_qt_text_alignment_center(item_id)
                self.main_view.table_payment_records.setItem(row_position, 0, item_id)

            # Name
            item_student_name = QTableWidgetItem(record.student.name)
            self.main_view.table_payment_records.setItem(row_position, 1, item_student_name)
            set_qt_text_alignment_center(item_student_name)

            # class
            item_class = QTableWidgetItem(record.student.lesson_class.name)
            self.main_view.table_payment_records.setItem(row_position, 2, item_class)
            set_qt_text_alignment_center(item_class)

            # phone contact
            item_plan = QTableWidgetItem(record.student.plan.name)
            self.main_view.table_payment_records.setItem(row_position, 3, item_plan)
            set_qt_text_alignment_center(item_plan)

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

            item_payment_status = QTableWidgetItem(payment_status_friendly[record.payment_status.value])
            item_payment_status.setForeground(payment_status_style[record.payment_status.value])
            self.main_view.table_payment_records.setItem(row_position, 4, item_payment_status)
            set_qt_text_alignment_center(item_payment_status)
        except Exception as e:
            print(e)
            return

    # threads

    def start_thread_load_student_filters(self):
        self.thread_load_student_filters = ThreadLoadStudentFilters()
        self.thread_load_student_filters.signals.signal_filters.connect(self.on_signal_filters)
        self.thread_load_student_filters.start()

    def on_student_filter_change(self):
        combo = self.combo_record_filters
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
        self.combo_record_filters = CheckableComboBox()
        self.main_view.layout_filter_records.addWidget(self.combo_record_filters)
        self.combo_record_filters.currentTextChanged.connect(self.on_student_filter_change)
        self.combo_record_filters.setMinimumWidth(150)

        self.combo_record_filters.addTitle("Filtros")

        payment_id = "payment_"
        self.combo_record_filters.addTitle("Pagamento")
        self.combo_record_filters.addItem("Pagos", f"{payment_id}1")
        self.combo_record_filters.addItem("Pendentes", f"{payment_id}2")
        self.combo_record_filters.addItem("Perdoados", f"{payment_id}3")

        class_id = "class_"
        self.combo_record_filters.addTitle("Turmas")
        for i, c in enumerate(filters["class"]):
            if i < 1:
                continue
            self.combo_record_filters.addItem(c.name, f"{class_id}{c.id}")

        plan_id = "plan_"
        self.combo_record_filters.addTitle("Planos")
        for i, p in enumerate(filters["plan"]):
            if i < 1:
                continue
            self.combo_record_filters.addItem(p.name, f"{plan_id}{p.id}")


    def apply_student_filters(self, filters: dict[str, bool | int | None]):
        return
        result = copy.deepcopy(self.student_dtos)

        # payment
        """
        # TODO
        payment_filter = filters.get("payment")
        if payment_filter is not None:
            result = [
                s for s in result
                if s.is_paid == payment_filter
            ]
        """

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

        # sex
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

        self.to_display_student_dtos = result
        self.main_view.label_student_filter.setText(f"Total: {len(result)}")
        self.main_view.table_payment_records.setRowCount(0)
        for s in self.to_display_student_dtos:
            self.insert_table_payment_records(s)

    def start_thread_load_payment_records(self):
        self.thread_load_payment_records = ThreadLoadPaymentRecords(date.today())
        self.thread_load_payment_records.signals.signal_payment_record_dtos.connect(self.on_signal_records)
        self.thread_load_payment_records.start()

    def on_signal_records(self, records):
        self.main_view.table_payment_records.setRowCount(0)
        payed = 0.00
        pending = 0.00
        forgiven = 0.00
        self.records = records
        for record in records:
            self.insert_table_records(record)
            header = self.main_view.table_payment_records.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)

            if record.payment_status is PaymentStatus.PAID:
                payed += float(record.value)
            elif record.payment_status is PaymentStatus.OPEN or record.payment_status is PaymentStatus.OVERDUE:
                pending += float(record.value)
            elif record.payment_status is PaymentStatus.FORGIVEN:
                forgiven += float(record.value)

        def format_money(money: float):
            money_str_split = str(money).split(".")
            if len(money_str_split[-1]) < 2:
                money_str_split[-1] = f"{money_str_split[-1]}0"
            if len(money_str_split[0]) < 2:
                money_str_split[0] = f"0{money_str_split[0]}"
            return f"R$ {money_str_split[0]},{money_str_split[-1]}"

        self.main_view.label_total_payment_done.setText(f"Total recebido: {format_money(payed)}")
        self.main_view.label_total_payment_pedding.setText(f"Total pendente: {format_money(pending)}")
        self.main_view.label_3.setText(f"Total perdoado: {format_money(forgiven)}")

        self.start_thread_load_student_filters()

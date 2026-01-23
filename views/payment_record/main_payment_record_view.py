import copy
from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView

from dtos.payment_record_dto import PaymentRecordDto
from enums.payment_status import PaymentStatus
from threads.payment_records.thread_create_payment_records import ThreadLoadPaymentRecords
from threads.payment_records.thread_edit_payment_record_status import ThreadEditPaymentRecordStatus
from threads.student.thread_load_student_filters import ThreadLoadStudentFilters
from views.checkable_combo_box import CheckableComboBox
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainPaymentRecordView:
    def __init__(self, main_view: Ui_MainWindow):
        self.main_view = main_view


        self.forgiven_value = None
        self.pending_value = None
        self.payed_value = None

        self.thread_load_payment_records = None
        self.thread_load_student_filters = None
        self.thread_edit_payment_record_status = None

        self.records = None
        self.display_records = None
        self.selected_item: PaymentRecordDto = None
        self.to_day = date.today()


        # TODO: self.main_view.btn_whatsapp.clicked.connect()

        self.main_view.btn_money_on.clicked.connect(lambda: self.on_click_action_btns(PaymentStatus.PAID))
        self.main_view.btn_money_off.clicked.connect(lambda: self.on_click_action_btns(PaymentStatus.OPEN))
        self.main_view.btn_money_forgiven.clicked.connect(lambda: self.on_click_action_btns(PaymentStatus.FORGIVEN))

        self.main_view.comboBox_year.currentIndexChanged.connect(self.on_index_change_comboBox_month)
        self.main_view.table_payment_records.itemSelectionChanged.connect(self.on_itemSelectionChanged_table_payment_records)
        self.combo_record_filters: CheckableComboBox = None


        self.assemble_ui()
        self.start_thread_load_payment_records()


    # views events
    def on_itemSelectionChanged_table_payment_records(self):
        selected_items = self.main_view.table_payment_records.selectedItems()
        if not selected_items:
            self.selected_item = None
            self.main_view.btn_money_on.setEnabled(False)
            self.main_view.btn_money_off.setEnabled(False)
            self.main_view.btn_money_forgiven.setEnabled(False)
            return None

        row = selected_items[0].row()
        selected_item_id = self.main_view.table_payment_records.item(row, 0).text()
        self.selected_item = next((r for r in self.records if r.id == int(selected_item_id)), None)
        self.main_view.btn_money_forgiven.setEnabled(True)

        self.main_view.btn_money_on.setEnabled(False)
        self.main_view.btn_money_off.setEnabled(False)
        self.main_view.btn_money_forgiven.setEnabled(False)
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

    def on_click_action_btns(self, status):
        self.selected_item.payment_status = status
        self.start_thread_edit_payment_record_status()

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

        self.main_view.comboBox_month.setCurrentIndex(0)

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
            "class": None,
            "plan": None
        }

        filled_fields = [str(f) for f in filled_fields]

        for field in filled_fields:
            if "payment" in field:
                filters["payment"] = field.split("_")[-1]

            if "class" in field:
                filters["class"] = int(field.split("_")[-1])

            if "plan" in field:
                filters["plan"] = int(field.split("_")[-1])

        combo.blockSignals(False)
        self.apply_student_filters(filters)


    # threads
    def start_thread_edit_payment_record_status(self):
        self.thread_edit_payment_record_status = ThreadEditPaymentRecordStatus(self.selected_item)
        self.thread_edit_payment_record_status.signals.signal_updated_record_dto.connect(self.on_signal_updated_record_dto)
        self.thread_edit_payment_record_status.start()

    def on_signal_updated_record_dto(self, record):
        self.set_records([record])
        self.insert_table_records(record)

        self.main_view.table_payment_records.clearSelection()
        self.main_view.btn_money_on.setEnabled(False)
        self.main_view.btn_money_off.setEnabled(False)
        self.main_view.btn_money_forgiven.setEnabled(False)

        self.set_label_values()


    def start_thread_load_student_filters(self):
        self.thread_load_student_filters = ThreadLoadStudentFilters()
        self.thread_load_student_filters.signals.signal_filters.connect(self.on_signal_filters)
        self.thread_load_student_filters.start()

    def on_signal_filters(self, filters):
        self.combo_record_filters = CheckableComboBox()
        self.main_view.layout_filter_records.addWidget(self.combo_record_filters)
        self.combo_record_filters.currentTextChanged.connect(self.on_student_filter_change)
        self.combo_record_filters.setMinimumWidth(150)

        self.combo_record_filters.addTitle("Filtros")

        payment_id = "payment_"
        self.combo_record_filters.addTitle("Pagamento")
        self.combo_record_filters.addItem("Pagos", f"{payment_id}Paid")
        self.combo_record_filters.addItem("Pendentes", f"{payment_id}Open")
        self.combo_record_filters.addItem("Perdoados", f"{payment_id}Forgiven")

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


    def start_thread_load_payment_records(self):
        self.thread_load_payment_records = ThreadLoadPaymentRecords(date.today())
        self.thread_load_payment_records.signals.signal_payment_record_dtos.connect(self.on_signal_records)
        self.thread_load_payment_records.start()

    def on_signal_records(self, records):
        self.main_view.table_payment_records.setRowCount(0)

        self.set_records(records)
        for record in self.records:
            self.insert_table_records(record)

        self.set_label_values()

        self.start_thread_load_student_filters()


    # helpers
    def format_money(self, money: float):
        money_str_split = str(money).split(".")
        if len(money_str_split[-1]) < 2:
            money_str_split[-1] = f"{money_str_split[-1]}0"
        if len(money_str_split[0]) < 2:
            money_str_split[0] = f"0{money_str_split[0]}"
        return f"R$ {money_str_split[0]},{money_str_split[-1]}"

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

            # money
            item_money = QTableWidgetItem(f"{self.format_money(record.value)}")
            self.main_view.table_payment_records.setItem(row_position, 4, item_money)
            set_qt_text_alignment_center(item_money)

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
            self.main_view.table_payment_records.setItem(row_position, 5, item_payment_status)
            set_qt_text_alignment_center(item_payment_status)
            header = self.main_view.table_payment_records.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
        except Exception as e:
            return

    def apply_student_filters(self, filters: dict[str, bool | int | None]):
        if not any(filters.values()):
            self.display_records = None
            self.main_view.label_record_total_records.setText(f"Total: {len(self.records)}")
            self.set_label_values()
            self.main_view.table_payment_records.setRowCount(0)
            for s in self.records:
                self.insert_table_records(s)
            return

        result = copy.deepcopy(self.records)

        # payment
        payment_filter = filters.get("payment")
        if payment_filter is not None:
            result = [
                s for s in result
                if s.payment_status.value == payment_filter
            ]

        # class
        class_filter = filters.get("class")
        if class_filter is not None:
            result = [
                s for s in result
                if s.student.class_id == int(class_filter)
            ]

        # plan
        plan_filter = filters.get("plan")
        if plan_filter is not None:
            result = [
                s for s in result
                if s.student.plan_id == int(plan_filter)
            ]
        self.display_records = result
        self.main_view.label_record_total_records.setText(f"Total: {len(result)}")
        self.set_label_values()
        self.main_view.table_payment_records.setRowCount(0)
        for s in result:
            self.insert_table_records(s)

    def set_records(self, records):
        if not self.records:
            self.records = records
            return

        target = self.display_records if self.display_records else self.records

        for record in records:
            index_of_existing_record = next((i for i, r in enumerate(target) if r.id == record.id),None)
            if index_of_existing_record is not None:
                target[index_of_existing_record] = record

    def set_label_values(self):
        self.payed_value = 0.00
        self.pending_value = 0.00
        self.forgiven_value = 0.00
        if self.display_records:
            targets = self.display_records
        else:
            targets = self.records
        for record in targets:
            if record.payment_status == PaymentStatus.PAID:
                self.payed_value += float(record.value)
            elif record.payment_status == PaymentStatus.OPEN or record.payment_status == PaymentStatus.OVERDUE:
                self.pending_value += float(record.value)
            elif record.payment_status == PaymentStatus.FORGIVEN:
                self.forgiven_value += float(record.value)

        self.main_view.label_total_payment_done.setText(f"Total recebido: {self.format_money(self.payed_value)}")
        self.main_view.label_total_payment_pedding.setText(f"Total pendente: {self.format_money(self.pending_value)}")
        self.main_view.label_3.setText(f"Total perdoado: {self.format_money(self.forgiven_value)}")

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

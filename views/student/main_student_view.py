from datetime import date
from pathlib import Path

from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtGui import QColor, QPixmap, QPainter
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView, QWidget, QSizePolicy

from dtos.student_dto import StudentDto
from enums.payment_status import PaymentStatus
from services.file_service import FileService
from threads.student.thread_get_students import ThreadGetStudents
from threads.student.thread_load_student_filters import ThreadLoadStudentFilters
from threads.student.thread_remove_student import ThreadRemoveStudent
from views.checkable_combo_box import CheckableComboBox
from views.confirm_view import ConfirmView
from views.student.add_student_view import StudentView
from views.ui.converted.ui_main_view import Ui_MainWindow
from PySide6.QtGui import QPainterPath
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel


class MainStudentView:
    def __init__(self, main_view: Ui_MainWindow):
        self._active = True
        self.thread_load_student_filters_running = False
        self.thread_get_students_running = False
        self.filters_on = None
        self.combo_student_filters:CheckableComboBox = None
        self.thread_load_student_filters = None
        self.thread_delete_student = None
        self.thread_get_students = None
        self.main_view = main_view
        self._clear_layout(self.main_view.student_filter_layout)
        self.selected_item = None
        self.main_view.table_students.hide()
        self.SELECTED_STYLE = "background-color: #555555; border-radius: 6px;"
        self.UNSELECTED_STYLE = "background-color: #2f2f2f; border-radius: 6px;"
        self.main_view.btn_student_view_card.setStyleSheet(self.SELECTED_STYLE)
        self.main_view.btn_student_view_table.setStyleSheet(self.UNSELECTED_STYLE)
        self._selected_card = None

        self.main_view.btn_add_student.clicked.connect(self.on_click_btn_add_student)
        self.main_view.btn_remove_student.clicked.connect(self.on_click_btn_remove_student)
        self.main_view.table_students.doubleClicked.connect(self.on_double_click_table_students)
        self.main_view.table_students.itemSelectionChanged.connect(self.on_selection_change_table_students)
        self.main_view.btn_student_view_card.clicked.connect(
            lambda: self.on_change_student_view(True)
        )
        self.main_view.btn_student_view_table.clicked.connect(
            lambda: self.on_change_student_view(False)
        )

        self.main_view.table_students.setColumnHidden(0, True)

        self.student_dtos = []
        self.to_display_student_dtos = []
        self.start_thread_get_students()

    # view handlers

    def on_change_student_view(self, is_card):
        if is_card:
            self.main_view.table_students.hide()
            self.main_view.cards_scroll_area.show()
            self.main_view.btn_student_view_card.setStyleSheet(self.SELECTED_STYLE)
            self.main_view.btn_student_view_table.setStyleSheet(self.UNSELECTED_STYLE)
        else:
            self.main_view.table_students.show()
            self.main_view.cards_scroll_area.hide()
            self.main_view.btn_student_view_card.setStyleSheet(self.UNSELECTED_STYLE)
            self.main_view.btn_student_view_table.setStyleSheet(self.SELECTED_STYLE)


    def on_click_btn_add_student(self):
        add_student_view = StudentView(parent=self.main_view)
        add_student_view.exec()
        student_dto = add_student_view.saved_student_dto
        if student_dto:
            if add_student_view.profile_photo_changed:
                photo_path = Path(add_student_view.profile_photo_changed)
                new_name = f"{student_dto.id}{photo_path.suffix}"
                rename = str(photo_path.parent / new_name)
                FileService.force_rename_file(add_student_view.profile_photo_changed, rename)

            self.student_dtos.append(student_dto)
            self.insert_table_students(student_dto)

            if self.combo_student_filters:
                self.combo_student_filters.setParent(None)
                self.combo_student_filters.deleteLater()
                self.combo_student_filters = None
            self.reset()

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
            if edit_view.profile_photo_changed:
                photo_path = Path(edit_view.profile_photo_changed)
                new_name = f"{student_dto.id}{photo_path.suffix}"
                rename = str(photo_path.parent / new_name)
                FileService.force_rename_file(edit_view.profile_photo_changed, rename)

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
                "Forgiven": "Pagamento Perdoado",
                "Inactive": "Inativo",
                "":""
            }
            payment_status_style = {
                "Open": QColor("#F9A825"),
                "Paid": QColor("#2E7D32"),
                "Overdue": QColor("#C62828"),
                "Forgiven": QColor("#00838F"),
                "Inactive": QColor("#000"),
                "": QColor("#000")
            }
            status_value = "Inactive" if student_dto.is_inactive else "" if not student_dto.latest_payment_status else student_dto.latest_payment_status.value
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
            self.create_cards(self.to_display_student_dtos)

    def start_thread_get_students(self):
        self.thread_get_students_running = True
        self.thread_get_students = ThreadGetStudents()
        self.thread_get_students.signals.signal_student_dtos.connect(self.on_signal_student_dtos)
        self.thread_get_students.start()

    def on_signal_student_dtos(self, student_dtos):
        self.thread_get_students_running = False
        self.student_dtos = student_dtos
        self.to_display_student_dtos = student_dtos
        for student in student_dtos:
            self.insert_table_students(student)
        self.create_cards(student_dtos)
        if not self.thread_load_student_filters_running:
            self.start_thread_load_student_filters()


    # thread events
    def start_thread_load_student_filters(self):
        self.thread_load_student_filters_running = True
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
            "sex": None,
            "inactive": None
        }

        def get_true_if_greater_zero(num: str) -> bool:
            return True if int(num.split("_")[-1]) > 0 else False

        filled_fields = [str(f) for f in filled_fields]

        for field in filled_fields:
            if "inactive" in field:
                filters["inactive"] = get_true_if_greater_zero(field)

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

        payment_id = "inactive_"
        self.combo_student_filters.addTitle("Inativo")
        self.combo_student_filters.addItem("Inativos", f"{payment_id}1")

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
        self.thread_load_student_filters_running = False

    def apply_student_filters(self, filters: dict[str, bool | int | None]):
        result = list(self.student_dtos)

        # inactive
        inactive_filter = filters.get("inactive")
        if inactive_filter is not None:
            result = [
                s for s in result
                if s.is_inactive
            ]
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

        self.create_cards(self.to_display_student_dtos)

    def set_total_student_label(self):
        if not self._active:
            return
        try:
            if self.to_display_student_dtos or self.filters_on:
                self.main_view.label_student_filter.setText(f"Total: {len(self.to_display_student_dtos)}")
            else:
                self.main_view.label_student_filter.setText(f"Total: {len(self.student_dtos)}")
        except RuntimeError:
            pass

    def reset(self):
        try:
            self._active = False

            if self.combo_student_filters:
                self.combo_student_filters.blockSignals(True)
                self.combo_student_filters.setParent(None)
                self.combo_student_filters.deleteLater()
                self.combo_student_filters = None
                self.main_view.student_filter_layout.removeWidget(self.combo_student_filters)

            self.main_view.reset_all()
        except Exception as e:
            print(e)

    def _clear_layout(self, layout):
        if not layout:
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                try:
                    widget.blockSignals(True)
                except RuntimeError:
                    pass
                widget.setParent(None)
                widget.deleteLater()

            child_layout = item.layout()
            if child_layout is not None:
                self._clear_layout(child_layout)

    def create_cards(self, student_dtos):
        while self.main_view.cards_container.layout() is not None:
            old_layout = self.main_view.cards_container.layout()
            while old_layout.count():
                item = old_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            QWidget().setLayout(old_layout)

        main_layout = QVBoxLayout(self.main_view.cards_container)
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setAlignment(Qt.AlignTop)

        CARDS_PER_ROW = 6

        for i in range(0, len(student_dtos), CARDS_PER_ROW):
            row_widget = QWidget()
            row_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

            row_layout = QHBoxLayout(row_widget)
            row_layout.setSpacing(12)
            row_layout.setContentsMargins(0, 0, 0, 0)

            chunk = student_dtos[i:i + CARDS_PER_ROW]
            for student_dto in chunk:
                card = self._build_student_card(student_dto)
                row_layout.addWidget(card)

            for _ in range(CARDS_PER_ROW - len(chunk)):
                spacer = QWidget()
                spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                row_layout.addWidget(spacer)

            main_layout.addWidget(row_widget)
        self._selected_card = None
        self.selected_item = None
        self.main_view.btn_remove_student.setEnabled(False)




    def _get_belt_file(self, belt) -> str:
        BELT_DEGREE_MAP = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
        }

        BELT_COLOR_FILE_MAP = {
            "WHITE": "white",
            "GREY": "gray",
            "YELLOW": "yellow",
            "ORANGE": "orange",
            "GREEN": "green",
            "BLUE": "blue",
            "PURPLE": "purple",
            "BROWN": "brown",
            "BLACK": "black",
        }
        belt_name = str(belt).split(".")[-1]
        parts = belt_name.split("_")
        degree = BELT_DEGREE_MAP.get(parts[-1])
        color_parts = parts[:-1] if degree else parts
        base_color = next(
            (BELT_COLOR_FILE_MAP[p] for p in reversed(color_parts) if p in BELT_COLOR_FILE_MAP),
            "white"
        )
        return f"{base_color}{degree}" if degree else base_color


    def _open_edit_card(self, student_dto: StudentDto):
        edit_view = StudentView(self.main_view, student_dto)
        edit_view.exec()
        if edit_view.saved_student_dto:
            if edit_view.profile_photo_changed:
                photo_path = Path(edit_view.profile_photo_changed)
                new_name = f"{student_dto.id}{photo_path.suffix}"
                rename = str(photo_path.parent / new_name)
                FileService.force_rename_file(edit_view.profile_photo_changed, rename)

            updated = edit_view.saved_student_dto
            self.student_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.student_dtos
            ]
            self.to_display_student_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.to_display_student_dtos
            ]
            self.insert_table_students(updated)
            self.create_cards(self.to_display_student_dtos)

    def _build_student_card(self, student_dto: StudentDto) -> QWidget:
        PHOTO_H = 310
        BELT_SIZE = 62
        BELT_ICON = 54
        STATUS_SIZE = 22
        STATUS_ICON = 34

        PAYMENT_STATUS_MAP = {
            "Open":     ("views/icons/un_money_money.png", "#F9A825"),
            "Paid":     ("views/icons/money.png",          "#2E7D32"),
            "Overdue":  ("views/icons/un_money_money.png", "#C62828"),
            "Forgiven": ("views/icons/money_forgiven.png", "#00838F"),
        }

        card = QWidget()
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        card.setMinimumWidth(120)
        card.setObjectName("card")
        card.setCursor(Qt.CursorShape.PointingHandCursor)
        card.setProperty("selected", False)

        def apply_card_style(selected: bool):
            if selected:
                card.setStyleSheet("""
                    QWidget#card {
                        background-color: #3d5a80;
                        border-radius: 14px;
                        border: 2px solid #6fa3d8;
                    }
                """)
            else:
                card.setStyleSheet("""
                    QWidget#card {
                        background-color: #2b2b2b;
                        border-radius: 14px;
                        border: 2px solid transparent;
                    }
                """)

        apply_card_style(False)

        class _CardClickFilter(QObject):
            def __init__(self_, parent, dto):
                super().__init__(parent)
                self_.dto = dto

            def eventFilter(self_, obj, event):
                if event.type() == QEvent.Type.MouseButtonPress:
                    if event.button() == Qt.MouseButton.LeftButton:
                        # deseleciona o card anteriormente selecionado
                        if self._selected_card and self._selected_card is not card:
                            self._selected_card.setProperty("selected", False)
                            apply_prev = self._selected_card.property("apply_style")
                            if apply_prev:
                                apply_prev(False)

                        is_selected = card.property("selected")
                        new_state = not is_selected
                        card.setProperty("selected", new_state)
                        apply_card_style(new_state)

                        if new_state:
                            self._selected_card = card
                            self.selected_item = self_.dto
                            self.main_view.btn_remove_student.setEnabled(True)
                        else:
                            self._selected_card = None
                            self.selected_item = None
                            self.main_view.btn_remove_student.setEnabled(False)
                        return False

                if event.type() == QEvent.Type.MouseButtonDblClick:
                    self._open_edit_card(self_.dto)
                    return True

                return False

        # guarda referência da função de estilo no card para poder desfazer de fora
        card.setProperty("apply_style", apply_card_style)

        _click_filter = _CardClickFilter(card, student_dto)
        card.installEventFilter(_click_filter)
        card._click_filter = _click_filter

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(7, 7, 7, 7)
        card_layout.setSpacing(0)

        photo_container = QWidget()
        photo_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        photo_container.setFixedHeight(PHOTO_H)
        photo_container.setStyleSheet("border-radius: 10px; background-color: #3a3a3a;")

        photo_label = QLabel(photo_container)
        photo_label.setAlignment(Qt.AlignCenter)
        photo_label.setStyleSheet("border-radius: 10px;")

        def update_photo_label_size(event=None):
            w = photo_container.width()
            h = photo_container.height()
            photo_label.setGeometry(0, 0, w, h)

            raw = None
            for ext in ("png", "jpg", "jpeg", "webp"):
                candidate = f"profile_photos/student/{student_dto.id}.{ext}"
                p = QPixmap(candidate)
                if not p.isNull():
                    raw = p
                    break
            if raw is None:
                raw = QPixmap("views/icons/user_without_photo.png")

            scaled = raw.scaled(w, h,
                                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                Qt.TransformationMode.SmoothTransformation)
            x_off = (scaled.width() - w) // 2
            y_off = (scaled.height() - h) // 2
            cropped = scaled.copy(x_off, y_off, w, h)

            rounded = QPixmap(cropped.size())
            rounded.fill(Qt.GlobalColor.transparent)
            painter = QPainter(rounded)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            path = QPainterPath()
            path.addRoundedRect(0, 0, w, h, 10, 10)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, cropped)
            painter.end()
            photo_label.setPixmap(rounded)

            status_label.move(w - STATUS_SIZE - 6, 6)

        class _ResizeFilter(QObject):
            def eventFilter(_, obj, event):
                if event.type() == QEvent.Type.Resize:
                    update_photo_label_size()
                return False

        _filter = _ResizeFilter(photo_container)
        photo_container.installEventFilter(_filter)
        photo_container._resize_filter = _filter

        belt_label = QLabel(photo_container)
        belt_label.setFixedSize(BELT_SIZE, BELT_SIZE)
        belt_label.move(6, 6)
        belt_label.setStyleSheet(f"border-radius: {BELT_SIZE // 2}px; background-color: #1a1a1a; padding: 3px;")
        belt_label.setAlignment(Qt.AlignCenter)

        belt_file = self._get_belt_file(student_dto.belt)
        belt_pixmap = QPixmap(f"views/icons/belts/{belt_file}.png")
        if not belt_pixmap.isNull():
            belt_label.setPixmap(belt_pixmap.scaled(
                BELT_ICON, BELT_ICON,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        belt_label.raise_()

        status_label = QLabel(photo_container)
        status_label.setFixedSize(STATUS_SIZE, STATUS_SIZE)
        status_label.move(0, 6)
        status_label.setAlignment(Qt.AlignCenter)

        if student_dto.is_inactive:
            status_label.hide()
        else:
            status_value = student_dto.latest_payment_status.value if student_dto.latest_payment_status else None
            if status_value and status_value in PAYMENT_STATUS_MAP:
                icon_path, bg_color = PAYMENT_STATUS_MAP[status_value]
                status_label.setStyleSheet(
                    f"border-radius: {STATUS_SIZE // 2}px; "
                    f"background-color: {bg_color}; "
                    f"padding: 3px;"
                )
                status_pixmap = QPixmap(icon_path)
                if not status_pixmap.isNull():
                    status_label.setPixmap(status_pixmap.scaled(
                        STATUS_SIZE - 8, STATUS_SIZE - 8,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    ))
                status_label.show()
            else:
                status_label.hide()

        status_label.raise_()

        card_layout.addWidget(photo_container)
        card_layout.addSpacing(5)

        info_widget = QWidget()
        info_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        info_widget.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-radius: 8px;
            }
        """)
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(6, 5, 6, 5)
        info_layout.setSpacing(2)

        name_label = QLabel(student_dto.name.split()[0] if student_dto.name else "—")
        name_label.setStyleSheet("color: #ffffff; font-size: 13px; font-weight: bold; background: transparent;")
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setWordWrap(True)

        class_label = QLabel(student_dto.lesson_class.name if student_dto.lesson_class else "")
        class_label.setStyleSheet("color: #aaaaaa; font-size: 10px; background: transparent;")
        class_label.setAlignment(Qt.AlignCenter)

        info_layout.addWidget(name_label)
        info_layout.addWidget(class_label)

        card_layout.addWidget(info_widget)

        return card
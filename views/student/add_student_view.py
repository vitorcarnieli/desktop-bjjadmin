import re

from PySide6.QtCore import QDate
from PySide6.QtGui import QPixmap, QIcon, QPainter, QColor
from PySide6.QtCore import Qt, QSize, QObject, QEvent
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QDialog, QFileDialog, QHeaderView, QTableWidgetItem

from dtos.class_dto import ClassDto
from dtos.message import Message
from dtos.student_dto import StudentDto
from enums.belts import Belt
from enums.message_type import MessageType
from enums.sex import Sex
from services.file_service import FileService
from threads.lesson_class.thread_get_classes import ThreadGetClasses
from threads.plan.thread_get_plans import ThreadGetPlans
from threads.student.thread_edit_student import ThreadEditStudent
from threads.student.thread_save_student import ThreadAddStudent
from views.styles.label_style import LabelStyle
from views.ui.converted.student.ui_add_student_view import Ui_AddStudentView


class StudentView(QDialog, Ui_AddStudentView):

    def __init__(self, parent, to_edit_student: StudentDto = None):
        super(StudentView, self).__init__(parent)
        self.profile_photo_path = "views/icons/user_without_photo.png"
        self.thread_edit_student = None
        self.setupUi(self)
        self.setEnabled(False)

        self.save_btn.clicked.connect(self.on_click_save_btn)
        self.line_phone.textChanged.connect(self.on_text_changed_line_phone)
        self.label_user_photo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_user_photo.installEventFilter(self)

        self.saved_student_dto = None
        self.to_edit_student = to_edit_student

        self.plan_dtos = []
        self.class_dtos = []
        self.belts = []

        self.profile_photo_changed = None

        self.thread_get_plans = None
        self.thread_get_classes = None
        self.thread_add_student = None

        self.assemble_user_photo()
        self.populate_combo_belts(True)
        self.start_thread_get_plans()
        self.table_frequency.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.assemble_table_frequency(self.to_edit_student)
        if not self.to_edit_student:
            self.inactive_student_check.hide()
        else:
            self.inactive_student_check.show()

    def assemble_table_frequency(self,dto):
        try:
            if not dto:
                self.table_frequency.hide()
                return
            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            frequency = dto.frequency
            if frequency:
                for row, (key, value) in enumerate(frequency.items()):
                    self.table_frequency.setItem(row, 0, QTableWidgetItem(str(key)))
                    item = QTableWidgetItem(str(value))
                    self.table_frequency.setItem(row, 1, item)
                    set_qt_text_alignment_center(item)

                header = self.table_frequency.horizontalHeader()
                header.setSectionResizeMode(0, QHeaderView.Stretch)
        except Exception as e:
            print(e)
            return



    # views events
    def on_click_save_btn(self):
        student_dto = self.get_form_data()
        if not student_dto:
            return

        if self.to_edit_student:
            student_dto.id = self.to_edit_student.id
            self.start_thread_edit_student(student_dto)
        else:
            self.start_thread_add_student(student_dto)

    def on_selection_change_radio_belts(self):
        # TODO
        return

    def on_click_label_perfil_photo(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Imagem",
            FileService.get_pictures_path(),
            "Imagens (*.png *.jpg *.jpeg *.webp *.heic *.heif)",
            options=options
        )

        if file:
            self.set_profile_photo(file)
            path = "profile_photos/student"
            FileService.create_folder(path)
            FileService.copy_file(file, path)
            self.profile_photo_changed = f"{path}/{file.split("/")[-1]}"


    # ThreadGetClasses
    def start_thread_get_classes(self):
        self.thread_get_classes = ThreadGetClasses()
        self.thread_get_classes.signals.signal_class_dtos.connect(self.on_signal_class_dtos)
        self.thread_get_classes.start()

    def on_signal_class_dtos(self, class_dtos):
        if len(class_dtos) < 2:
            self.update_status(Message(MessageType.ERROR, "Cadastre turmas antes de cadastrar alunos"))
            return
        class_dtos.pop(0)

        self.combo_class.addItem("Selecione")
        self.class_dtos = class_dtos
        for class_dto in class_dtos:
            self.combo_class.addItem(class_dto.name)
        self.combo_class.setStyleSheet("""
        QComboBox{
	background:  rgb(255, 255, 255);
	border-radius: 10px;
	padding: 5px;
}

QComboBox QAbstractItemView {
background:  rgb(255, 255, 255);
}

        """)
        if self.to_edit_student:
            self.set_form_data()
        self.setEnabled(True)


    # ThreadGetPlans
    def start_thread_get_plans(self):
        self.thread_get_plans = ThreadGetPlans()
        self.thread_get_plans.signals.signal_plan_dtos.connect(self.on_signal_plan_dtos)
        self.thread_get_plans.start()

    def on_signal_plan_dtos(self, plan_dtos):
        if len(plan_dtos) < 2:
            self.update_status(Message(MessageType.ERROR, "Cadastre planos antes de cadastrar alunos"))
            return
        plan_dtos.pop(0)

        self.combo_plan.addItem("Selecione")
        self.plan_dtos = plan_dtos
        for plan_dto in plan_dtos:
            plan_str = f"{plan_dto.name} - R$ {plan_dto.value.replace(".", ",")}"
            self.combo_plan.addItem(plan_str)

        self.combo_plan.setStyleSheet("""
        QComboBox{
	background:  rgb(255, 255, 255);
	border-radius: 10px;
	padding: 5px;
}

QComboBox QAbstractItemView {
background:  rgb(255, 255, 255);
}

        """)
        self.start_thread_get_classes()


    # ThreadSaveStudent
    def start_thread_add_student(self, student_dto):
        self.thread_add_student = ThreadAddStudent(student_dto)
        self.thread_add_student.signals.signal_message.connect(self.update_status)
        self.thread_add_student.signals.signal_student_dto.connect(self.on_signal_student_dto)
        self.thread_add_student.start()

    def on_signal_student_dto(self, student_dto):
        if not student_dto:
            return
        self.saved_student_dto = student_dto
        self.accept()

    def start_thread_edit_student(self, student_dto):
        self.thread_edit_student = ThreadEditStudent(student_dto)
        self.thread_edit_student.signals.signal_student_dto.connect(self.on_signal_student_dto)
        self.thread_edit_student.start()
    
    
    # view handlers
    def eventFilter(self, obj, event):
        if obj is self.label_user_photo:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.on_click_label_perfil_photo()
                    return True  # evento tratado

        return super().eventFilter(obj, event)

    def set_form_data(self):
        # name
        self.line_name.setText(self.to_edit_student.name)

        # date
        py_date = self.to_edit_student.date_of_birth
        self.dateEdit.setDate(QDate(py_date.year, py_date.month, py_date.day))

        # sex
        if self.to_edit_student == Sex.MALE:
            self.radio_male.setChecked(True)
        else:
            self.radio_female.setChecked(False)

        # phone
        if self.to_edit_student.phone:
            self.line_phone.setText(self.to_edit_student.phone)

        # plan
        plan = next((p for p in self.plan_dtos if p.id == self.to_edit_student.plan_id), None)
        if plan:
            selected_plan_index = self.plan_dtos.index(plan)
            self.combo_plan.setCurrentIndex(selected_plan_index + 1)

        # class
        lesson_class = next((c for c in self.class_dtos if c.id == self.to_edit_student.class_id), None)
        if lesson_class:
            selected_class_index = self.class_dtos.index(lesson_class)
            self.combo_class.setCurrentIndex(selected_class_index + 1)

        # details
        self.textEdit_observation.setText(self.to_edit_student.observation)

        # belt
        belt = self.to_edit_student.belt.value
        index = self.combo_belts.findText(belt, Qt.MatchExactly)
        if index != -1:
            self.combo_belts.setCurrentIndex(index)

        if self.to_edit_student.is_inactive:
            self.inactive_student_check.setChecked(True)
        else:
            self.inactive_student_check.setChecked(False)

    def get_form_data(self):
        required_fields = {
            "Nome": self.line_name.text(),
            "Plano": self.combo_plan.currentIndex(),
            "Turma": self.combo_class.currentIndex(),
            "Faixa": self.combo_belts.currentIndex()
        }
        for k, v in required_fields.items():
            # implement the "SELECT" option to avoid generating an error if v == 0.
            if not v:
                self.update_status(Message(MessageType.ERROR, f'O campo "{k}" precisa ser preenchido'))
                return None

        student_dto = StudentDto()
        student_dto.name = required_fields["Nome"]
        student_dto.plan_id = self.plan_dtos[required_fields["Plano"] - 1].id
        student_dto.class_id = self.class_dtos[required_fields["Turma"] - 1].id
        student_dto.belt = Belt(self.combo_belts.currentText())
        student_dto.observation = self.textEdit_observation.toPlainText()
        student_dto.phone = self.line_phone.text()
        student_dto.date_of_birth = self.dateEdit.date().toPython()
        student_dto.sex = Sex.MALE if self.radio_male.isChecked() else Sex.FEMALE
        student_dto.is_inactive = self.inactive_student_check.isChecked()
        return student_dto

    def on_text_changed_line_phone(self, text):
        cursor_pos = self.line_phone.cursorPosition()

        digits_before_cursor = len(re.sub(r"\D", "", text[:cursor_pos]))

        formatted = self.format_phone(text)

        self.line_phone.blockSignals(True)
        self.line_phone.setText(formatted)
        self.line_phone.blockSignals(False)

        new_cursor_pos = self.cursor_position_from_digits(
            formatted, digits_before_cursor
        )
        self.line_phone.setCursorPosition(new_cursor_pos)

    def cursor_position_from_digits(self, formatted: str, digit_index: int) -> int:
        if digit_index == 0:
            return 0

        count = 0
        for i, char in enumerate(formatted):
            if char.isdigit():
                count += 1
                if count == digit_index:
                    return i + 1

        return len(formatted)

    def format_phone(self, text):
        digits = re.sub(r"\D", "", text)[:11]

        if len(digits) <= 2:
            return f"({digits}"
        elif len(digits) <= 7:
            return f"({digits[:2]}) {digits[2:]}"
        else:
            return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"


    def populate_combo_belts(self, is_adult: bool):

        def insert_option(file_name: str, translated_name: str):
            pixmap = None
            if file_name:
                pixmap = QPixmap(f"views/icons/belts/{file_name}.png")
                pixmap = pixmap.scaled(
                    69, 28,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            self.combo_belts.addItem(QIcon(pixmap), translated_name)

        self.combo_belts.setIconSize(QSize(69, 28))

        insert_option("", "SELECIONE")

        belts = [
            ("white", "Branca"),
            ("blue", "Azul"),
            ("purple", "Roxa"),
            ("brown", "Marrom"),
        ]

        for base_name, base_label in belts:
            insert_option(base_name, base_label)

            for i in range(1, 5):
                insert_option(
                    f"{base_name}{i}",
                    f"{base_label} {'I' * i if i != 4 else 'IV'}"
                )

        insert_option("black", "Preta")

        self.combo_belts.setStyleSheet("""
        QComboBox {
            background: #383838;
            color: white;
            border-radius: 10px;
            padding: 5px;
        }

        QComboBox QAbstractItemView {
            background: #383838;
            color: white;
            selection-background-color: #505050;
        }
        """)

    def assemble_user_photo(self):
        if self.to_edit_student:
            for file in FileService.list_file_names("profile_photos/student"):
                if file.split(".")[0] == str(self.to_edit_student.id):
                    self.profile_photo_path = f"profile_photos/student/{self.to_edit_student.id}.{file.split(".")[-1]}"
                    break
        self.set_profile_photo(self.profile_photo_path)

        class HoverFilter(QObject):
            def eventFilter(_, obj, event):
                if obj is self.label_user_photo:

                    if event.type() == QEvent.Type.Enter:
                        hovered = QPixmap(self._user_photo_pixmap)  # sempre atual
                        painter = QPainter(hovered)

                        painter.fillRect(
                            hovered.rect(),
                            QColor(255, 255, 255, 120)
                        )

                        svg = QSvgRenderer("views/icons/pencil-square.svg")
                        icon_size = 48

                        icon_pixmap = QPixmap(icon_size, icon_size)
                        icon_pixmap.fill(Qt.GlobalColor.transparent)

                        svg_painter = QPainter(icon_pixmap)
                        svg.render(svg_painter)
                        svg_painter.end()

                        x = (hovered.width() - icon_size) // 2
                        y = (hovered.height() - icon_size) // 2
                        painter.drawPixmap(x, y, icon_pixmap)

                        painter.end()
                        self.label_user_photo.setPixmap(hovered)

                    elif event.type() == QEvent.Type.Leave:
                        self.label_user_photo.setPixmap(self._user_photo_pixmap)

                return False

        self._user_photo_hover_filter = HoverFilter(self.label_user_photo)
        self.label_user_photo.installEventFilter(self._user_photo_hover_filter)

    def set_profile_photo(self, file_path):
        pixmap = QPixmap(file_path).scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self._user_photo_pixmap = pixmap  # ← fonte única da verdade

        label = self.label_user_photo
        label.setPixmap(pixmap)
        label.setMouseTracking(True)
        label.setCursor(Qt.CursorShape.PointingHandCursor)

    def update_status(self, message: Message):
        if message.type == MessageType.ERROR:
            self.label.setStyleSheet(LabelStyle.Error)
            self.label.setText(message.payload)
        elif message.type == MessageType.INFORMATION:
            self.label.setStyleSheet(LabelStyle.Info)
            self.label.setText(message.payload)
        elif message.type == MessageType.SUCCESS:
            self.label.setStyleSheet(LabelStyle.Success)
            self.label.setText(message.payload)

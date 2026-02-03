import uuid

from PySide6.QtCore import QObject, QEvent, Qt, QTime
from PySide6.QtGui import QPixmap, QPainter, QColor, QStandardItem
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QDialog, QFileDialog, QComboBox, QVBoxLayout, QStyledItemDelegate

from dtos.class_dto import ClassDto
from dtos.lesson_dto import LessonDto
from dtos.message import Message
from enums.message_type import MessageType
from services.file_service import FileService
from threads.lesson.thread_save_lesson import ThreadSaveLesson
from threads.lesson_class.thread_get_classes import ThreadGetClasses
from threads.student.thread_get_students import ThreadGetStudents
from views.checkable_combo_box import CheckableComboBox
from views.styles.label_style import LabelStyle
from views.ui.converted.lesson.ui_add_lesson import Ui_add_lesson


class AddLessonView(QDialog, Ui_add_lesson):

    def __init__(self, parent, date, to_edit_lesson_dto: LessonDto = None):
        super(AddLessonView, self).__init__(parent)
        self.to_edit_index_defined = None
        self.setupUi(self)


        self.btn_save.clicked.connect(self.on_click_btn_save)
        self.comboBox_class.currentIndexChanged.connect(self.on_index_change_comboBox_class)


        self.date = date

        self.combo_students: CheckableComboBox = None

        self.saved_lesson_dto = None
        self.to_edit_lesson_dto = to_edit_lesson_dto
        self.current_class_selected: ClassDto = None
        self.student_dtos = []
        self.class_dtos = []

        self.thread_get_students = None
        self.thread_get_classes = None
        self.thread_save_lesson = None

        self.profile_photo_changed = None
        self._user_photo_hover_filter = None
        self._user_photo_pixmap = None


        self.assemble_ui()
        # set_form_data flow starts in start_thread_get_classes()
        self.start_thread_get_classes()

    # ThreadGetClasses
    def start_thread_get_classes(self):
        self.thread_get_classes = ThreadGetClasses()
        self.thread_get_classes.signals.signal_class_dtos.connect(self.on_signal_class_dtos)
        self.update_status(Message(MessageType.INFORMATION, "Aguarde enquanto as turmas são carregas"))
        self.thread_get_classes.start()

    def on_signal_class_dtos(self, class_dtos):
        class_dtos.pop(0)
        self.class_dtos = class_dtos
        self.comboBox_class.addItem("Selecione")
        for dto in class_dtos:
            self.comboBox_class.addItem(dto.name)
        self.comboBox_class.setStyleSheet(
        """
        QComboBox {
        	background:  rgb(255, 255, 255);
        	border-radius: 10px;
        	padding: 5px;
        }

        QComboBox QAbstractItemView {
            background:  rgb(255, 255, 255);
        }
        """
        )
        model = self.comboBox_class.model()
        item = model.item(0)
        item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
        self.update_status(Message(MessageType.INFORMATION, ""))
        self.set_form_data()

    # ThreadGetStudents
    def start_thread_get_students(self):
        self.thread_get_students = ThreadGetStudents()
        self.thread_get_students.signals.signal_student_dtos.connect(self.on_signal_student_dtos)
        self.update_status(Message(MessageType.INFORMATION, "Aguarde enquanto os alunos são carregas"))
        self.thread_get_students.start()

    def on_signal_student_dtos(self, student_dtos):
        self.student_dtos = list(filter(lambda s: s.class_id == self.current_class_selected.id, student_dtos))
        self.combo_students.clear()
        for student in self.student_dtos:
            if student.class_id == self.current_class_selected.id:
                self.combo_students.addItem(student.name)

        # simulates the user's click, this prevents the name of the last item added to the combo from showing
        self.combo_students.showPopup()
        self.combo_students.hidePopup()

        self.update_status(Message(MessageType.INFORMATION, ""))
        self.combo_students.setEnabled(True)
        self.textEdit_details.setEnabled(True)
        self.set_form_data()

    # ThreadSaveLesson
    def start_thread_save_lesson(self, lesson_dto):
        self.thread_save_lesson = ThreadSaveLesson(lesson_dto)
        self.thread_save_lesson.signals.signal_message.connect(self.update_status)
        self.thread_save_lesson.signals.signal_lesson_dto.connect(self.on_signal_lesson_dto)
        self.setEnabled(False)
        self.thread_save_lesson.start()

    def on_signal_lesson_dto(self, lesson_dto):
        self.saved_lesson_dto = lesson_dto
        self.accept()

    # UI handlers
    def on_click_btn_save(self):
        lesson_dto = self.get_form_data()
        if lesson_dto:
            self.start_thread_save_lesson(lesson_dto)


    def on_index_change_comboBox_class(self):
        selected_index = self.comboBox_class.currentIndex()
        if selected_index < 1:
            self.current_class_selected = None
            return

        self.current_class_selected = self.class_dtos[selected_index - 1]
        self.start_thread_get_students()

    def get_form_data(self):
        student_indexes = self.combo_students.get_selected_indexes()
        if not student_indexes:
            self.update_status(Message(MessageType.ERROR,  "Registre a presença de algum aluno"))
            return None

        def get_period_from_time(time_edit):
            time = time_edit.time()
            hour = time.hour()

            if 5 <= hour < 12:
                return "Manhã"
            elif 12 <= hour < 18:
                return "Tarde"
            else:
                return "Noite"

        dto = LessonDto()
        dto.id = self.to_edit_lesson_dto.id if self.to_edit_lesson_dto else None
        time = f"{self.timeEdit_start.time().toString().split(":")[0]}:{self.timeEdit_start.time().toString().split(":")[1]}"
        dto.name = f"{get_period_from_time(self.timeEdit_start)} {time}"
        dto.observation = self.textEdit_details.toPlainText()
        dto.date = self.date
        dto.start_time = self.timeEdit_start.time().toPython()
        dto.end_time = self.timeEdit_end.time().toPython()
        dto.lesson_class_id = self.current_class_selected.id
        dto.students = [self.student_dtos[i] for i in student_indexes]

        return dto

    def set_form_data(self):
        if not self.to_edit_lesson_dto:
            return

        # first flow, defines the class to call the trigger that loads the students
        if not self.to_edit_index_defined:
            index = next((i for i, c in enumerate(self.class_dtos) if c.id == self.to_edit_lesson_dto.lesson_class_id), None)
            self.to_edit_index_defined = True
            self.comboBox_class.setCurrentIndex(index + 1)
            return

        # students
        student_ids = [s.id for s in self.to_edit_lesson_dto.students]
        student_indexes = [i for i, s in enumerate(self.student_dtos) if s.id in student_ids]
        self.combo_students.set_current_indexes(student_indexes)

        def python_time_to_qtime(py_time):
            return QTime(py_time.hour, py_time.minute)

        # start time
        self.timeEdit_start.setTime(
            python_time_to_qtime(self.to_edit_lesson_dto.start_time)
        )

        # end time
        self.timeEdit_end.setTime(
            python_time_to_qtime(self.to_edit_lesson_dto.end_time)
        )

        # details
        self.textEdit_details.setText(self.to_edit_lesson_dto.observation)

    # assemble ui
    def assemble_ui(self):
        self.combo_students = CheckableComboBox()
        self.verticalLayout_8.addWidget(self.combo_students)
        self.combo_students.setEnabled(False)
        self.textEdit_details.setEnabled(False)

        self.label_photo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_photo.installEventFilter(self)

        self.label_title_lesson.setText(f"Aula - {self._get_format_date(self.date.day)}/{self._get_format_date(self.date.month)}/{self.date.year}")

        self.assemble_class_photo()

    def assemble_class_photo(self):
        file_path = "views/icons/class.png"
        if self.to_edit_lesson_dto:
            for file in FileService.list_file_names("profile_photos/lesson"):
                if file.split(".")[0] == str(self.to_edit_lesson_dto.id):
                    file_path = f"profile_photos/lesson/{self.to_edit_lesson_dto.id}.{file.split(".")[-1]}"
                    break
        self.set_class_photo(file_path)

        class HoverFilter(QObject):
            def eventFilter(_, obj, event):
                if obj is self.label_photo:

                    if event.type() == QEvent.Type.Enter:
                        hovered = QPixmap(self._user_photo_pixmap)
                        painter = QPainter(hovered)

                        painter.fillRect(
                            hovered.rect(),
                            QColor(255, 255, 255, 120)
                        )

                        svg = QSvgRenderer("views/icons/pencil-square.svg")
                        icon_size = 48

                        icon_pixmap = QPixmap(48, 48)
                        icon_pixmap.fill(Qt.GlobalColor.transparent)

                        svg_painter = QPainter(icon_pixmap)
                        svg.render(svg_painter)
                        svg_painter.end()

                        x = (hovered.width() - icon_size) // 2
                        y = (hovered.height() - icon_size) // 2
                        painter.drawPixmap(x, y, icon_pixmap)

                        painter.end()
                        self.label_photo.setPixmap(hovered)

                    elif event.type() == QEvent.Type.Leave:
                        self.label_photo.setPixmap(self._user_photo_pixmap)

                return False

        self._user_photo_hover_filter = HoverFilter(self.label_photo)
        self.label_photo.installEventFilter(self._user_photo_hover_filter)

    def set_class_photo(self, file_path):
        pixmap = QPixmap(file_path).scaled(
            405, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self._user_photo_pixmap = pixmap

        label = self.label_photo
        label.setPixmap(pixmap)
        label.setMouseTracking(True)
        label.setCursor(Qt.CursorShape.PointingHandCursor)

    def _get_format_date(self, date):
        return date if date >= 10 else f"0{date}"

    def set_profile_photo(self, file_path):
        pixmap = QPixmap(file_path).scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self._user_photo_pixmap = pixmap

        label = self.label_photo
        label.setPixmap(pixmap)
        label.setMouseTracking(True)
        label.setCursor(Qt.CursorShape.PointingHandCursor)

    def eventFilter(self, obj, event):
        if obj is self.label_photo:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.on_click_label_perfil_photo()
                    return True

        return super().eventFilter(obj, event)

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
            path = "profile_photos/lesson"
            FileService.create_folder(path)
            FileService.copy_file(file, path)
            copied_file_path = f"{path}/{file.split("/")[-1]}"
            target_file_path = f"{path}/{uuid.uuid4()}.{file.split("/")[-1].split(".")[-1]}"
            FileService.rename_file(copied_file_path, target_file_path)
            self.profile_photo_changed = target_file_path



    def update_status(self, message: Message):
        if message.type == MessageType.ERROR:
            self.label_status.setStyleSheet(LabelStyle.Error)
            self.label_status.setText(message.payload)
        elif message.type == MessageType.INFORMATION:
            self.label_status.setStyleSheet(LabelStyle.Info)
            self.label_status.setText(message.payload)
        elif message.type == MessageType.SUCCESS:
            self.label_status.setStyleSheet(LabelStyle.Success)
            self.label_status.setText(message.payload)





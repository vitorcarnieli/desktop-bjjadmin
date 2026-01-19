from PySide6.QtWidgets import QDialog

from dtos.class_dto import ClassDto
from dtos.message import Message
from enums.message_type import MessageType
from threads.lesson_class.thread_add_class import ThreadAddClass
from threads.lesson_class.thread_edit_class import ThreadEditClass
from views.styles.label_style import LabelStyle
from views.ui.converted.administrative.ui_add_class import Ui_AddClass


class ClassView(QDialog, Ui_AddClass):

    def __init__(self, parent, class_to_edit_dto=None):
        super(ClassView, self).__init__(parent)
        self.setupUi(self)

        self.btn_save.clicked.connect(self.on_click_btn_save)

        self.saved_class_dto = None
        self.thread_add_class = None
        self.thread_edit_class = None

        self.class_to_edit_dto = class_to_edit_dto
        self.set_form_data()



    def on_click_btn_save(self):
        class_dto = self.get_class_dto()
        if not class_dto:
            return

        if self.class_to_edit_dto:
            self.start_thread_edit_class(class_dto)
            return
        self.start_thread_add_class(class_dto)

    def start_thread_add_class(self, dto):
        self.thread_add_class = ThreadAddClass(dto)
        self.thread_add_class.signals.signal_message.connect(self.update_status)
        self.thread_add_class.signals.signal_class_dto.connect(self.on_signal_class_dto)
        self.thread_add_class.start()

    def start_thread_edit_class(self, dto):
        self.thread_edit_class = ThreadEditClass(dto)
        self.thread_edit_class.signals.signal_class_dto.connect(self.on_signal_class_dto)
        self.thread_edit_class.start()

    def set_form_data(self):
        if not self.class_to_edit_dto:
            return
        self.lineEdit_name.setText(self.class_to_edit_dto.name)
        self.textEdit_details.setText(self.class_to_edit_dto.observation)

    def get_class_dto(self):
        name = self.lineEdit_name.text()
        if not name:
            self.update_status(Message(MessageType.ERROR, "O plano não pode ser cadastrado sem nome"))
            return None

        observation = self.textEdit_details.toPlainText()

        class_dto = ClassDto()
        class_dto.name = name
        class_dto.observation = observation
        if self.class_to_edit_dto:
            class_dto.id = self.class_to_edit_dto.id
        return class_dto

    def on_signal_class_dto(self, class_dto):
        self.saved_class_dto = class_dto
        self.accept()

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

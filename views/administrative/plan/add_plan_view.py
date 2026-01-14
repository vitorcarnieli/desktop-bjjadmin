from PySide6.QtWidgets import QDialog

from dtos.message import Message
from dtos.plan_dto import PlanDto
from enums.message_type import MessageType
from threads.plan.thread_edit_plan import ThreadEditPlan
from threads.plan.thread_save_plan import ThreadAddPlan
from views.styles.label_style import LabelStyle
from views.ui.converted.administrative.ui_add_plan import Ui_AddPlan


class AddPlanView(QDialog, Ui_AddPlan):

    def __init__(self, parent, plan_to_edit_dto=None):
        super(AddPlanView, self).__init__(parent)
        self.setupUi(self)

        self.btn_save.clicked.connect(self.on_click_btn_save)

        self.saved_plan_dto = None
        self.thread_add_plan = None
        self.thread_edit_plan = None

        self.plan_to_edit_dto = plan_to_edit_dto
        self.set_form_data()



    def on_click_btn_save(self):
        plan_dto = self.get_plan_dto()
        if not plan_dto:
            return

        if self.plan_to_edit_dto:
            self.start_thread_edit_plan(plan_dto)
            return
        self.start_thread_add_plan(plan_dto)

    def start_thread_add_plan(self, dto):
        self.thread_add_plan = ThreadAddPlan(dto)
        self.thread_add_plan.signals.signal_message.connect(self.update_status)
        self.thread_add_plan.signals.signal_plan_dto.connect(self.on_signal_plan_dto)
        self.thread_add_plan.start()

    def start_thread_edit_plan(self, dto):
        self.thread_edit_plan = ThreadEditPlan(dto)
        self.thread_edit_plan.signals.signal_plan_dto.connect(self.on_signal_plan_dto)
        self.thread_edit_plan.start()

    def set_form_data(self):
        if not self.plan_to_edit_dto:
            return
        self.line_name.setText(self.plan_to_edit_dto.name)
        self.textEdit_datails.setText(self.plan_to_edit_dto.observation)

    def get_plan_dto(self):
        name = self.line_name.text()
        if not name:
            self.update_status(Message(MessageType.ERROR, "O plano não pode ser cadastrado sem nome"))
            return None


        observation = self.textEdit_datails.toPlainText()

        plan_dto = PlanDto()
        plan_dto.name = name
        plan_dto.observation = observation
        if self.plan_to_edit_dto:
            plan_dto.id = self.plan_to_edit_dto.id
        return plan_dto

    def on_signal_plan_dto(self, plan_dto):
        self.saved_plan_dto = plan_dto
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

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

import constants
from views.administrative.administrative_main_view import AdministrativeMainView
from views.styles import menu_button_style
from views.ui.converted.ui_main_view import Ui_MainWindow
from views.student.main_student_view import MainStudentView


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)

        # opening window in maximized size
        # self.showMaximized()

        self.btn_menu_lessons.clicked.connect(self.on_click_btn_menu_lessons)
        self.btn_menu_student.clicked.connect(self.on_click_btn_menu_student)
        self.btn_menu_message_forwarding.clicked.connect(self.on_click_btn_menu_message_forwarding)
        self.btn_registers.clicked.connect(self.on_click_btn_registers)
        self.stacked_pages.currentChanged.connect(self.on_stacked_pages_current_changed)

        self.btn_menu_lessons.setStyleSheet(menu_button_style.checked_menu)
        self.btn_menu_lessons.setIcon(QIcon("views/icons/phone-blue.png"))

        self.main_student_view = MainStudentView(self)
        self.main_administrative_view = AdministrativeMainView(self)

        self.btn_menu_lessons.setIcon(QIcon("views/icons/lesson.png"))
        self.btn_menu_student.setIcon(QIcon("views/icons/groups-white.png"))
        self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))
        self.btn_registers.setIcon(QIcon("views/icons/record_fill.png"))


        # Set License Label
        # self.set_license_label(license_dto)

        # Set Version
        self.label_copywrite.setText(f"Versão: {constants.APP_VERSION}")


    def on_click_btn_menu_lessons(self):
        self.stacked_pages.setCurrentIndex(0)

    def on_click_btn_menu_student(self):
        self.stacked_pages.setCurrentIndex(1)

    def on_click_btn_menu_message_forwarding(self):
        self.stacked_pages.setCurrentIndex(2)

    def on_click_btn_registers(self):
        self.stacked_pages.setCurrentIndex(3)


    def on_stacked_pages_current_changed(self, index):
        self.btn_menu_lessons.setIcon(QIcon("views/icons/lesson.png"))
        self.btn_menu_student.setIcon(QIcon("views/icons/groups-white.png"))
        self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))
        self.btn_registers.setIcon(QIcon("views/icons/record_fill.png"))

        if index == 0:
            self.btn_menu_lessons.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_lessons.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 1:
            self.btn_menu_student.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_student.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 2:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 3:
            self.btn_registers.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_registers.setStyleSheet(menu_button_style.unchecked_menu)

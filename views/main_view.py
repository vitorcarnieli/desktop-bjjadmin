from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QMessageBox

import constants
from dtos.message import Message
from enums.message_type import MessageType
from views.styles import menu_button_style
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)

        # opening window in maximized size
        # self.showMaximized()

        self.btn_menu_account.clicked.connect(self.on_click_btn_menu_account)
        self.btn_menu_group.clicked.connect(self.on_click_btn_menu_group)
        self.btn_menu_message_forwarding.clicked.connect(self.on_click_btn_menu_message_forwarding)
        self.btn_menu_configuration.clicked.connect(self.on_click_btn_menu_configuration)
        self.stacked_pages.currentChanged.connect(self.on_stacked_pages_current_changed)

        #self.btn_change_license.clicked.connect(self.on_click_btn_change_license)

        self.btn_menu_account.setStyleSheet(menu_button_style.checked_menu)
        self.btn_menu_account.setIcon(QIcon("views/icons/phone-blue.png"))
        """
        self.main_account_view = MainAccountView(self)
        self.main_group_view = MainGroupView(self)
        self.configuration_view = MainConfigurationView(self)
        self.main_reactions_task = MainReactionTaskView(self)
        """


        # Set License Label
        # self.set_license_label(license_dto)

        # Set Version
        self.label_copywrite.setText(f"Versão: {constants.APP_VERSION}")


    def on_click_btn_menu_account(self):
        self.stacked_pages.setCurrentIndex(0)

    def on_click_btn_menu_group(self):
        self.stacked_pages.setCurrentIndex(1)

    def on_click_btn_menu_message_forwarding(self):
        self.stacked_pages.setCurrentIndex(2)

    def on_click_btn_menu_configuration(self):
        self.stacked_pages.setCurrentIndex(3)

    def on_stacked_pages_current_changed(self, index):
        if index == 0:
            self.btn_menu_account.setStyleSheet(menu_button_style.checked_menu)
            self.btn_menu_account.setIcon(QIcon("views/icons/lesson.png"))
        else:
            self.btn_menu_account.setStyleSheet(menu_button_style.unchecked_menu)
            self.btn_menu_account.setIcon(QIcon("views/icons/lesson.png"))

        if index == 1:
            self.btn_menu_group.setStyleSheet(menu_button_style.checked_menu)
            self.btn_menu_group.setIcon(QIcon("views/icons/groups-white.png"))
        else:
            self.btn_menu_group.setStyleSheet(menu_button_style.unchecked_menu)
            self.btn_menu_group.setIcon(QIcon("views/icons/groups-white.png"))

        if index == 2:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.checked_menu)
            self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))
        else:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.unchecked_menu)
            self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))

        if index == 3:
            self.btn_menu_configuration.setStyleSheet(menu_button_style.checked_menu)
            self.btn_menu_configuration.setIcon(QIcon("views/icons/settings-white.png"))
        else:
            self.btn_menu_configuration.setStyleSheet(menu_button_style.unchecked_menu)
            self.btn_menu_configuration.setIcon(QIcon("views/icons/settings-white.png"))

    def on_signal_get_app_version(self, app_version: float):
        if app_version > constants.APP_VERSION:
            message_str = f"Existe uma nova versão do sistema.<br>Para baixar acesse: " \
                          f"<a href='{constants.APP_BASE_URL}'>{constants.APP_BASE_URL}</a>"
            #notification_view = NotificationView(self, QMessageBox.Icon.Information, message_str)
            #notification_view.exec()
            self.label_copywrite.setOpenExternalLinks(True)
            self.label_copywrite.setTextFormat(Qt.RichText)
            self.label_copywrite.setText(f"@2Tec Versão: {constants.APP_VERSION}. <a href='{constants.APP_BASE_URL}'>Baixar nova versão!</a>")

    def on_message(self, message: Message):
        if message.type == MessageType.ERROR:
            return
            #notification_view = NotificationView(self, QMessageBox.Icon.Critical, message.payload)
            #notification_view.exec()
        else:
            return
            #notification_view = NotificationView(self, QMessageBox.Icon.Information, message.payload)
            #notification_view.exec()

    """
        def set_license_label(self, license_dto: LicenseDto):
        if license_dto:
            expiration_date_str = DateService.get_date_str(license_dto.expiration_date)
            self.label_subscription.setText("Licença válida até: " + expiration_date_str)
    """

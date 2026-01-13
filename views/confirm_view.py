from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox


class ConfirmView(QMessageBox):

    def __init__(self, parent=None, title="", text=""):
        super(ConfirmView, self).__init__(parent)
        self.setStyleSheet("background-color: white; color:black;")
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("views/Icons/icon.ico"))
        self.setText(text)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_yes = self.button(QMessageBox.Yes)
        button_yes.setText('Sim')
        button_no = self.button(QMessageBox.No)
        button_no.setText('Não')

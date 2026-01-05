import sys
from PyQt6.QtWidgets import QApplication
from views.main_view import MainView

app = QApplication(sys.argv)

with open("views/styles/style.css", "r") as f:
    app.setStyleSheet(f.read())

main_view = MainView()
main_view.show()
sys.exit(app.exec())
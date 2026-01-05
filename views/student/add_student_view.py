from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QDialog

from views.ui.converted.student.ui_add_student_view import Ui_AddStudentView


class AddStudentView(QDialog, Ui_AddStudentView):

    def __init__(self, parent=None):
        super(AddStudentView, self).__init__(parent)
        self.setupUi(self)
        self.populate_combo_belts(True)

        pixmap = QPixmap("views/icons/user_without_photo.png")

        pixmap = pixmap.scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.label_user_photo.setPixmap(pixmap)


    def on_click_save_btn(self):
        # TODO
        return

    def on_selection_change_radio_belts(self):
        # TODO
        return

    def populate_combo_belts(self, is_adult: bool):

        def insert_option(file_name: str, translated_name: str):
            pixmap = QPixmap(f"views/icons/belts/{file_name}.png")
            pixmap = pixmap.scaled(
                69, 28,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.combo_belts.addItem(QIcon(pixmap), translated_name)

        self.combo_belts.setIconSize(QSize(69, 28))

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

from PyQt6.QtWidgets import QDialog

from views.ui.converted.student.ui_add_student_view import Ui_AddStudentView


class AddStudentView(QDialog, Ui_AddStudentView):

    def __init__(self, parent=None):
        super(AddStudentView, self).__init__(parent)
        self.setupUi(self)
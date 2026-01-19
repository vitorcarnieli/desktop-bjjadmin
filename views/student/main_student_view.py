from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem

from dtos.student_dto import StudentDto
from threads.student.thread_get_students import ThreadGetStudents
from views.student.add_student_view import StudentView
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainStudentView:
    def __init__(self, main_view: Ui_MainWindow):
        self.thread_get_students = None
        self.main_view = main_view

        self.main_view.btn_add_student.clicked.connect(self.on_click_btn_add_student)
        self.main_view.btn_remove_student.clicked.connect(self.on_click_btn_remove_student)
        self.main_view.table_students.doubleClicked.connect(self.on_double_click_table_students)
        self.main_view.table_students.itemSelectionChanged.connect(self.on_selection_change_table_students)

        self.main_view.table_students.setColumnHidden(0, True)

        self.student_dtos = []

        self.start_thread_get_students()

    # view handlers

    def on_click_btn_add_student(self):
        add_student_view = StudentView(parent=self.main_view)
        add_student_view.exec()
        student_dto = add_student_view.saved_student_dto
        if student_dto:
            self.student_dtos.append(student_dto)
            self.insert_table_students(student_dto)

    def on_click_btn_remove_student(self):
        # TODO
        return

    def on_double_click_table_students(self):
        row = self.main_view.table_students.currentIndex().row()
        cod = int(self.main_view.table_students.item(row, 0).text())
        student_dto = next((dto for dto in self.student_dtos if dto.id == cod), None)
        if not student_dto:
            return
        edit_view = StudentView(self.main_view, student_dto)
        edit_view.exec()
        if edit_view.saved_student_dto:
            updated = edit_view.saved_student_dto
            self.student_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.student_dtos
            ]
            self.insert_table_students(updated)

    def on_selection_change_table_students(self):
        # TODO
        return

    def insert_table_students(self, student_dto: StudentDto):
        self.main_view.label_total.setText(f"Total: {len(self.student_dtos)}")
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.main_view.table_students.rowCount()):
                cod = int(self.main_view.table_students.item(r, 0).text())
                if cod == student_dto.id:
                    row_position = r
                    already_exists_on_table = True
                    break
            if row_position is None:
                row_position = self.main_view.table_students.rowCount()
                self.main_view.table_students.insertRow(row_position)

            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(student_dto.id))
                set_qt_text_alignment_center(item_id)
                self.main_view.table_students.setItem(row_position, 0, item_id)

            # Name
            item_name = QTableWidgetItem(student_dto.name)
            self.main_view.table_students.setItem(row_position, 1, item_name)
            set_qt_text_alignment_center(item_name)

            # class
            item_students_amount = QTableWidgetItem(student_dto.lesson_class.name)
            self.main_view.table_students.setItem(row_position, 2, item_students_amount)
            set_qt_text_alignment_center(item_students_amount)

            # phone contact
            item_phone = QTableWidgetItem(student_dto.phone)
            self.main_view.table_students.setItem(row_position, 3, item_phone)
            set_qt_text_alignment_center(item_phone)

            # status
            item_observation = QTableWidgetItem(student_dto.observation)
            self.main_view.table_students.setItem(row_position, 4, item_observation)
            set_qt_text_alignment_center(item_observation)
        except Exception as e:
            print(e)
            return

    # threads

    def start_thread_get_students(self):
        self.thread_get_students = ThreadGetStudents()
        self.thread_get_students.signals.signal_student_dtos.connect(self.on_signal_student_dtos)
        self.thread_get_students.start()

    def on_signal_student_dtos(self, student_dtos):
        self.student_dtos = student_dtos
        for student in student_dtos:
            self.insert_table_students(student)

    # thread events

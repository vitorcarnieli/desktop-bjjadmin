from views.main_view import MainView


class MainStudentView:
    def __init__(self, main_view: MainView):
        self.main_view = main_view

        self.main_view.btn_add_student.clicked.connect(self.on_click_btn_add_student)
        self.main_view.btn_remove_student.clicked.connect(self.on_click_btn_remove_student)
        self.main_view.table_students.doubleClicked.connect(self.on_double_click_table_students)
        self.main_view.table_students.itemSelectionChanged.connect(self.on_selection_change_table_students)

        self.start_thread_list_students()

    def on_click_btn_add_student(self):
        """
        try:
            add_student_view = AddStudentView(parent=self.main_view)
            add_student_view.exec()
            student_dto = add_student_view.student_dto_added
            if student_dto:
                self.insert_table_students(student_dto)
        except Exception as e:
            notification_view = NotificationView(self.main_view, QMessageBox.Icon.Critical, str(e))
            notification_view.exec()
        """


    def on_click_btn_remove_student(self):
        # TODO
        return

    def on_double_click_table_students(self):
        # TODO
        return

    def on_selection_change_table_students(self):
        # TODO
        return

    def start_thread_list_students(self):
        # TODO
        return

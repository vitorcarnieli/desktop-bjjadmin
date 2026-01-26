from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QTableWidgetItem

from dtos.lesson_dto import LessonDto
from services.file_service import FileService
from threads.lesson.thread_get_lessons_by_date import ThreadGetLessonsByDate
from threads.lesson.thread_remove_lesson import ThreadRemoveLesson
from views.lesson.add_lesson_view import AddLessonView
from views.ui.converted.lesson.ui_lesson import Ui_lesson


class LessonView(QDialog, Ui_lesson):

    def __init__(self, parent, date):
        super(LessonView, self).__init__(parent)
        self.setupUi(self)
        self.date = date
        self.selected_item_id = None

        self.lesson_dtos = []

        self.pushButton_add.clicked.connect(self.on_click_btn_add)
        self.pushButton_remove.clicked.connect(self.on_click_btn_remove)
        self.tableWidget_lessons.doubleClicked.connect(self.on_double_click_table_lessons)
        self.tableWidget_lessons.itemSelectionChanged.connect(self.on_itemSelectionChanged)

        self.label_title_lesson.setText(f"Aulas - {self._get_format_date(date.day)}/{self._get_format_date(date.month)}/{date.year}")
        self.thread_get_lessons_by_date = None
        self.thread_remove_lesson = None
        self.tableWidget_lessons.setColumnHidden(0, True)
        self.start_thread_get_lessons_by_date()

    # ThreadGetLessonsByDate
    def start_thread_get_lessons_by_date(self):
        self.thread_get_lessons_by_date = ThreadGetLessonsByDate(self.date)
        self.thread_get_lessons_by_date.signals.signal_lesson_dtos.connect(self.on_signal_lesson_dtos)
        self.thread_get_lessons_by_date.start()

    def on_signal_lesson_dtos(self, dtos):
        self.lesson_dtos = dtos
        for dto in dtos:
            self.insert_table_lessons(dto)

    # ThreadRemoveLesson
    def start_thread_remove_lesson(self):
        self.thread_remove_lesson = ThreadRemoveLesson(self.selected_item_id)
        self.thread_remove_lesson.signals.signal_finished.connect(self.on_signal_finished_thread_remove_lesson)
        self.thread_remove_lesson.start()

    def on_signal_finished_thread_remove_lesson(self, id):
        for row in range(self.tableWidget_lessons.rowCount()):
            item = self.tableWidget_lessons.item(row, 0)
            if item and item.text() == str(id):
                self.tableWidget_lessons.removeRow(row)
        dto = next((l for l in self.lesson_dtos if l.id == int(id)), None)
        self.selected_item_id = None
        self.lesson_dtos.remove(dto)
        self.tableWidget_lessons.clearSelection()

    # ui events
    def on_itemSelectionChanged(self):
        selected_items = self.tableWidget_lessons.selectedItems()
        if not selected_items:
            self.selected_item_id = None
            self.pushButton_remove.setEnabled(False)
            return None

        row = selected_items[0].row()
        self.selected_item_id = self.tableWidget_lessons.item(row, 0).text()
        self.pushButton_remove.setEnabled(True)
        return None

    def on_click_btn_add(self):
        add_lesson_view = AddLessonView(self, self.date)
        add_lesson_view.exec()
        lesson_added = add_lesson_view.saved_lesson_dto
        if lesson_added:
            if add_lesson_view.profile_photo_changed:
                photo_path = Path(add_lesson_view.profile_photo_changed)
                new_name = f"{lesson_added.id}{photo_path.suffix}"
                rename = str(photo_path.parent / new_name)
                FileService.remove_file(rename)
                FileService.rename_file(add_lesson_view.profile_photo_changed, rename)

            self.lesson_dtos.append(lesson_added)
            self.insert_table_lessons(lesson_added)

    def on_click_btn_remove(self):
        self.start_thread_remove_lesson()

    def on_double_click_table_lessons(self):
        row = self.tableWidget_lessons.currentIndex().row()
        cod = int(self.tableWidget_lessons.item(row, 0).text())
        student_dto = next((dto for dto in self.lesson_dtos if dto.id == cod), None)
        if not student_dto:
            return
        edit_view = AddLessonView(self, self.date, student_dto)
        edit_view.exec()
        if edit_view.saved_lesson_dto:
            if edit_view.profile_photo_changed:
                photo_path = Path(edit_view.profile_photo_changed)
                new_name = f"{student_dto.id}{photo_path.suffix}"
                rename = str(photo_path.parent / new_name)
                FileService.remove_file(rename)
                FileService.rename_file(edit_view.profile_photo_changed, rename)
            updated = edit_view.saved_lesson_dto
            self.lesson_dtos = [
                updated if dto.id == updated.id else dto
                for dto in self.lesson_dtos
            ]
            self.insert_table_lessons(updated)

    # helpers
    def _get_format_date(self, date):
        return date if date >= 10 else f"0{date}"

    def insert_table_lessons(self, dto: LessonDto):
        try:
            row_position = None
            already_exists_on_table = False

            for r in range(self.tableWidget_lessons.rowCount()):
                cod = int(self.tableWidget_lessons.item(r, 0).text())
                if cod == dto.id:
                    row_position = r
                    already_exists_on_table = True
                    break
            if row_position is None:
                row_position = self.tableWidget_lessons.rowCount()
                self.tableWidget_lessons.insertRow(row_position)

            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            if not already_exists_on_table:
                item_id = QTableWidgetItem(str(dto.id))
                set_qt_text_alignment_center(item_id)
                self.tableWidget_lessons.setItem(row_position, 0, item_id)

            # Name
            item_name = QTableWidgetItem(dto.name)
            self.tableWidget_lessons.setItem(row_position, 1, item_name)
            set_qt_text_alignment_center(item_name)

            # class
            item_class = QTableWidgetItem(dto.lesson_class.name)
            self.tableWidget_lessons.setItem(row_position, 2, item_class)
            set_qt_text_alignment_center(item_class)

            # students amount
            item_students_amount = QTableWidgetItem(str(len(dto.students)) if dto.students else "0")
            self.tableWidget_lessons.setItem(row_position, 3, item_students_amount)
            set_qt_text_alignment_center(item_students_amount)

        except Exception as e:
            print(e)
            return

from datetime import date

from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtCore import QDate
from PySide6.QtGui import QTextCharFormat, QColor, QFont

from threads.lesson.thread_get_lesson_dates import ThreadGetLessonDates
from views.lesson.lesson_view import LessonView
from views.ui.converted.ui_main_view import Ui_MainWindow


class MainLessonView:
    def __init__(self, main_view: Ui_MainWindow):
        self.thread_get_lesson_dates = None
        self.main_view = main_view

        self.main_view.calendarWidget.activated.connect(self.on_calendar_activated)
        self.start_thread_get_lesson_dates()

    def start_thread_get_lesson_dates(self):
        self.thread_get_lesson_dates = ThreadGetLessonDates()
        self.thread_get_lesson_dates.signals.signal_dates.connect(self.on_signal_dates)
        self.thread_get_lesson_dates.start()

    def on_signal_dates(self, dates):
        q_dates = [QDate(d.date.year, d.date.month, d.date.day) for d in dates]
        for d in q_dates:
            self.highlight_date(d)


    def on_calendar_activated(self, event):
        date = self.main_view.calendarWidget.selectedDate().toPython()
        a = LessonView(self.main_view, date)
        a.exec()

    def highlight_date(self, date):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor("#fff"))
        fmt.setForeground(QColor("green"))
        fmt.setFontPointSize(13)
        fmt.setFontWeight(QFont.Bold)
        self.main_view.calendarWidget.setDateTextFormat(date, fmt)

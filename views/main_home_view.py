from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView

from threads.thread_load_home import ThreadLoadHome
from views.pie_chart_widget import PieChartWidget
from views.ui.converted.ui_main_view import Ui_MainWindow
from views.week_column_chart_widget import WeekColumnChartWidget


class MainHomeView:
    def __init__(self, main_view: Ui_MainWindow):
        self.profile_photo_path = None
        self._user_photo_pixmap = None
        self.thread_load_home = None
        self.thread_load_payment_records_is_running = False
        self.main_view = main_view

        self.start_thread_load_home()

    def start_thread_load_home(self):
        self.thread_load_home = ThreadLoadHome()
        self.thread_load_home.signals.signal_payment_infos.connect(self.on_signal_payment_infos)
        self.thread_load_home.signals.signal_birth_infos.connect(self.on_signal_birth_infos)
        self.thread_load_home.signals.signal_classes_infos.connect(self.on_signal_classes_infos)
        self.thread_load_home.signals.signal_lessons_infos.connect(self.on_signal_lessons_infos)
        self.thread_load_home.start()

    def on_signal_lessons_infos(self, data):
        chart = WeekColumnChartWidget(
            title="Aulas por dia",
            data=data
        )

        self.main_view.column_layout.addWidget(chart)

    def on_signal_classes_infos(self, data):
        self.chart = PieChartWidget(
            title="Alunos por turma",
            data=data
        )
        self.main_view.pie_layout.addWidget(self.chart)

    def format_date_to_portuguese(self, date_of_birth) -> str:
        weekdays_pt = [
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo"
        ]

        today = date.today()

        try:
            current_year_birthday = date(
                today.year,
                date_of_birth.month,
                date_of_birth.day
            )
        except ValueError:
            current_year_birthday = date(today.year, 2, 28)

        weekday_name = weekdays_pt[current_year_birthday.weekday()]

        return f"{weekday_name} - {date_of_birth:%d/%m}"

    def insert_table(self, student_dto):
        try:
            row_position = self.main_view.table_birthday.rowCount()
            self.main_view.table_birthday.insertRow(row_position)

            def set_qt_text_alignment_center(ui_element):
                ui_element.setTextAlignment(Qt.AlignCenter)

            today = date.today()

            age = today.year - student_dto.date_of_birth.year

            item_name = QTableWidgetItem(
                f"{student_dto.name} - {age} anos"
            )
            self.main_view.table_birthday.setItem(row_position, 0, item_name)
            set_qt_text_alignment_center(item_name)

            item_date = QTableWidgetItem(
                self.format_date_to_portuguese(student_dto.date_of_birth)
            )
            self.main_view.table_birthday.setItem(row_position, 1, item_date)
            set_qt_text_alignment_center(item_date)

            if (student_dto.date_of_birth.month == today.month and
                    student_dto.date_of_birth.day == today.day):

                green_color = QColor(0, 128, 0)

                for column in range(self.main_view.table_birthday.columnCount()):
                    item = self.main_view.table_birthday.item(row_position, column)
                    if item:
                        item.setBackground(green_color)

            header = self.main_view.table_birthday.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)

        except Exception as e:
            print(e)



    def on_signal_birth_infos(self, infos):
        for student_dto in infos["month"]:
            self.insert_table(student_dto)

    def on_signal_payment_infos(self, infos):
        def format_value(value):
            if not("." in str(value)):
                return f"R$ {value},00"
            else:
                value_split = str(value).split(".")
                if len(value_split[-1]) < 2:
                    value_split[-1] = f"{value_split[-1]}0"
                return f"R$ {value_split[0]},{value_split[-1]}"

        self.main_view.total_num.setText(str(infos["total"]))
        self.main_view.paied_num.setText(format_value(infos["paid"]))
        self.main_view.peding_num.setText(format_value(infos["pending"]))

    def reset_view(self):
        # 1. Parar thread atual com segurança
        if self.thread_load_home and self.thread_load_home.isRunning():
            try:
                self.thread_load_home.quit()
                self.thread_load_home.wait()
            except Exception:
                pass

        self.thread_load_home = None

        # 2. Limpar layout de gráfico de colunas
        self._clear_layout(self.main_view.column_layout)

        # 3. Limpar layout de gráfico de pizza
        self._clear_layout(self.main_view.pie_layout)

        # 4. Limpar tabela
        self.main_view.table_birthday.setRowCount(0)

        # 5. Resetar labels
        self.main_view.total_num.setText("0")
        self.main_view.paied_num.setText("R$ 0,00")
        self.main_view.peding_num.setText("R$ 0,00")

        # 6. Reiniciar carregamento
        self.start_thread_load_home()

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

            child_layout = item.layout()
            if child_layout is not None:
                self._clear_layout(child_layout)

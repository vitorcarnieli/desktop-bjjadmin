from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow

from threads.thread_load_home import ThreadLoadHome
from views.administrative.administrative_main_view import AdministrativeMainView
from views.lesson.main_lesson_view import MainLessonView
from views.main_home_view import MainHomeView
from views.payment_record.main_payment_record_view import MainPaymentRecordView
from views.styles import menu_button_style
from views.ui.converted.ui_main_view import Ui_MainWindow
from views.student.main_student_view import MainStudentView


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./views/icons/window_icon.ico"))

        pixmap = QPixmap("./views/icons/logo3.png").scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )


        label = self.label_logo
        label.setPixmap(pixmap)
        label.setMouseTracking(True)
        label.setCursor(Qt.CursorShape.PointingHandCursor)

        # opening window in maximized size
        self.showMaximized()

        self.btn_home.clicked.connect(self.on_click_btn_menu_home)
        self.btn_menu_lessons.clicked.connect(self.on_click_btn_menu_lessons)
        self.btn_menu_student.clicked.connect(self.on_click_btn_menu_student)
        self.btn_menu_message_forwarding.clicked.connect(self.on_click_btn_menu_message_forwarding)
        self.btn_registers.clicked.connect(self.on_click_btn_registers)
        self.stacked_pages.currentChanged.connect(self.on_stacked_pages_current_changed)

        self.btn_home.setStyleSheet(menu_button_style.checked_menu)

        self.main_home_view = MainHomeView(self)
        self.main_administrative_view = AdministrativeMainView(self)
        self.main_lesson_view = MainLessonView(self)
        self.main_payment_record_view = MainPaymentRecordView(self)
        self.main_student_view = MainStudentView(self)

        self.btn_home.setIcon(QIcon("views/icons/home.png"))
        self.btn_menu_lessons.setIcon(QIcon("views/icons/lesson.png"))
        self.btn_menu_student.setIcon(QIcon("views/icons/groups-white.png"))
        self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))
        self.btn_registers.setIcon(QIcon("views/icons/record_fill.png"))
        self.refresh_home_btn.setIcon(QIcon("views/icons/refresh_white.png"))
        self.refresh_home_btn.setIcon(QIcon("views/icons/refresh_white.png"))
        self.btn_student_view_card.setIcon(QIcon("views/icons/cards.png"))
        self.btn_student_view_table.setIcon(QIcon("views/icons/list.png"))


        # Set Version
        self.label_copywrite.setText(f"Versão: 1.3")

        self.calendarWidget.setStyleSheet("""
        /* QCalendarWidget - Estilo Moderno */
QCalendarWidget {
    background-color: rgb(32, 32, 32);
    border: 1px solid rgb(60, 60, 60);
    border-radius: 12px;
    padding: 8px;
}

/* Barra de navegação superior */
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: rgb(40, 40, 40);
    border-radius: 0px;
    padding: 4px;
    margin-bottom: 0px;
}

/* Botões de navegação (anterior/próximo) */
QCalendarWidget QToolButton {
    background-color: rgb(50, 50, 50);
    border: 1px solid rgb(70, 70, 70);
    border-radius: 6px;
    color: rgb(220, 220, 220);
    padding: 6px;
    margin: 2px;
    font-weight: bold;
}

QCalendarWidget QToolButton:hover {
    background-color: rgb(70, 130, 255);
    border-color: rgb(90, 150, 255);
}

QCalendarWidget QToolButton:pressed {
    background-color: rgb(50, 110, 235);
}

/* Botão do menu (dropdown ano/mês) */
QCalendarWidget QToolButton::menu-indicator {
    image: none;
    width: 0px;
}

/* Setas de navegação */
QCalendarWidget QToolButton#qt_calendar_prevmonth {
    qproperty-icon: url(none);
    qproperty-text: "<";
}

QCalendarWidget QToolButton#qt_calendar_nextmonth {
    qproperty-icon: url(none);
    qproperty-text: ">";
}

/* Botão de seleção de mês */
QCalendarWidget QToolButton#qt_calendar_monthbutton {
    background-color: transparent;
    border: none;
    color: rgb(70, 130, 255);
    font-size: 14px;
    font-weight: bold;
    padding: 6px 12px;
}

QCalendarWidget QToolButton#qt_calendar_monthbutton:hover {
    background-color: rgb(50, 50, 50);
    border-radius: 6px;
}

/* Botão de seleção de ano */
QCalendarWidget QToolButton#qt_calendar_yearbutton {
    background-color: transparent;
    border: none;
    color: rgb(70, 130, 255);
    font-size: 14px;
    font-weight: bold;
    padding: 6px 12px;
}

QCalendarWidget QToolButton#qt_calendar_yearbutton:hover {
    background-color: rgb(50, 50, 50);
    border-radius: 6px;
}

/* Menu dropdown para mês/ano */
QCalendarWidget QMenu {
    background-color: rgb(40, 40, 40);
    border: 1px solid rgb(70, 70, 70);
    border-radius: 8px;
    padding: 4px;
}

QCalendarWidget QMenu::item {
    padding: 6px 20px;
    color: rgb(220, 220, 220);
    border-radius: 4px;
}

QCalendarWidget QMenu::item:selected {
    background-color: rgb(70, 130, 255);
}

/* SpinBox para navegação de ano */
QCalendarWidget QSpinBox {
    background-color: rgb(50, 50, 50);
    border: 1px solid rgb(70, 70, 70);
    border-radius: 6px;
    color: rgb(220, 220, 220);
    padding: 4px 8px;
    selection-background-color: rgb(70, 130, 255);
}

QCalendarWidget QSpinBox::up-button,
QCalendarWidget QSpinBox::down-button {
    background-color: rgb(60, 60, 60);
    border: none;
    border-radius: 3px;
}

QCalendarWidget QSpinBox::up-button:hover,
QCalendarWidget QSpinBox::down-button:hover {
    background-color: rgb(70, 130, 255);
}

/* Tabela do calendário */
QCalendarWidget QTableView {
    background-color: rgb(32, 32, 32);
    border: none;
    selection-background-color: rgb(70, 130, 255);
    selection-color: white;
    outline: none;
    gridline-color: rgb(45, 45, 45);
}

/* Cabeçalho (dias da semana) */
QCalendarWidget QTableView QHeaderView::section {
    background-color: #fff;
    color: rgb(150, 150, 150);
    padding: 8px;
    border: none;
    font-weight: bold;
    font-size: 11px;
    text-transform: uppercase;
}
QCalendarWidget QTableView::horizontalHeader::section {
    background-color: rgb(255, 255, 255);
    color: rgb(200, 200, 200);
}
/* Células do calendário */
QCalendarWidget QAbstractItemView {
    color: rgb(220, 220, 220);
    font-size: 13px;
}

QCalendarWidget QAbstractItemView:enabled {
    color: rgb(220, 220, 220);
}

QCalendarWidget QAbstractItemView:disabled {
    color: rgb(100, 100, 100);
}

/* Dia atual */
QCalendarWidget QAbstractItemView:enabled {
    selection-background-color: rgb(70, 130, 255);
    selection-color: white;
}

/* Células do calendário - sem efeito de fundo */
QCalendarWidget QTableView::item {
    background-color: transparent;
}

QCalendarWidget QTableView::item:hover {
    background-color: rgb(50, 50, 50);
    border-radius: 4px;
}

/* Dia selecionado */
QCalendarWidget QTableView::item:selected {
    background-color: rgb(70, 130, 255);
    color: white;
    border-radius: 4px;
    font-weight: bold;
}

/* Dias de outros meses (desabilitados) */
QCalendarWidget QTableView::item:disabled {
    color: rgb(80, 80, 80);
}

/* Scrollbars (caso apareçam) */
QCalendarWidget QScrollBar:vertical {
    background-color: rgb(32, 32, 32);
    width: 12px;
    border-radius: 6px;
}

QCalendarWidget QScrollBar::handle:vertical {
    background-color: rgb(70, 70, 70);
    border-radius: 6px;
    min-height: 20px;
}

QCalendarWidget QScrollBar::handle:vertical:hover {
    background-color: rgb(90, 90, 90);
}

QCalendarWidget QScrollBar::add-line:vertical,
QCalendarWidget QScrollBar::sub-line:vertical {
    height: 0px;
}
        """)

    def on_click_btn_menu_home(self):
        self.stacked_pages.setCurrentIndex(0)

    def on_click_btn_menu_lessons(self):
        self.stacked_pages.setCurrentIndex(1)

    def on_click_btn_menu_student(self):
        self.stacked_pages.setCurrentIndex(2)

    def on_click_btn_menu_message_forwarding(self):
        self.stacked_pages.setCurrentIndex(3)

    def on_click_btn_registers(self):
        self.stacked_pages.setCurrentIndex(4)


    def on_stacked_pages_current_changed(self, index):
        self.btn_home.setIcon(QIcon("views/icons/home.png"))
        self.btn_menu_lessons.setIcon(QIcon("views/icons/lesson.png"))
        self.btn_menu_student.setIcon(QIcon("views/icons/groups-white.png"))
        self.btn_menu_message_forwarding.setIcon(QIcon("views/icons/administrative.png"))
        self.btn_registers.setIcon(QIcon("views/icons/record_fill.png"))

        if index == 0:
            self.btn_home.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_home.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 1:
            self.btn_menu_lessons.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_lessons.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 2:
            self.btn_menu_student.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_student.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 3:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_menu_message_forwarding.setStyleSheet(menu_button_style.unchecked_menu)

        if index == 4:
            self.btn_registers.setStyleSheet(menu_button_style.checked_menu)
        else:
            self.btn_registers.setStyleSheet(menu_button_style.unchecked_menu)

    def reset_all(self):
        self.setEnabled(False)
        self.main_administrative_view = AdministrativeMainView(self)
        self.main_lesson_view = MainLessonView(self)
        self.main_payment_record_view = MainPaymentRecordView(self)
        self.main_student_view = MainStudentView(self)
        self.main_home_view = MainHomeView(self)
        self.setEnabled(True)

    def reset_student(self):
        self.setEnabled(False)
        self.main_student_view = MainStudentView(self)
        self.setEnabled(True)

    def reset_payment_record(self):
        self.setEnabled(False)
        self.main_payment_record_view = MainPaymentRecordView(self)
        self.setEnabled(True)

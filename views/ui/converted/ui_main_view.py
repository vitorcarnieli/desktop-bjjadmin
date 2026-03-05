# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 758)
        icon = QIcon()
        icon.addFile(u"../../icons/window_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        MainWindow.setIconSize(QSize(16, 16))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.centralwidget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.left_menu = QVBoxLayout(self.frame_left_menu)
        self.left_menu.setSpacing(6)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setContentsMargins(0, 0, 0, 0)
        self.layout_top_menu = QFrame(self.frame_left_menu)
        self.layout_top_menu.setObjectName(u"layout_top_menu")
        self.layout_top_menu.setMinimumSize(QSize(250, 0))
        self.layout_top_menu.setMaximumSize(QSize(16777215, 16777215))
        self.layout_top_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_top_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout_top_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.layout_top_menu)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setPointSize(18)
        self.label_logo.setFont(font)
        self.label_logo.setStyleSheet(u"color: white;")
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_logo)

        self.btn_home = QPushButton(self.layout_top_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px!important;\n"
"	background-color:  #303030;\n"
"	color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_menu_lessons = QPushButton(self.layout_top_menu)
        self.btn_menu_lessons.setObjectName(u"btn_menu_lessons")
        self.btn_menu_lessons.setMinimumSize(QSize(0, 40))
        self.btn_menu_lessons.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  #303030;\n"
"	color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../icons/lesson.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_lessons.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btn_menu_lessons)

        self.btn_menu_student = QPushButton(self.layout_top_menu)
        self.btn_menu_student.setObjectName(u"btn_menu_student")
        self.btn_menu_student.setMinimumSize(QSize(0, 40))
        self.btn_menu_student.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  #303030;\n"
"	color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../icons/groups-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_student.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btn_menu_student)

        self.btn_menu_message_forwarding = QPushButton(self.layout_top_menu)
        self.btn_menu_message_forwarding.setObjectName(u"btn_menu_message_forwarding")
        self.btn_menu_message_forwarding.setMinimumSize(QSize(0, 40))
        self.btn_menu_message_forwarding.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  #303030;\n"
"	color: white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../icons/administrative.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_message_forwarding.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.btn_menu_message_forwarding)

        self.btn_registers = QPushButton(self.layout_top_menu)
        self.btn_registers.setObjectName(u"btn_registers")
        self.btn_registers.setMinimumSize(QSize(0, 40))
        self.btn_registers.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 20px;\n"
"	text-align: left;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  #303030;\n"
"	color: white;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../icons/record_fill.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_registers.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.btn_registers)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.beta_label = QLabel(self.layout_top_menu)
        self.beta_label.setObjectName(u"beta_label")

        self.verticalLayout_2.addWidget(self.beta_label)


        self.left_menu.addWidget(self.layout_top_menu)

        self.line_2 = QFrame(self.frame_left_menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setEnabled(True)
        font1 = QFont()
        font1.setKerning(True)
        self.line_2.setFont(font1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.left_menu.addWidget(self.line_2)

        self.frame_license = QFrame(self.frame_left_menu)
        self.frame_license.setObjectName(u"frame_license")
        self.frame_license.setStyleSheet(u"border-top: 1px")
        self.frame_license.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_license.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_license)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_subscription = QLabel(self.frame_license)
        self.label_subscription.setObjectName(u"label_subscription")
        self.label_subscription.setStyleSheet(u"color: white;")
        self.label_subscription.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_subscription)

        self.label_copywrite = QLabel(self.frame_license)
        self.label_copywrite.setObjectName(u"label_copywrite")
        self.label_copywrite.setStyleSheet(u"color: white;")
        self.label_copywrite.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_copywrite)


        self.left_menu.addWidget(self.frame_license)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.stacked_pages = QStackedWidget(self.centralwidget)
        self.stacked_pages.setObjectName(u"stacked_pages")
        self.stacked_pages.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_21 = QVBoxLayout(self.page_home)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.refresh_home_btn = QPushButton(self.page_home)
        self.refresh_home_btn.setObjectName(u"refresh_home_btn")
        self.refresh_home_btn.setMinimumSize(QSize(30, 30))
        self.refresh_home_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(33, 33, 33);\n"
"	border-radius: 10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../icons/refresh_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_home_btn.setIcon(icon6)

        self.horizontalLayout_11.addWidget(self.refresh_home_btn)


        self.verticalLayout_21.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_total = QFrame(self.page_home)
        self.frame_total.setObjectName(u"frame_total")
        self.frame_total.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.frame_total.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_total.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_total)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_total)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label)

        self.total_num = QLabel(self.frame_total)
        self.total_num.setObjectName(u"total_num")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.total_num.setFont(font3)
        self.total_num.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.total_num)


        self.horizontalLayout_7.addWidget(self.frame_total)

        self.frame_paied = QFrame(self.page_home)
        self.frame_paied.setObjectName(u"frame_paied")
        self.frame_paied.setStyleSheet(u"background-color: green;")
        self.frame_paied.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_paied.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_paied)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.frame_paied)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_6)

        self.paied_num = QLabel(self.frame_paied)
        self.paied_num.setObjectName(u"paied_num")
        self.paied_num.setFont(font3)
        self.paied_num.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.paied_num)


        self.horizontalLayout_7.addWidget(self.frame_paied)

        self.frame_peding = QFrame(self.page_home)
        self.frame_peding.setObjectName(u"frame_peding")
        self.frame_peding.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_peding.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_peding.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_peding)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_23232 = QLabel(self.frame_peding)
        self.label_23232.setObjectName(u"label_23232")
        self.label_23232.setFont(font2)
        self.label_23232.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_23232)

        self.peding_num = QLabel(self.frame_peding)
        self.peding_num.setObjectName(u"peding_num")
        self.peding_num.setFont(font3)
        self.peding_num.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.peding_num)


        self.horizontalLayout_7.addWidget(self.frame_peding)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.payment_pie_layout = QHBoxLayout()
        self.payment_pie_layout.setObjectName(u"payment_pie_layout")

        self.verticalLayout_12.addLayout(self.payment_pie_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.pie_layout = QHBoxLayout()
        self.pie_layout.setObjectName(u"pie_layout")

        self.verticalLayout_13.addLayout(self.pie_layout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_6)

        self.column_layout = QHBoxLayout()
        self.column_layout.setObjectName(u"column_layout")

        self.verticalLayout_20.addLayout(self.column_layout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_20)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.page_home)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)

        self.table_birthday = QTableWidget(self.page_home)
        if (self.table_birthday.columnCount() < 2):
            self.table_birthday.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_birthday.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_birthday.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_birthday.setObjectName(u"table_birthday")
        self.table_birthday.setStyleSheet(u"/* QTableWidget / QTableView - Dark Modern */\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(24, 24, 24);\n"
"    color: rgb(220, 220, 220);\n"
"    gridline-color: rgb(45, 45, 45);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 10px;\n"
"    font-size: 13px;\n"
"    selection-background-color: rgb(52, 120, 180);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Linhas alternadas */\n"
"QTableWidget::item:alternate {\n"
"    background-color: rgb(28, 28, 28);\n"
"}\n"
"\n"
"/* Hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"/* Selecionado */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(52, 120, 180);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Header horizontal */\n"
"QHeaderView::section {\n"
"    background-color: rgb(32, 32, 32);\n"
"    color: rgb(200, 200, 200);\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(45, 45, 45);\n"
"    border-right: 1px solid rgb(45, 45, 45);\n"
"    font-"
                        "weight: bold;\n"
"}\n"
"\n"
"/* Header hover */\n"
"QHeaderView::section:hover {\n"
"    background-color: rgb(38, 38, 38);\n"
"}\n"
"\n"
"/* Scrollbars minimalistas */\n"
"QScrollBar:vertical {\n"
"    background: rgb(24, 24, 24);\n"
"    width: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    height: 0;\n"
"}\n"
"\n"
"/* Foco discreto */\n"
"QTableWidget:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.table_birthday.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_birthday.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table_birthday.horizontalHeader().setStretchLastSection(True)
        self.table_birthday.verticalHeader().setVisible(False)
        self.table_birthday.verticalHeader().setHighlightSections(False)
        self.table_birthday.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_11.addWidget(self.table_birthday)


        self.horizontalLayout_10.addLayout(self.verticalLayout_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.stacked_pages.addWidget(self.page_home)
        self.page_lesson = QWidget()
        self.page_lesson.setObjectName(u"page_lesson")
        self.verticalLayout_3 = QVBoxLayout(self.page_lesson)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_lesson)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"margin-left: 0px;}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_page_account = QLabel(self.frame)
        self.label_page_account.setObjectName(u"label_page_account")
        font4 = QFont()
        font4.setPointSize(13)
        self.label_page_account.setFont(font4)
        self.label_page_account.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_page_account)

        self.line_page_account = QFrame(self.frame)
        self.line_page_account.setObjectName(u"line_page_account")
        self.line_page_account.setStyleSheet(u" border: none;\n"
"                        background: rgb(255, 255, 255);")
        self.line_page_account.setFrameShape(QFrame.Shape.HLine)
        self.line_page_account.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_page_account)

        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"/* QCalendarWidget - Estilo Moderno */\n"
"QCalendarWidget {\n"
"    background-color: rgb(32, 32, 32);\n"
"    border: 1px solid rgb(60, 60, 60);\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Barra de navega\u00e7\u00e3o superior */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: rgb(40, 40, 40);\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"/* Bot\u00f5es de navega\u00e7\u00e3o (anterior/pr\u00f3ximo) */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    border-radius: 6px;\n"
"    color: rgb(220, 220, 220);\n"
"    padding: 6px;\n"
"    margin: 2px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: rgb(70, 130, 255);\n"
"    border-color: rgb(90, 150, 255);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: rgb(50, 110, 235);\n"
"}\n"
"\n"
"/* Bot\u00e3"
                        "o do menu (dropdown ano/m\u00eas) */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    image: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* Setas de navega\u00e7\u00e3o */\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(none);\n"
"    qproperty-text: \"<\";\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(none);\n"
"    qproperty-text: \">\";\n"
"}\n"
"\n"
"/* Bot\u00e3o de sele\u00e7\u00e3o de m\u00eas */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: rgb(70, 130, 255);\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Bot\u00e3o de sele\u00e7\u00e3o de ano */\n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"    background-color: transp"
                        "arent;\n"
"    border: none;\n"
"    color: rgb(70, 130, 255);\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Menu dropdown para m\u00eas/ano */\n"
"QCalendarWidget QMenu {\n"
"    background-color: rgb(40, 40, 40);\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item {\n"
"    padding: 6px 20px;\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu::item:selected {\n"
"    background-color: rgb(70, 130, 255);\n"
"}\n"
"\n"
"/* SpinBox para navega\u00e7\u00e3o de ano */\n"
"QCalendarWidget QSpinBox {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    border-radius: 6px;\n"
"    color: rgb(220, 220, 220);\n"
"    padding: 4px 8px;\n"
"    selection-ba"
                        "ckground-color: rgb(70, 130, 255);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button,\n"
"QCalendarWidget QSpinBox::down-button {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button:hover,\n"
"QCalendarWidget QSpinBox::down-button:hover {\n"
"    background-color: rgb(70, 130, 255);\n"
"}\n"
"\n"
"/* Tabela do calend\u00e1rio */\n"
"QCalendarWidget QTableView {\n"
"    background-color: rgb(32, 32, 32);\n"
"    border: none;\n"
"    selection-background-color: rgb(70, 130, 255);\n"
"    selection-color: white;\n"
"    outline: none;\n"
"    gridline-color: rgb(45, 45, 45);\n"
"}\n"
"\n"
"/* Cabe\u00e7alho (dias da semana) */\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    background-color: #323232;\n"
"    color: rgb(150, 150, 150);\n"
"    padding: 8px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"/* C\u00e9lulas do calend\u00e1"
                        "rio */\n"
"QCalendarWidget QAbstractItemView {\n"
"    color: rgb(220, 220, 220);\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"/* Dia atual */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    selection-background-color: rgb(70, 130, 255);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* C\u00e9lulas do calend\u00e1rio - sem efeito de fundo */\n"
"QCalendarWidget QTableView::item {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Dia selecionado */\n"
"QCalendarWidget QTableView::item:selected {\n"
"    background-color: rgb(70, 130, 255);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Dias de outros meses (desabilitados) */\n"
"QCalendarWidge"
                        "t QTableView::item:disabled {\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* Scrollbars (caso apare\u00e7am) */\n"
"QCalendarWidget QScrollBar:vertical {\n"
"    background-color: rgb(32, 32, 32);\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QCalendarWidget QScrollBar::handle:vertical {\n"
"    background-color: rgb(70, 70, 70);\n"
"    border-radius: 6px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QCalendarWidget QScrollBar::add-line:vertical,\n"
"QCalendarWidget QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}")
        self.calendarWidget.setMinimumDate(QDate(2026, 1, 1))
        self.calendarWidget.setMaximumDate(QDate(2100, 12, 31))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.verticalLayout.addWidget(self.calendarWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.stacked_pages.addWidget(self.page_lesson)
        self.page_student = QWidget()
        self.page_student.setObjectName(u"page_student")
        self.verticalLayout_16 = QVBoxLayout(self.page_student)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_manage_students = QLabel(self.page_student)
        self.label_manage_students.setObjectName(u"label_manage_students")
        self.label_manage_students.setFont(font4)
        self.label_manage_students.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_manage_students)

        self.line_manage__students = QFrame(self.page_student)
        self.line_manage__students.setObjectName(u"line_manage__students")
        self.line_manage__students.setStyleSheet(u" border: none;\n"
"                        background: rgb(255, 255, 255);")
        self.line_manage__students.setFrameShape(QFrame.Shape.HLine)
        self.line_manage__students.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_manage__students)

        self.layout_buttons_manage_students = QHBoxLayout()
        self.layout_buttons_manage_students.setObjectName(u"layout_buttons_manage_students")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_buttons_manage_students.addItem(self.horizontalSpacer_9)

        self.btn_add_student = QPushButton(self.page_student)
        self.btn_add_student.setObjectName(u"btn_add_student")
        self.btn_add_student.setMinimumSize(QSize(130, 30))
        self.btn_add_student.setMaximumSize(QSize(250, 30))
        self.btn_add_student.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon7 = QIcon()
        icon7.addFile(u"../../../../../2tec/engagement-telegram/views/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_student.setIcon(icon7)

        self.layout_buttons_manage_students.addWidget(self.btn_add_student)

        self.btn_remove_student = QPushButton(self.page_student)
        self.btn_remove_student.setObjectName(u"btn_remove_student")
        self.btn_remove_student.setEnabled(False)
        self.btn_remove_student.setMinimumSize(QSize(130, 30))
        self.btn_remove_student.setMaximumSize(QSize(250, 30))
        self.btn_remove_student.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon8 = QIcon()
        icon8.addFile(u"../../../../../2tec/engagement-telegram/views/icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_remove_student.setIcon(icon8)

        self.layout_buttons_manage_students.addWidget(self.btn_remove_student)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_buttons_manage_students.addItem(self.horizontalSpacer_10)


        self.verticalLayout_16.addLayout(self.layout_buttons_manage_students)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_student_filter = QLabel(self.page_student)
        self.label_student_filter.setObjectName(u"label_student_filter")
        self.label_student_filter.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_student_filter)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.student_filter_layout = QHBoxLayout()
        self.student_filter_layout.setObjectName(u"student_filter_layout")

        self.horizontalLayout_8.addLayout(self.student_filter_layout)

        self.student_search_by_name = QLineEdit(self.page_student)
        self.student_search_by_name.setObjectName(u"student_search_by_name")
        self.student_search_by_name.setMinimumSize(QSize(125, 30))
        self.student_search_by_name.setMaximumSize(QSize(250, 16777215))
        self.student_search_by_name.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    background: #ffffff;\n"
"    color: #333333;\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.student_search_by_name)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.btn_student_view_card = QPushButton(self.page_student)
        self.btn_student_view_card.setObjectName(u"btn_student_view_card")
        self.btn_student_view_card.setEnabled(True)
        self.btn_student_view_card.setMinimumSize(QSize(30, 30))
        self.btn_student_view_card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_student_view_card.setStyleSheet(u"QPushButton {\n"
"background-color: #2f2f2f; border-radius: 6px;\n"
"                            }")

        self.horizontalLayout_8.addWidget(self.btn_student_view_card)

        self.btn_student_view_table = QPushButton(self.page_student)
        self.btn_student_view_table.setObjectName(u"btn_student_view_table")
        self.btn_student_view_table.setEnabled(True)
        self.btn_student_view_table.setMinimumSize(QSize(30, 30))
        self.btn_student_view_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_student_view_table.setStyleSheet(u"QPushButton {\n"
"background-color: #2f2f2f; border-radius: 6px;\n"
"                            }")

        self.horizontalLayout_8.addWidget(self.btn_student_view_table)

        self.label_7 = QLabel(self.page_student)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.cards_scroll_area = QScrollArea(self.page_student)
        self.cards_scroll_area.setObjectName(u"cards_scroll_area")
        self.cards_scroll_area.setStyleSheet(u"border:none;")
        self.cards_scroll_area.setWidgetResizable(True)
        self.cards_container = QWidget()
        self.cards_container.setObjectName(u"cards_container")
        self.cards_container.setGeometry(QRect(0, 0, 744, 306))
        self.verticalLayout_22 = QVBoxLayout(self.cards_container)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.cards_scroll_area.setWidget(self.cards_container)

        self.verticalLayout_16.addWidget(self.cards_scroll_area)

        self.table_students = QTableWidget(self.page_student)
        if (self.table_students.columnCount() < 5):
            self.table_students.setColumnCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_students.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_students.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_students.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_students.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_students.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.table_students.setObjectName(u"table_students")
        self.table_students.setStyleSheet(u"QTableWidget{\n"
"                                background: #F0F3F6;\n"
"                                border: none;\n"
"                                border-radius: 20px;\n"
"                                selection-background-color: #d5e3f2;\n"
"                                selection-color: inherit;\n"
"                                }\n"
"\n"
"                                QHeaderView::section {\n"
"                                background-color: #E3E9EF;\n"
"                                border: none;\n"
"                                height: 32px;\n"
"                                }\n"
"\n"
"                                QHeaderView::section:first {\n"
"                                border-top-left-radius: 20px;\n"
"                                }\n"
"\n"
"\n"
"                                QHeaderView::section:last {\n"
"                                border-top-right-radius: 20px;\n"
"                                }\n"
"                              ")
        self.table_students.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_students.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_students.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_students.horizontalHeader().setStretchLastSection(True)
        self.table_students.verticalHeader().setVisible(False)
        self.table_students.verticalHeader().setDefaultSectionSize(45)

        self.verticalLayout_16.addWidget(self.table_students)

        self.stacked_pages.addWidget(self.page_student)
        self.page_administrative = QWidget()
        self.page_administrative.setObjectName(u"page_administrative")
        self.page_administrative.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.page_administrative)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_page_administrative = QLabel(self.page_administrative)
        self.label_page_administrative.setObjectName(u"label_page_administrative")
        self.label_page_administrative.setFont(font4)
        self.label_page_administrative.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_page_administrative)

        self.line_page_administrative = QFrame(self.page_administrative)
        self.line_page_administrative.setObjectName(u"line_page_administrative")
        self.line_page_administrative.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_page_administrative.setFrameShape(QFrame.Shape.HLine)
        self.line_page_administrative.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_page_administrative)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget_2 = QTabWidget(self.page_administrative)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #cfcfcf;\n"
"    background: #f9f9f9;\n"
"    border-radius: 4px;\n"
"    top: -1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #e6e6e6;\n"
"    border: 1px solid #cfcfcf;\n"
"    border-bottom: none;\n"
"    padding: 6px 14px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    color: #444;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #ffffff;\n"
"    color: #222;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #f2f2f2;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"")
        self.tab_plan = QWidget()
        self.tab_plan.setObjectName(u"tab_plan")
        self.tab_plan.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.tab_plan)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_add_plan = QPushButton(self.tab_plan)
        self.btn_add_plan.setObjectName(u"btn_add_plan")
        self.btn_add_plan.setMinimumSize(QSize(110, 30))
        self.btn_add_plan.setMaximumSize(QSize(250, 30))
        self.btn_add_plan.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")

        self.horizontalLayout_3.addWidget(self.btn_add_plan)

        self.btn_remove_plan = QPushButton(self.tab_plan)
        self.btn_remove_plan.setObjectName(u"btn_remove_plan")
        self.btn_remove_plan.setEnabled(False)
        self.btn_remove_plan.setMinimumSize(QSize(110, 30))
        self.btn_remove_plan.setMaximumSize(QSize(250, 30))
        self.btn_remove_plan.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")

        self.horizontalLayout_3.addWidget(self.btn_remove_plan)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)

        self.table_plan = QTableWidget(self.tab_plan)
        if (self.table_plan.columnCount() < 5):
            self.table_plan.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_plan.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_plan.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_plan.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_plan.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_plan.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.table_plan.setObjectName(u"table_plan")
        self.table_plan.setStyleSheet(u"QTableWidget{\n"
"                                background: #F0F3F6;\n"
"                                border: none;\n"
"                                border-radius: 20px;\n"
"                                selection-background-color: #d5e3f2;\n"
"                                selection-color: inherit;\n"
"                                }\n"
"\n"
"                                QHeaderView::section {\n"
"                                background-color: #E3E9EF;\n"
"                                border: none;\n"
"                                height: 32px;\n"
"                                }\n"
"\n"
"                                QHeaderView::section:first {\n"
"                                border-top-left-radius: 20px;\n"
"                                }\n"
"\n"
"\n"
"                                QHeaderView::section:last {\n"
"                                border-top-right-radius: 20px;\n"
"                                }\n"
"                              ")
        self.table_plan.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_plan.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_plan.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_plan.horizontalHeader().setStretchLastSection(True)
        self.table_plan.verticalHeader().setVisible(False)
        self.table_plan.verticalHeader().setHighlightSections(False)

        self.verticalLayout_15.addWidget(self.table_plan)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)

        self.tabWidget_2.addTab(self.tab_plan, "")
        self.tab_class = QWidget()
        self.tab_class.setObjectName(u"tab_class")
        self.tab_class.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.tab_class)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.btn_add_class = QPushButton(self.tab_class)
        self.btn_add_class.setObjectName(u"btn_add_class")
        self.btn_add_class.setMinimumSize(QSize(110, 30))
        self.btn_add_class.setMaximumSize(QSize(250, 30))
        self.btn_add_class.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")

        self.horizontalLayout_5.addWidget(self.btn_add_class)

        self.btn_remove_class = QPushButton(self.tab_class)
        self.btn_remove_class.setObjectName(u"btn_remove_class")
        self.btn_remove_class.setEnabled(False)
        self.btn_remove_class.setMinimumSize(QSize(110, 30))
        self.btn_remove_class.setMaximumSize(QSize(250, 30))
        self.btn_remove_class.setStyleSheet(u"QPushButton {\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")

        self.horizontalLayout_5.addWidget(self.btn_remove_class)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addLayout(self.horizontalLayout_5)

        self.table_class = QTableWidget(self.tab_class)
        if (self.table_class.columnCount() < 4):
            self.table_class.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_class.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_class.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_class.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_class.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.table_class.setObjectName(u"table_class")
        self.table_class.setStyleSheet(u"QTableWidget{\n"
"                                background: #F0F3F6;\n"
"                                border: none;\n"
"                                border-radius: 20px;\n"
"                                selection-background-color: #d5e3f2;\n"
"                                selection-color: inherit;\n"
"                                }\n"
"\n"
"                                QHeaderView::section {\n"
"                                background-color: #E3E9EF;\n"
"                                border: none;\n"
"                                height: 32px;\n"
"                                }\n"
"\n"
"                                QHeaderView::section:first {\n"
"                                border-top-left-radius: 20px;\n"
"                                }\n"
"\n"
"\n"
"                                QHeaderView::section:last {\n"
"                                border-top-right-radius: 20px;\n"
"                                }\n"
"                              ")
        self.table_class.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_class.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_class.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_class.horizontalHeader().setCascadingSectionResizes(False)
        self.table_class.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_class.horizontalHeader().setStretchLastSection(True)
        self.table_class.verticalHeader().setVisible(False)
        self.table_class.verticalHeader().setHighlightSections(False)

        self.verticalLayout_17.addWidget(self.table_class)


        self.verticalLayout_19.addLayout(self.verticalLayout_17)

        self.tabWidget_2.addTab(self.tab_class, "")

        self.verticalLayout_5.addWidget(self.tabWidget_2)

        self.stacked_pages.addWidget(self.page_administrative)
        self.page_records = QWidget()
        self.page_records.setObjectName(u"page_records")
        self.verticalLayout_6 = QVBoxLayout(self.page_records)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_manage_students_2 = QLabel(self.page_records)
        self.label_manage_students_2.setObjectName(u"label_manage_students_2")
        self.label_manage_students_2.setFont(font4)
        self.label_manage_students_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_manage_students_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.btn_reload_records = QPushButton(self.page_records)
        self.btn_reload_records.setObjectName(u"btn_reload_records")
        self.btn_reload_records.setStyleSheet(u"background-color: transparent;")
        self.btn_reload_records.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.btn_reload_records)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.line_manage__students_2 = QFrame(self.page_records)
        self.line_manage__students_2.setObjectName(u"line_manage__students_2")
        self.line_manage__students_2.setStyleSheet(u" border: none;\n"
"                        background: rgb(255, 255, 255);")
        self.line_manage__students_2.setFrameShape(QFrame.Shape.HLine)
        self.line_manage__students_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_manage__students_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_record_total_records = QLabel(self.page_records)
        self.label_record_total_records.setObjectName(u"label_record_total_records")
        self.label_record_total_records.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_record_total_records)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_total_payment_done = QLabel(self.page_records)
        self.label_total_payment_done.setObjectName(u"label_total_payment_done")
        self.label_total_payment_done.setStyleSheet(u"color: green;")

        self.horizontalLayout.addWidget(self.label_total_payment_done)

        self.label_4 = QLabel(self.page_records)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.page_records)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.page_records)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.label_5)

        self.label_total_payment_pedding = QLabel(self.page_records)
        self.label_total_payment_pedding.setObjectName(u"label_total_payment_pedding")
        self.label_total_payment_pedding.setStyleSheet(u"color: red;")

        self.horizontalLayout.addWidget(self.label_total_payment_pedding)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.layout_filter_records = QVBoxLayout()
        self.layout_filter_records.setObjectName(u"layout_filter_records")

        self.horizontalLayout_13.addLayout(self.layout_filter_records)

        self.records_search_by_name = QLineEdit(self.page_records)
        self.records_search_by_name.setObjectName(u"records_search_by_name")
        self.records_search_by_name.setMinimumSize(QSize(0, 30))
        self.records_search_by_name.setMaximumSize(QSize(250, 16777215))
        self.records_search_by_name.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    background: #ffffff;\n"
"    color: #333333;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.records_search_by_name)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.comboBox_month = QComboBox(self.page_records)
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.setObjectName(u"comboBox_month")
        self.comboBox_month.setStyleSheet(u"            QComboBox {\n"
"    background: #383838;\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #ffffff;\n"
"    background: #383838;\n"
"}\n"
"\n"
"/* ComboBox desabilitada */\n"
"QComboBox:disabled {\n"
"    background: #2b2b2b;\n"
"    color: #777777;\n"
"}\n"
"\n"
"/* Itens desabilitados */\n"
"QComboBox QAbstractItemView::item:disabled {\n"
"    background: #2b2b2b;\n"
"    color: #777777;\n"
"}\n"
"\n"
"/* Item selecionado mas desabilitado */\n"
"QComboBox QAbstractItemView::item:selected:disabled {\n"
"    background: #303030;\n"
"}")

        self.horizontalLayout_4.addWidget(self.comboBox_month)

        self.comboBox_year = QComboBox(self.page_records)
        self.comboBox_year.setObjectName(u"comboBox_year")
        self.comboBox_year.setStyleSheet(u"            QComboBox {\n"
"    background: #383838;\n"
"    color: #ffffff;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #ffffff;\n"
"    background: #383838;\n"
"}\n"
"\n"
"/* ComboBox desabilitada */\n"
"QComboBox:disabled {\n"
"    background: #2b2b2b;\n"
"    color: #777777;\n"
"}\n"
"\n"
"/* Itens desabilitados */\n"
"QComboBox QAbstractItemView::item:disabled {\n"
"    background: #2b2b2b;\n"
"    color: #777777;\n"
"}\n"
"\n"
"/* Item selecionado mas desabilitado */\n"
"QComboBox QAbstractItemView::item:selected:disabled {\n"
"    background: #303030;\n"
"}")

        self.horizontalLayout_4.addWidget(self.comboBox_year)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.btn_money_on = QPushButton(self.page_records)
        self.btn_money_on.setObjectName(u"btn_money_on")
        self.btn_money_on.setMinimumSize(QSize(30, 30))
        self.btn_money_on.setStyleSheet(u"QPushButton {\n"
"\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 100px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon9 = QIcon()
        icon9.addFile(u"../../icons/money.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_money_on.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.btn_money_on)

        self.btn_money_forgiven = QPushButton(self.page_records)
        self.btn_money_forgiven.setObjectName(u"btn_money_forgiven")
        self.btn_money_forgiven.setMinimumSize(QSize(30, 30))
        self.btn_money_forgiven.setStyleSheet(u"QPushButton {\n"
"\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 100px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon10 = QIcon()
        icon10.addFile(u"../../icons/money_forgiven.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_money_forgiven.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.btn_money_forgiven)

        self.btn_money_off = QPushButton(self.page_records)
        self.btn_money_off.setObjectName(u"btn_money_off")
        self.btn_money_off.setMinimumSize(QSize(30, 30))
        self.btn_money_off.setStyleSheet(u"QPushButton {\n"
"\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 100px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon11 = QIcon()
        icon11.addFile(u"../../icons/un_money_money.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_money_off.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.btn_money_off)

        self.label_2 = QLabel(self.page_records)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(15, 0))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.btn_whatsapp = QPushButton(self.page_records)
        self.btn_whatsapp.setObjectName(u"btn_whatsapp")
        self.btn_whatsapp.setMinimumSize(QSize(30, 30))
        self.btn_whatsapp.setStyleSheet(u"QPushButton {\n"
"\n"
"                            background: #383838;\n"
"                            color: white;\n"
"                            border-radius: 100px;\n"
"                            }\n"
"\n"
"                            QPushButton:hover {\n"
"                            background-color: #303030;\n"
"                            color: white;\n"
"                            }\n"
"\n"
"                            QPushButton:disabled{\n"
"                            background-color: rgb(222, 222, 222);\n"
"                            }")
        icon12 = QIcon()
        icon12.addFile(u"../../icons/whatsapp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_whatsapp.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.btn_whatsapp)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.table_payment_records = QTableWidget(self.page_records)
        if (self.table_payment_records.columnCount() < 6):
            self.table_payment_records.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_payment_records.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.table_payment_records.setObjectName(u"table_payment_records")
        self.table_payment_records.setMinimumSize(QSize(0, 0))
        self.table_payment_records.setStyleSheet(u"QTableWidget{\n"
"                                background: #F0F3F6;\n"
"                                border: none;\n"
"                                border-radius: 20px;\n"
"                                selection-background-color: #d5e3f2;\n"
"                                selection-color: inherit;\n"
"                                }\n"
"\n"
"                                QHeaderView::section {\n"
"                                background-color: #E3E9EF;\n"
"                                border: none;\n"
"                                height: 32px;\n"
"                                }\n"
"\n"
"                                QHeaderView::section:first {\n"
"                                border-top-left-radius: 20px;\n"
"                                }\n"
"\n"
"\n"
"                                QHeaderView::section:last {\n"
"                                border-top-right-radius: 20px;\n"
"                                }\n"
"                              ")
        self.table_payment_records.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_payment_records.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_payment_records.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_payment_records.horizontalHeader().setStretchLastSection(True)
        self.table_payment_records.verticalHeader().setVisible(False)
        self.table_payment_records.verticalHeader().setDefaultSectionSize(45)

        self.verticalLayout_6.addWidget(self.table_payment_records)

        self.stacked_pages.addWidget(self.page_records)

        self.horizontalLayout_2.addWidget(self.stacked_pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_pages.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BJJ Admin \u2014 Gerencie seu CT com efici\u00eancia ", None))
        self.label_logo.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.btn_menu_lessons.setText(QCoreApplication.translate("MainWindow", u"Aulas", None))
        self.btn_menu_student.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.btn_menu_message_forwarding.setText(QCoreApplication.translate("MainWindow", u"Administrativo", None))
        self.btn_registers.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.beta_label.setText("")
        self.label_subscription.setText("")
        self.label_copywrite.setText("")
        self.refresh_home_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total de Alunos", None))
        self.total_num.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total de Pagamentos", None))
        self.paied_num.setText(QCoreApplication.translate("MainWindow", u"R$ 00000,00", None))
        self.label_23232.setText(QCoreApplication.translate("MainWindow", u"Total de Pend\u00eancias", None))
        self.peding_num.setText(QCoreApplication.translate("MainWindow", u"R$ 00000,00", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Aniversariantes do M\u00eas", None))
        ___qtablewidgetitem = self.table_birthday.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.table_birthday.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_page_account.setText(QCoreApplication.translate("MainWindow", u"Gerenciar Aulas", None))
        self.label_manage_students.setText(QCoreApplication.translate("MainWindow", u"Gerenciar Alunos", None))
        self.btn_add_student.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remove_student.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.label_student_filter.setText(QCoreApplication.translate("MainWindow", u"Total:.", None))
        self.student_search_by_name.setText("")
        self.student_search_by_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por nome", None))
        self.btn_student_view_card.setText("")
        self.btn_student_view_table.setText("")
        self.label_7.setText("")
        ___qtablewidgetitem2 = self.table_students.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem3 = self.table_students.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem4 = self.table_students.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem5 = self.table_students.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Contato", None));
        ___qtablewidgetitem6 = self.table_students.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_page_administrative.setText(QCoreApplication.translate("MainWindow", u"Administrativo", None))
        self.btn_add_plan.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remove_plan.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem7 = self.table_plan.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem8 = self.table_plan.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem9 = self.table_plan.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem10 = self.table_plan.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"N. de Alunos", None));
        ___qtablewidgetitem11 = self.table_plan.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Detalhes", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_plan), QCoreApplication.translate("MainWindow", u"Planos", None))
        self.btn_add_class.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remove_class.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem12 = self.table_class.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem13 = self.table_class.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem14 = self.table_class.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"N. de Alunos", None));
        ___qtablewidgetitem15 = self.table_class.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Detalhes", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_class), QCoreApplication.translate("MainWindow", u"Turmas", None))
        self.label_manage_students_2.setText(QCoreApplication.translate("MainWindow", u"Registros", None))
#if QT_CONFIG(tooltip)
        self.btn_reload_records.setToolTip(QCoreApplication.translate("MainWindow", u"Recarregar p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reload_records.setText("")
        self.label_record_total_records.setText(QCoreApplication.translate("MainWindow", u"Total de registros:", None))
        self.label_total_payment_done.setText(QCoreApplication.translate("MainWindow", u"Total pago:", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total perdoado:", None))
        self.label_5.setText("")
        self.label_total_payment_pedding.setText(QCoreApplication.translate("MainWindow", u"Total pendente:", None))
        self.records_search_by_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por nome", None))
        self.comboBox_month.setItemText(0, QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.comboBox_month.setItemText(1, QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.comboBox_month.setItemText(2, QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.comboBox_month.setItemText(3, QCoreApplication.translate("MainWindow", u"Abril", None))
        self.comboBox_month.setItemText(4, QCoreApplication.translate("MainWindow", u"Maio", None))
        self.comboBox_month.setItemText(5, QCoreApplication.translate("MainWindow", u"Junho", None))
        self.comboBox_month.setItemText(6, QCoreApplication.translate("MainWindow", u"Julho", None))
        self.comboBox_month.setItemText(7, QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.comboBox_month.setItemText(8, QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.comboBox_month.setItemText(9, QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.comboBox_month.setItemText(10, QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.comboBox_month.setItemText(11, QCoreApplication.translate("MainWindow", u"Dezembro", None))

#if QT_CONFIG(tooltip)
        self.btn_money_on.setToolTip(QCoreApplication.translate("MainWindow", u"Definir como \"Pago\"", None))
#endif // QT_CONFIG(tooltip)
        self.btn_money_on.setText("")
#if QT_CONFIG(tooltip)
        self.btn_money_forgiven.setToolTip(QCoreApplication.translate("MainWindow", u"Definir como \"Perdoado\"", None))
#endif // QT_CONFIG(tooltip)
        self.btn_money_forgiven.setText("")
#if QT_CONFIG(tooltip)
        self.btn_money_off.setToolTip(QCoreApplication.translate("MainWindow", u"Definir como \"Pendente\"", None))
#endif // QT_CONFIG(tooltip)
        self.btn_money_off.setText("")
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_whatsapp.setToolTip(QCoreApplication.translate("MainWindow", u"Enviar mensagem de cobran\u00e7a", None))
#endif // QT_CONFIG(tooltip)
        self.btn_whatsapp.setText("")
        ___qtablewidgetitem16 = self.table_payment_records.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem17 = self.table_payment_records.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Aluno", None));
        ___qtablewidgetitem18 = self.table_payment_records.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem19 = self.table_payment_records.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Plano", None));
        ___qtablewidgetitem20 = self.table_payment_records.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Valor Cobrado", None));
        ___qtablewidgetitem21 = self.table_payment_records.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Status do Pagamento", None));
    # retranslateUi


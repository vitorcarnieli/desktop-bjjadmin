from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis
)
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QMargins

class WeekColumnChartWidget(QWidget):

    _DAYS = [
        "Seg",
        "Ter",
        "Qua",
        "Qui",
        "Sex",
        "Sáb",
        "Dom"
    ]

    def __init__(self, title: str, data: list[int], parent=None):
        super().__init__(parent)

        self._validate_data(data)

        self.setMinimumHeight(300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Conjunto de barras
        bar_set = QBarSet(title)

        for value in data:
            bar_set.append(value)

        # Série
        series = QBarSeries()
        series.append(bar_set)

        # Chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setMargins(QMargins(0, 0, 0, 0))

        # Eixo X (dias)
        axis_x = QBarCategoryAxis()
        axis_x.append(self._DAYS[:len(data)])

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        # Eixo Y (valores)
        axis_y = QValueAxis()

        max_value = max(data) if data else 0
        axis_y.setRange(0, max_value)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        # View
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setMinimumHeight(300)
        chart_view.setMinimumWidth(400)  # CRÍTICO

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(chart_view)

    def _validate_data(self, data):

        if not isinstance(data, list):
            raise TypeError("data must be list[int]")

        if len(data) > 7:
            raise ValueError("data cannot have more than 7 values")

        for value in data:

            if not isinstance(value, (int, float)):
                raise TypeError("values must be numbers")

            if value < 0:
                raise ValueError("values cannot be negative")

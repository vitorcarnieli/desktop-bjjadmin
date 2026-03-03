from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis
)
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtCore import Qt, QMargins


class WeekColumnChartWidget(QWidget):

    _DAYS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

    def __init__(
        self,
        title: str,
        data: list[int],
        background_color: str | None = None,
        text_color: str | None = None,
        parent=None
    ):
        super().__init__(parent)

        self._validate_data(data)

        self.setMinimumHeight(300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        parsed_bg = self._parse_hex_color(background_color) if background_color else None
        parsed_text = self._parse_hex_color(text_color) if text_color else None

        # Conjunto de barras
        bar_set = QBarSet(title)
        for value in data:
            bar_set.append(value)

        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.legend().setVisible(False)

        if parsed_text:
            chart.setTitleBrush(QBrush(parsed_text))

        if parsed_bg:
            chart.setBackgroundBrush(parsed_bg)
            chart.setPlotAreaBackgroundBrush(parsed_bg)
            chart.setPlotAreaBackgroundVisible(True)

        # Eixo X
        axis_x = QBarCategoryAxis()
        axis_x.append(self._DAYS[:len(data)])

        if parsed_text:
            axis_x.setLabelsBrush(QBrush(parsed_text))
            axis_x.setTitleBrush(QBrush(parsed_text))

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        # Eixo Y
        axis_y = QValueAxis()
        max_value = max(data) if data else 0
        axis_y.setRange(0, max_value)

        if parsed_text:
            axis_y.setLabelsBrush(QBrush(parsed_text))
            axis_y.setTitleBrush(QBrush(parsed_text))

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setMinimumHeight(300)
        chart_view.setMinimumWidth(400)
        chart_view.setMaximumWidth(400)

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

    def _parse_hex_color(self, hex_color: str) -> QColor:
        if not isinstance(hex_color, str) or not hex_color.startswith("#"):
            raise ValueError("Color must be hex string like #RRGGBB")

        color = QColor(hex_color)
        if not color.isValid():
            raise ValueError(f"Invalid hex color: {hex_color}")

        return color

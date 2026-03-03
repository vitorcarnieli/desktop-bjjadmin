from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtCore import QMargins


class PieChartWidget(QWidget):

    def __init__(
        self,
        title: str,
        data: list[dict],
        background_color: str | None = None,
        label_color: str | None = None,
        title_color: str | None = None,
        parent=None
    ):
        super().__init__(parent)

        self.setMinimumHeight(300)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._validate_data(data)

        series = QPieSeries()
        total = sum(item["percent"] for item in data)

        parsed_label_color = self._parse_hex_color(label_color) if label_color else None
        parsed_title_color = self._parse_hex_color(title_color) if title_color else None

        for item in data:
            label = item["label"]
            value = item["percent"]

            pie_slice = series.append(label, value)

            percent = (value / total) * 100 if total else 0
            pie_slice.setLabel(f"{label} ({percent:.1f}%)")
            pie_slice.setLabelVisible(True)

            # Cor da fatia (opcional)
            if "color" in item and item["color"]:
                pie_slice.setBrush(self._parse_hex_color(item["color"]))

            # Cor do texto da fatia
            if parsed_label_color:
                pie_slice.setLabelBrush(QBrush(parsed_label_color))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)

        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.legend().setVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Cor do título
        if parsed_title_color:
            chart.setTitleBrush(QBrush(parsed_title_color))

        # Cor de fundo
        if background_color:
            bg = self._parse_hex_color(background_color)
            chart.setBackgroundBrush(bg)
            chart.setPlotAreaBackgroundBrush(bg)
            chart.setPlotAreaBackgroundVisible(True)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setMinimumHeight(300)
        chart_view.setMinimumWidth(400)
        chart_view.setMaximumWidth(400)
        chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(chart_view)

    def _validate_data(self, data):
        if not isinstance(data, list):
            raise TypeError("data must be list")

        for item in data:
            if "label" not in item or "percent" not in item:
                raise ValueError("Invalid data format")

            if not isinstance(item["percent"], (int, float)):
                raise TypeError("percent must be numeric")

    def _parse_hex_color(self, hex_color: str | None) -> QColor:
        if not hex_color:
            raise ValueError("Color cannot be empty")

        if not isinstance(hex_color, str) or not hex_color.startswith("#"):
            raise ValueError("Color must be hex string like #RRGGBB")

        color = QColor(hex_color)
        if not color.isValid():
            raise ValueError(f"Invalid hex color: {hex_color}")

        return color

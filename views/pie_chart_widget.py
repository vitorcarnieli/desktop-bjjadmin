from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import QMargins


class PieChartWidget(QWidget):

    def __init__(self, title: str, data: list[dict], parent=None):
        super().__init__(parent)

        self.setMinimumHeight(300)  # CRÍTICO
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._validate_data(data)

        series = QPieSeries()

        total = sum(item["percent"] for item in data)

        for item in data:

            label = item["label"]
            value = item["percent"]

            slice = series.append(label, value)

            percent = (value / total) * 100 if total else 0

            slice.setLabel(f"{label} ({percent:.1f}%)")
            slice.setLabelVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)

        # melhorias importantes
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.legend().setVisible(False)  # evita duplicação com labels
        chart.setAnimationOptions(QChart.SeriesAnimations)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        chart_view.setMinimumHeight(300)  # CRÍTICO
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

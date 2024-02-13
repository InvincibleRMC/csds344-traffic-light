from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow)

from traffic_light import TrafficLight
from traffic_state import TrafficState


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSDS 344 Traffic Simulation")
        self.setFixedSize(QSize(1200, 1200))

        self.label = QLabel('Hello World!', parent=self)
        traffic_light = TrafficLight(parent=self)

        traffic_light.move(150, 150)

        self.label.move(0, 0)


app = QApplication([])

window = Window()
window.show()

app.exec()

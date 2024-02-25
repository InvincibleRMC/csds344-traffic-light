from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow)

from traffic_light import TrafficLight, TrafficLightDirection
from traffic_state import TrafficState

HEIGHT = 900
WIDTH = 1200


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSDS 344 Traffic Simulation")
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        self.label = QLabel('Hello World!', parent=self)
        right_traffic_light = TrafficLight(TrafficLightDirection.EAST_WEST, parent=self)
        left_traffic_light = TrafficLight(TrafficLightDirection.EAST_WEST, parent=self)

        top_traffic_light = TrafficLight(TrafficLightDirection.NORTH_SOUTH, parent=self)
        bottom_traffic_light = TrafficLight(TrafficLightDirection.NORTH_SOUTH, parent=self)

        right_traffic_light.move(900, 450)
        left_traffic_light.move(300, 450)
        top_traffic_light.move(600, 700)
        bottom_traffic_light.move(600, 50)

        self.label.move(0, 0)


app = QApplication([])

window = Window()
window.show()

app.exec()

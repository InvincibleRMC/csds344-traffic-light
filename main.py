from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

from enum import IntEnum


class TrafficState(IntEnum):
    NORTH_SOUTH_LEFT = 0
    NORTH_SOUTH_RIGHT = 1
    NORTH_SOUTH_STRAIGHT = 2
    EAST_WEST_LEFT = 3
    EAST_WEST_RIGHT = 4
    EAST_WEST_STRAIGHT = 5


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSDS 344 Traffic Simulation")
        self.setFixedSize(QSize(600, 600))

        self.label = QLabel('Hello World!', parent=self)

        self.label.move(0, 0)


app = QApplication([])

window = Window()
window.show()

app.exec()

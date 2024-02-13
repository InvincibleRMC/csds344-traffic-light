from enum import IntEnum
from typing import Optional

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Circle(QLabel):
    def __init__(self, parent: Optional[QWidget] = None,
                 radius: int = 50,
                 color: Optional[QColor | Qt.GlobalColor] = None) -> None:
        super().__init__(parent)
        self.setFixedSize(QSize(2 * radius, 2 * radius))
        stylesheet = self.styleSheet()
        self.setStyleSheet(f"{stylesheet}border-radius: {radius}px;")

        if color:
            self.set_color(color)

    def set_color(self, color: QColor | Qt.GlobalColor) -> None:
        if isinstance(color, Qt.GlobalColor):
            color = QColor(color)
        style = f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});"
        self.setStyleSheet(f"{self.styleSheet()}{style}")

    def update_color(self, color: QColor | Qt.GlobalColor) -> None:
        style = self.styleSheet()
        style.find('background-color')
        split = style.split('background-color')
        self.setStyleSheet(split[0])
        self.set_color(color)


class CircleIndicator(Circle):
    def __init__(self, parent: Optional[QWidget] = None,
                 radius: int = 50) -> None:
        super().__init__(parent, radius)
        self.set_black()

    def set_red(self) -> None:
        self.update_color(Qt.GlobalColor.red)

    def set_yellow(self) -> None:
        self.update_color(Qt.GlobalColor.yellow)

    def set_green(self) -> None:
        self.update_color(Qt.GlobalColor.green)

    def set_black(self) -> None:
        self.update_color(Qt.GlobalColor.black)


class TrafficLightState(IntEnum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        layout = QVBoxLayout()
        green_circle = CircleIndicator(radius=25)
        green_circle.set_green()

        yellow_circle = CircleIndicator(radius=25)
        yellow_circle.set_yellow()

        red_circle = CircleIndicator(radius=25)
        red_circle.set_red()

        layout.addWidget(green_circle)
        layout.addWidget(yellow_circle)
        layout.addWidget(red_circle)
        layout.addWidget(QLabel("hello world"))

        self.setLayout(layout)
        self.setFixedSize(QSize(200, 200))

        self.state = TrafficLightState.GREEN

    def next_state(self) -> None:
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.RED

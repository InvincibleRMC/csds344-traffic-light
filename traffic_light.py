from enum import IntEnum
from typing import Optional
from traffic_state import TrafficState

from PyQt6.QtCore import QSize, Qt, pyqtSlot, pyqtSignal
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

    def clear_color(self) -> None:
        style = self.styleSheet()
        if 'background-color' in style:
            style.find('background-color')
            split = style.split('background-color')
            self.setStyleSheet(split[0])

    def update_color(self, color: QColor | Qt.GlobalColor) -> None:
        self.clear_color()
        self.set_color(color)


class CircleIndicator(Circle):
    def __init__(self, parent: Optional[QWidget] = None,
                 radius: int = 50) -> None:
        super().__init__(parent, radius)

    def set_red(self) -> None:
        self.update_color(Qt.GlobalColor.red)

    def set_yellow(self) -> None:
        self.update_color(Qt.GlobalColor.yellow)

    def set_green(self) -> None:
        self.update_color(Qt.GlobalColor.green)

    def set_black(self) -> None:
        self.update_color(Qt.GlobalColor.black)


class TrafficLightDirection(IntEnum):
    NORTH_SOUTH = 0
    EAST_WEST = 1


class TrafficLightState(IntEnum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight(QWidget):

    signal = pyqtSignal(TrafficState)

    def __init__(self, traffic_light_direction: TrafficLightDirection,
                 parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        layout = QVBoxLayout()

        red_circle = CircleIndicator(radius=25)
        red_circle.set_red()

        yellow_circle = CircleIndicator(radius=25)
        yellow_circle.set_black()

        green_circle = CircleIndicator(radius=25)
        green_circle.set_black()

        layout.addWidget(red_circle)
        layout.addWidget(yellow_circle)
        layout.addWidget(green_circle)

        self.setLayout(layout)
        self.setFixedSize(QSize(200, 200))

        self.direction = traffic_light_direction
        self.state = TrafficLightState.RED

        self.red_circle = red_circle
        self.yellow_circle = yellow_circle
        self.green_circle = green_circle

        self.signal.connect(self.update_state)

    def next_state(self) -> None:
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.RED

    def start_cycle(self) -> None:
        pass

    def set_lights(self, state: TrafficLightState) -> None:
        match state:
            case TrafficLightState.RED:
                self.red_circle.set_red()
                self.yellow_circle.set_black()
                self.green_circle.set_black()
            case TrafficLightState.YELLOW:
                self.red_circle.set_black()
                self.yellow_circle.set_yellow()
                self.green_circle.set_black()
            case TrafficLightState.GREEN:
                self.red_circle.set_black()
                self.yellow_circle.set_black()
                self.green_circle.set_green()

    # def set_lights_with_direction(self, state: TrafficState) -> None:
    #     if self.direction is TrafficLightDirection.NORTH_SOUTH
    @pyqtSlot(TrafficState)
    def update_state(self, state: TrafficState) -> None:
        print(state)
        self.green_circle.set_green()
        # match state:
        #     case TrafficState.NORTH_SOUTH_LEFT:
        #         if self.direction is TrafficLightDirection.NORTH_SOUTH:
        #             self.set_lights(TrafficLightState.GREEN)
        #         else:
        #             self.set_lights(TrafficLightState.RED)


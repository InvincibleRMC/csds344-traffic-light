import time

from PyQt6.QtCore import QSize, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow

from traffic_light import (TrafficLight, TrafficLightDirection,
                           TrafficLightState)
from traffic_state import TrafficState
from images import ImageLabel, ArrowsManager

HEIGHT = 600
WIDTH = 600


class BackgroundThread(QThread):
    current_state = pyqtSignal(TrafficState)
    state = TrafficState.EAST_WEST_LEFT

    def run(self) -> None:
        while True:
            self.current_state.emit(self.state)
            self.next_state()
            time.sleep(6)

    def next_state(self) -> None:
        match self.state:
            case TrafficState.EAST_WEST_LEFT:
                self.state = TrafficState.EAST_WEST_STRAIGHT
            case TrafficState.EAST_WEST_STRAIGHT:
                self.state = TrafficState.EAST_WEST_RIGHT
            case TrafficState.EAST_WEST_RIGHT:
                self.state = TrafficState.NORTH_SOUTH_LEFT
            case TrafficState.NORTH_SOUTH_LEFT:
                self.state = TrafficState.NORTH_SOUTH_STRAIGHT
            case TrafficState.NORTH_SOUTH_STRAIGHT:
                self.state = TrafficState.NORTH_SOUTH_RIGHT
            case TrafficState.NORTH_SOUTH_RIGHT:
                self.state = TrafficState.EAST_WEST_LEFT


class Window(QMainWindow):
    start = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSDS 344 Traffic Simulation")
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        self.background = ImageLabel("assets/intersection.png", parent=self)
        self.arrows = ArrowsManager(window=self)

        self.right_traffic_light = TrafficLight(TrafficLightDirection.EAST_WEST, parent=self)
        self.left_traffic_light = TrafficLight(TrafficLightDirection.EAST_WEST, parent=self)

        self.top_traffic_light = TrafficLight(TrafficLightDirection.NORTH_SOUTH, parent=self)
        self.bottom_traffic_light = TrafficLight(TrafficLightDirection.NORTH_SOUTH, parent=self)

        self.right_traffic_light.move(900, 450)
        self.left_traffic_light.move(300, 300)
        self.top_traffic_light.move(600, 700)
        self.bottom_traffic_light.move(600, 50)

        self.custom_thread = BackgroundThread()
        self.custom_thread.current_state.connect(self.update_all)
        self.custom_thread.start()

    def update_all(self, state: TrafficState) -> None:
        self.right_traffic_light.async_update_state(state)
        self.left_traffic_light.async_update_state(state)
        self.top_traffic_light.async_update_state(state)
        self.bottom_traffic_light.async_update_state(state)
        self.arrows.update_state(state)


app = QApplication([])

window = Window()
window.show()

app.exec()

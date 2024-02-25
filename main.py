import time

from PyQt6.QtCore import QSize, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow

from traffic_state import TrafficState
from images import ImageLabel, ArrowsManager, LightManager

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

        self.background = ImageLabel("assets/arrows/intersection.png", parent=self)
        self.arrows = ArrowsManager(window=self)
        self.lights = LightManager(window=self)

        self.custom_thread = BackgroundThread()
        self.custom_thread.current_state.connect(self.update_all)
        self.custom_thread.start()

    def update_all(self, state: TrafficState) -> None:
        self.arrows.update_state(state)
        self.lights.update_state(state)


app = QApplication([])

window = Window()
window.show()

app.exec()

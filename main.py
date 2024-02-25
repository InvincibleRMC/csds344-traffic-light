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
        time.sleep(3)
        while True:
            self.current_state.emit(self.state)
            self.next_state()
            # green 4 sec, yellow 1 sec, red 1 sec
            if self.current_state % 3 == 0:
                time.sleep(4)
            elif self.current_state % 3 == 1:
                time.sleep(1.5)
            else:
                time.sleep(0.5)

    def next_state(self) -> None:
        self.state = (self.state + 1) % 18
        # match self.state:
        #     case TrafficState.EAST_WEST_LEFT_GREEN:
        #         self.state = TrafficState.EAST_WEST_LEFT_YELLOW
        #     case TrafficState.EAST_WEST_LEFT_YELLOW:
        #         self.state = TrafficState.EAST_WEST_LEFT_RED
        #     case TrafficState.EAST_WEST_LEFT_RED:
        #         self.state = TrafficState.EAST_WEST_STRAIGHT_GREEN
        #     case TrafficState.EAST_WEST_STRAIGHT_GREEN:
        #         self.state = TrafficState.EAST_WEST_STRAIGHT_YELLOW
        #     case TrafficState.EAST_WEST_STRAIGHT_YELLOW:
        #         self.state = TrafficState.EAST_WEST_STRAIGHT_RED
        #     case TrafficState.EAST_WEST_STRAIGHT_RED:        
        #         self.state = TrafficState.EAST_WEST_RIGHT_GREEN
        #     case TrafficState.EAST_WEST_RIGHT_GREEN:
        #         self.state = TrafficState.EAST_WEST_RIGHT_YELLOW
        #     case TrafficState.EAST_WEST_RIGHT_YELLOW:
        #         self.state = TrafficState.EAST_WEST_RIGHT_RED
        #     case TrafficState.EAST_WEST_RIGHT_RED:
        #         self.state = TrafficState.NORTH_SOUTH_LEFT_GREEN
        #     case TrafficState.NORTH_SOUTH_LEFT_GREEN:
        #         self.state = TrafficState.NORTH_SOUTH_LEFT_YELLOW
        #     case TrafficState.NORTH_SOUTH_LEFT_YELLOW:
        #         self.state = TrafficState.NORTH_SOUTH_LEFT_RED
        #     case TrafficState.NORTH_SOUTH_LEFT_RED:
        #         self.state = TrafficState.NORTH_SOUTH_STRAIGHT_GREEN
        #     case TrafficState.NORTH_SOUTH_STRAIGHT_GREEN:
        #         self.state = TrafficState.NORTH_SOUTH_STRAIGHT_YELLOW
        #     case TrafficState.NORTH_SOUTH_STRAIGHT_YELLOW:
        #         self.state = TrafficState.NORTH_SOUTH_STRAIGHT_RED
        #     case TrafficState.NORTH_SOUTH_STRAIGHT_RED:
        #         self.state = TrafficState.NORTH_SOUTH_RIGHT_GREEN
        #     case TrafficState.NORTH_SOUTH_RIGHT_GREEN:
        #         self.state = TrafficState.NORTH_SOUTH_RIGHT_YELLOW
        #     case TrafficState.NORTH_SOUTH_RIGHT_YELLOW:
        #         self.state = TrafficState.NORTH_SOUTH_RIGHT_RED
        #     case TrafficState.NORTH_SOUTH_RIGHT_RED:
        #         self.state = TrafficState.EAST_WEST_LEFT_GREEN


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

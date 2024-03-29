import signal
import time

from PyQt6.QtCore import QSize, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow

from images import ArrowsManager, ImageLabel, LightManager
from traffic_state import TrafficState

HEIGHT = 600
WIDTH = 600


class BackgroundThread(QThread):
    current_state = pyqtSignal(int)
    state = TrafficState.NORTH_SOUTH_LEFT_GREEN.value

    def run(self) -> None:
        while True:
            self.current_state.emit(self.state)
            self.next_state()
            # green 5 sec, yellow 2 sec, red 1 sec
            if self.state % 3 == 0:
                # Red duration
                time.sleep(1)
            elif self.state % 3 == 1:
                # Green duration
                time.sleep(5)
            else:
                # Yellow duration
                time.sleep(2)

    def next_state(self) -> None:
        self.state = (self.state + 1) % 18


class Window(QMainWindow):
    start = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("CSDS 344 Traffic Simulation")
        self.setFixedSize(QSize(WIDTH, HEIGHT))

        self.background = ImageLabel("assets/arrows/intersection.png", parent=self)
        self.arrows = ArrowsManager(window=self)
        self.lights = LightManager(window=self)

        self.custom_thread = BackgroundThread()
        self.custom_thread.current_state.connect(self.update_all)
        self.custom_thread.start()

    def update_all(self, state: int) -> None:
        state = TrafficState(state)
        self.arrows.update_state(state)
        self.lights.update_state(state)


# Kills with Control + C
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication([])

window = Window()
window.show()

app.exec()

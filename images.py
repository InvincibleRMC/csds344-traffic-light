from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QWidget, QLabel

from traffic_state import TrafficState


class ImageLabel(QLabel):
    def __init__(self, img_path: str, parent: QWidget, rot: float = 0) -> None:
        super().__init__(parent=parent)

        self.img = QPixmap(img_path)
        self.setPixmap(self.img.transformed(QTransform().rotate(rot)))
        self.move(0, 0)
        self.resize(self.img.width(), self.img.height())


class ArrowsManager:
    def __init__(self, window: QWidget):
        self.state_arrows = {
            TrafficState.EAST_WEST_LEFT: [
                ImageLabel("assets/car_left.png", parent=window, rot=90),
                ImageLabel("assets/car_left.png", parent=window, rot=270)
            ],
            TrafficState.NORTH_SOUTH_LEFT: [
                ImageLabel("assets/car_left.png", parent=window, rot=0),
                ImageLabel("assets/car_left.png", parent=window, rot=180)
            ],
        }

    def update_state(self, new_state: TrafficState) -> None:
        for state in self.state_arrows.keys():
            for arrow in self.state_arrows[state]:
                if state == new_state:
                    arrow.show()
                else:
                    arrow.hide()
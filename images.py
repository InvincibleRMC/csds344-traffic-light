import time

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


class LightManager:
    def __init__(self, window: QWidget):
        self.state_arrows = {
            TrafficState.EAST_WEST_LEFT: [
                ImageLabel("assets/traffic_lights/green_left.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/green_left.png", parent=window, rot=270),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=180)
            ],
            TrafficState.EAST_WEST_STRAIGHT: [
                ImageLabel("assets/traffic_lights/green.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/green.png", parent=window, rot=270),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=180)
            ],
            TrafficState.EAST_WEST_RIGHT: [
                ImageLabel("assets/traffic_lights/green_right.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/green_right.png", parent=window, rot=270),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=180)
            ],
            TrafficState.NORTH_SOUTH_LEFT: [
                ImageLabel("assets/traffic_lights/green_left.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/green_left.png", parent=window, rot=180),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=270)
            ],
            TrafficState.NORTH_SOUTH_STRAIGHT: [
                ImageLabel("assets/traffic_lights/green.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/green.png", parent=window, rot=180),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=270)
            ],
            TrafficState.NORTH_SOUTH_RIGHT: [
                ImageLabel("assets/traffic_lights/green_right.png", parent=window, rot=0),
                ImageLabel("assets/traffic_lights/green_right.png", parent=window, rot=180),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=90),
                ImageLabel("assets/traffic_lights/red.png", parent=window, rot=270)
            ],
        }
        self.foo = ImageLabel("assets/traffic_lights/yellow.png", parent=window, rot=0)
        self.foo2 = ImageLabel("assets/traffic_lights/yellow.png", parent=window, rot=180)
        self.bar = ImageLabel("assets/traffic_lights/yellow.png", parent=window, rot=90)
        self.bar2 = ImageLabel("assets/traffic_lights/yellow.png", parent=window, rot=270)
        self.foo.hide()
        self.foo2.hide()
        self.bar.hide()
        self.bar2.hide()

    def update_state(self, new_state: TrafficState) -> None:
        time.sleep(1)
        for state, light_list in self.state_arrows.items():
            for light in light_list:
                if state == new_state:
                    light.show()
                else:
                    light.hide()

        time.sleep(1)
        # for state, light_list in self.state_arrows.items():
        #     for light in light_list:
        #         if state == new_state:
        #             light.hide()

        NORTH_SOUTH = [TrafficState.NORTH_SOUTH_LEFT, TrafficState.NORTH_SOUTH_STRAIGHT, TrafficState.NORTH_SOUTH_RIGHT]
        EAST_WEST = [TrafficState.EAST_WEST_LEFT, TrafficState.EAST_WEST_STRAIGHT, TrafficState.EAST_WEST_RIGHT]

        if new_state in NORTH_SOUTH:
            # foo = 
            self.foo.show()
            # foo2 = 
            self.foo2.show()
        else:
            # bar = 
            self.bar.show()
            
            self.bar2.show()

        time.sleep(1)

        if new_state in NORTH_SOUTH:
            self.foo.hide()
            self.foo2.hide()
            # ImageLabel("assets/traffic_lights/red.png", parent=self.window, rot=0).show()
            # ImageLabel("assets/traffic_lights/red.png", parent=self.window, rot=180).show()
        else:
            self.bar.hide()
            self.bar2.hide()
            # ImageLabel("assets/traffic_lights/red.png", parent=self.window, rot=90).show()
            # ImageLabel("assets/traffic_lights/red.png", parent=self.window, rot=270).show()

        time.sleep(1)


class ArrowsManager:
    def __init__(self, window: QWidget):
        self.state_arrows = {
            TrafficState.EAST_WEST_LEFT: [
                ImageLabel("assets/arrows/car_left.png", parent=window, rot=90),
                ImageLabel("assets/arrows/car_left.png", parent=window, rot=270)
            ],
            TrafficState.EAST_WEST_STRAIGHT: [
                ImageLabel("assets/arrows/car_straight.png", parent=window, rot=90),
                ImageLabel("assets/arrows/car_straight.png", parent=window, rot=270),
                ImageLabel("assets/arrows/pedestrian.png", parent=window, rot=0),
                ImageLabel("assets/arrows/pedestrian.png", parent=window, rot=180)
            ],
            TrafficState.EAST_WEST_RIGHT: [
                ImageLabel("assets/arrows/car_right.png", parent=window, rot=90),
                ImageLabel("assets/arrows/car_right.png", parent=window, rot=270)
            ],
            TrafficState.NORTH_SOUTH_LEFT: [
                ImageLabel("assets/arrows/car_left.png", parent=window, rot=0),
                ImageLabel("assets/arrows/car_left.png", parent=window, rot=180)
            ],
            TrafficState.NORTH_SOUTH_STRAIGHT: [
                ImageLabel("assets/arrows/car_straight.png", parent=window, rot=0),
                ImageLabel("assets/arrows/car_straight.png", parent=window, rot=180),
                ImageLabel("assets/arrows/pedestrian.png", parent=window, rot=90),
                ImageLabel("assets/arrows/pedestrian.png", parent=window, rot=270)
            ],
            TrafficState.NORTH_SOUTH_RIGHT: [
                ImageLabel("assets/arrows/car_right.png", parent=window, rot=0),
                ImageLabel("assets/arrows/car_right.png", parent=window, rot=180)
            ],
        }

    def update_state(self, new_state: TrafficState) -> None:
        for state, arrow_list in self.state_arrows.items():
            for arrow in arrow_list:
                if state == new_state:
                    arrow.show()
                else:
                    arrow.hide()

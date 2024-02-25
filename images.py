import time
import typing as t

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


class TrafficLight:
    def __init__(self, parent: QWidget, rot: float, north_south: bool) -> None:
        self.red = ImageLabel("assets/traffic_lights/red.png", parent=parent, rot=rot)
        self.yellow = ImageLabel("assets/traffic_lights/yellow.png", parent=parent, rot=rot)
        self.green = ImageLabel("assets/traffic_lights/green.png", parent=parent, rot=rot)
        self.green_left = ImageLabel("assets/traffic_lights/green_left.png", parent=parent, rot=rot)
        self.green_right = ImageLabel("assets/traffic_lights/green_right.png", parent=parent, rot=rot)

        self.all_images = [self.red, self.yellow, self.green, self.green_left, self.green_right]

        if north_south:
            self.straight_state = [TrafficState.NORTH_SOUTH_STRAIGHT_GREEN, TrafficState.NORTH_SOUTH_STRAIGHT_YELLOW, TrafficState.NORTH_SOUTH_STRAIGHT_RED]
            self.left_state = [TrafficState.NORTH_SOUTH_LEFT_GREEN, TrafficState.NORTH_SOUTH_LEFT_YELLOW, TrafficState.NORTH_SOUTH_LEFT_RED]
            self.right_state = [TrafficState.NORTH_SOUTH_RIGHT_GREEN, TrafficState.NORTH_SOUTH_RIGHT_YELLOW, TrafficState.NORTH_SOUTH_RIGHT_RED]
        else:
            self.straight_state = [TrafficState.EAST_WEST_STRAIGHT_GREEN, TrafficState.EAST_WEST_STRAIGHT_YELLOW, TrafficState.EAST_WEST_STRAIGHT_RED]
            self.left_state = [TrafficState.EAST_WEST_LEFT_GREEN, TrafficState.EAST_WEST_LEFT_YELLOW, TrafficState.EAST_WEST_LEFT_RED]
            self.right_state = [TrafficState.EAST_WEST_RIGHT_GREEN, TrafficState.EAST_WEST_RIGHT_YELLOW, TrafficState.EAST_WEST_RIGHT_RED]

    def set_image(self, image: ImageLabel):
        for img in self.all_images:
            if img == image:
                img.show()
            else:
                img.hide()

    def update_green(self, state: TrafficState):
        if state == self.straight_state:
            self.set_image(self.green)
        elif state == self.left_state:
            self.set_image(self.green_left)
        elif state == self.right_state:
            self.set_image(self.green_right)
        else:
            self.set_image(self.red)

    def update_yellow(self, state: TrafficState):
        if state in (self.straight_state, self.left_state, self.right_state):
            self.set_image(self.yellow)
        else:
            self.set_image(self.red)

    def update_red(self):
        self.set_image(self.red)


class LightManager:
    def __init__(self, window: QWidget):
        self.window = window

        self.traffic_lights = [
            TrafficLight(parent=window, rot=0, north_south=True),
            TrafficLight(parent=window, rot=90, north_south=False),
            TrafficLight(parent=window, rot=180, north_south=True),
            TrafficLight(parent=window, rot=270, north_south=False),
        ]

    def update_state(self, new_state: TrafficState) -> None:
        print(new_state)
        print("Green")
        for light in self.traffic_lights:
            light.update_green(new_state)

        # time.sleep(3)
        # print("Yellow")
        # for light in self.traffic_lights:
        #     light.update_yellow(new_state)
        #
        # time.sleep(2)
        # print("Red")
        # for light in self.traffic_lights:
        #     light.update_red()

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

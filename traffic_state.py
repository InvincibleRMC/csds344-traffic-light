from enum import IntEnum


class TrafficState(IntEnum):
    NORTH_SOUTH_LEFT = 0
    NORTH_SOUTH_RIGHT = 1
    NORTH_SOUTH_STRAIGHT = 2
    EAST_WEST_LEFT = 3
    EAST_WEST_RIGHT = 4
    EAST_WEST_STRAIGHT = 5

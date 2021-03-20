from __future__ import annotations

from enum import Enum


class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8

    X = LEFT | RIGHT
    Y = UP | DOWN

    ALL = X | Y

    def __and__(self, other: Move):
        return self.value & other.value

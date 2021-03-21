from __future__ import annotations

from .Board import Board
from .enum.Move import Move


class State:

    def __init__(self, board: Board, previousStep: Move = None, parent: State = None, epoch: int = 0):
        self.board = board
        self.previousStep = previousStep
        self.parent = parent
        self.epoch = epoch

        self.children = {}

    def __eq__(self, other: State) -> bool:
        return self.board == other.board

    def __hash__(self):
        return self.board.__hash__()

    def __str__(self):
        return self.epoch.__str__() + ' ' + self.board.__str__()

from __future__ import annotations

from .Board import Board
from .enum.Move import Move


class State:

    def __init__(self, board: Board, previousStep: str = None, parent: State = None, epoch: int = 0):
        self.epoch = epoch
        self.board = board
        self.previousStep = previousStep
        self.parent = parent
        self.children = []

    def calculateChildren(self, move: Move):
        for p in self.board.moveBy(move):
            self.children.append(State(p[0], p[1], self, self.epoch + 1))

    def __eq__(self, other: State) -> bool:
        return self.board == other.board

    def __hash__(self):
        return self.board.__hash__()

    def __str__(self):
        return self.epoch.__str__() + ' ' + self.board.__str__()

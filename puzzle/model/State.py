from __future__ import annotations

from .Board import Board
from puzzle.enum.Move import Move


class State:

    def __init__(self, board: Board, previousStep: Move = None, parent: State = None):
        self.board = board
        self.previousStep = previousStep
        self.parent = parent
        self.epoch = 0 if self.parent is None else self.parent.epoch + 1
        self.score = 0

        self.children = {}

    def __eq__(self, other: State) -> bool:
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        return f'epoch="{self.epoch}", board={self.board}, score={self.score}, prevStep={self.previousStep}'

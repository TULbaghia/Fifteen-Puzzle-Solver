from __future__ import annotations

from .Board import Board
from board.enum.Move import Move


class State:

    def __init__(self, board: Board, previousStep: Move = None, parent: State = None, epoch: int = 0):
        self.board = board
        self.previousStep = previousStep
        self.parent = parent
        self.epoch = epoch
        self.score = 0

        self.children = {}

    def __eq__(self, other: State) -> bool:
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        return f'{self.epoch}xx{self.board}'

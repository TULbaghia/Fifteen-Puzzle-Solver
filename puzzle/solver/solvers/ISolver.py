from abc import ABC

from puzzle.model.Board import Board
from puzzle.model.State import State


class ISolver(ABC):

    def solve(self, initialState: State, finalView: Board) -> State:
        raise NotImplementedError

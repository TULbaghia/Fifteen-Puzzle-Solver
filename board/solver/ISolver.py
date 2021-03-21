from abc import ABC

from board.model.Board import Board
from board.model.State import State


class ISolver(ABC):

    def solve(self, initialState: State, finalView: Board) -> State:
        raise NotImplementedError

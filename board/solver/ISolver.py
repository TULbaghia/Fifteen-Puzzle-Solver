from abc import ABC

from board.Board import Board
from board.MutableBoard import MutableBoard
from board.State import State
from board.enum.Move import Move


class ISolver(ABC):

    def solve(self, initialState: State, finalView: Board) -> State:
        raise NotImplementedError

    def mutateBoard(self, state: State):
        MutableBoard.mutate(state, Move.ALL)

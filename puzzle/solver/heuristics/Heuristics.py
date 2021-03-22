from puzzle.model.Board import Board
from puzzle.model.State import State


class Heuristics(object):

    @staticmethod
    def hamming(candidate: State, finalView: Board) -> int:
        res = 0
        candidate = candidate.board.getBoard()
        finalView = finalView.getBoard()
        for i in range(len(candidate)):
            if candidate[i] != 0 and candidate[i] != finalView[i]:
                res += 1
        return res

    """
    TODO: Sprawdzić czy liczy dobrze x, y
    """
    @staticmethod
    def manhattan(candidate: State, finalView: Board) -> int:
        res = 0
        candidate = candidate.board
        finalView = finalView.getBoard()
        for i in range(len(candidate.getBoard())):
            if candidate.getBoard()[i] != 0 and candidate.getBoard()[i] != finalView[i]:
                ci = finalView.index(candidate.getBoard()[i])
                y = (i // candidate.row) - (ci // candidate.row)
                x = (i % candidate.col) - (ci % candidate.col)
                res += abs(y) + abs(x)
        return res
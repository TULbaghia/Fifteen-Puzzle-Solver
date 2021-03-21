from __future__ import annotations


class Board(object):

    def __init__(self, board: tuple):
        self.__board = tuple(board)
        self.__emptyIndex = self.__board.index(0)

    def getBoard(self) -> tuple:
        return self.__board

    def getEmptyIndex(self) -> int:
        return self.__emptyIndex

    def __eq__(self, other: Board):
        return self.__board == other.__board

    def __hash__(self):
        return self.__board.__hash__()

    def __str__(self):
        return self.__board.__str__()

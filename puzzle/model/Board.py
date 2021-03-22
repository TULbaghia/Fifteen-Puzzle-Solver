from __future__ import annotations


class Board(object):

    def __init__(self, board: tuple, col: int, row: int):
        self.__board = tuple(board)
        self.__col = col
        self.__row = row
        self.__emptyIndex = self.__board.index(0)
        self.__hash = hash((self.__col, self.__row, self.__board))

    def getBoard(self) -> tuple:
        return self.__board

    def getEmptyIndex(self) -> int:
        return self.__emptyIndex

    def getCol(self):
        return self.__col

    def getRow(self):
        return self.__row

    def __eq__(self, other: Board):
        return self.__hash == other.__hash

    def __hash__(self):
        return self.__hash

    def __str__(self):
        b = '('
        lastR = 0
        for i in range(len(self.__board)):
            c = i % self.__col
            r = i // self.__col
            if lastR != r:
                b = b[:-2]
                b += '), ('
                lastR = r
            b += str(self.__board[i]) + ', '
        b = b[:-2] + ")"
        return f'({b})'

from __future__ import annotations


class Board(object):

    def __init__(self, board: tuple, col: int, row: int):
        self.__board = tuple(board)
        self.col = col
        self.row = row
        self.__emptyIndex = self.__board.index(0)

    def getBoard(self) -> tuple:
        return self.__board

    def getEmptyIndex(self) -> int:
        return self.__emptyIndex

    def __eq__(self, other: Board):
        return self.__board == other.__board and self.col == other.col and self.row == other.row

    def __hash__(self):
        return hash((self.col, self.row, self.__board))

    def __str__(self):
        b = '('
        lastR = 0
        for i in range(len(self.__board)):
            c = i % self.col
            r = (i - c) / self.col
            if lastR != r:
                b = b[:-2]
                b += '), ('
                lastR = r
            b += str(self.__board[i]) + ', '
        b = b[:-2] + ")"
        return f'({b})'

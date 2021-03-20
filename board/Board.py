from __future__ import annotations
from typing import Union

from board.enum.Move import Move
from board.exception import NoEmptyIndexInBoardException

"""
TODO: Zmienic rozmiar tablicy
"""


class Board(object):

    def __init__(self, board):
        self.__board = tuple(board)
        self.__emptyIndex = self.getEmptyIndex()

    def getEmptyIndex(self) -> int:
        for i in range(len(self.__board)):
            if self.__board[i] == 0:
                return i
        raise NoEmptyIndexInBoardException

    def getBoardCopy(self) -> []:
        return list(self.__board)

    def __getSwappedBoard(self, x, y) -> Board:
        board = self.getBoardCopy()
        board[x], board[y] = board[y], board[x]
        return Board(board)

    def __moveUp(self) -> Union[None, Board]:
        if self.__emptyIndex in range(0, 5):
            return
        return self.__getSwappedBoard(self.__emptyIndex - 4, self.__emptyIndex)

    def __moveDown(self) -> Union[None, Board]:
        if self.__emptyIndex in range(12, 16):
            return
        return self.__getSwappedBoard(self.__emptyIndex + 4, self.__emptyIndex)

    def __moveLeft(self) -> Union[None, Board]:
        if self.__emptyIndex == 0 or self.__emptyIndex % 4 == 0:
            return
        return self.__getSwappedBoard(self.__emptyIndex - 1, self.__emptyIndex)

    def __moveRight(self) -> Union[None, Board]:
        if self.__emptyIndex % 3 == 0:
            return
        return self.__getSwappedBoard(self.__emptyIndex + 1, self.__emptyIndex)

    def moveBy(self, moveEnum: Move) -> []:
        moves = []

        if moveEnum & Move.UP:
            move = self.__moveUp()
            if move is not None:
                moves.append((move, Move.UP))

        if moveEnum & Move.DOWN:
            move = self.__moveDown()
            if move is not None:
                moves.append((move, Move.DOWN))

        if moveEnum & Move.LEFT:
            move = self.__moveLeft()
            if move is not None:
                moves.append((move, Move.LEFT))

        if moveEnum & Move.RIGHT:
            move = self.__moveRight()
            if move is not None:
                moves.append((move, Move.RIGHT))

        return moves

    def __eq__(self, other: Board):
        return self.__board == other.__board

    def __hash__(self):
        return self.__board.__hash__()

    def __str__(self):
        return self.__board.__str__()

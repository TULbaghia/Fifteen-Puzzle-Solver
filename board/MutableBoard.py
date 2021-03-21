from typing import Union

from board.Board import Board
from board.State import State
from board.enum.Move import Move


class MutableBoard(object):

    @staticmethod
    def __getSwappedBoard(board: Board, x, y) -> Board:
        board = list(board.getBoard())
        board[x], board[y] = board[y], board[x]
        return Board(tuple(board))

    @staticmethod
    def __moveUp(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() in range(0, 5):
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() - 4, board.getEmptyIndex())

    @staticmethod
    def __moveDown(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() in range(12, 16):
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() + 4, board.getEmptyIndex())

    @staticmethod
    def __moveLeft(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() == 0 or board.getEmptyIndex() % 4 == 0:
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() - 1, board.getEmptyIndex())

    @staticmethod
    def __moveRight(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() % 3 == 0:
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() + 1, board.getEmptyIndex())

    @staticmethod
    def mutate(state: State, moveEnum: Move):
        moves = []

        if moveEnum & Move.UP:
            move = MutableBoard.__moveUp(state.board)
            if move is not None:
                moves.append((move, Move.UP))

        if moveEnum & Move.DOWN:
            move = MutableBoard.__moveDown(state.board)
            if move is not None:
                moves.append((move, Move.DOWN))

        if moveEnum & Move.LEFT:
            move = MutableBoard.__moveLeft(state.board)
            if move is not None:
                moves.append((move, Move.LEFT))

        if moveEnum & Move.RIGHT:
            move = MutableBoard.__moveRight(state.board)
            if move is not None:
                moves.append((move, Move.RIGHT))

        for (board, move) in moves:
            state.children[move] = State(board, move, state, state.epoch + 1)

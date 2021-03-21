from typing import Union

from board.model.Board import Board
from board.model.State import State
from board.enum.Move import Move


class MutableBoard(object):

    @staticmethod
    def __getSwappedBoard(board: Board, x, y) -> Board:
        boardx = list(board.getBoard())
        boardx[x], boardx[y] = boardx[y], boardx[x]
        return Board(tuple(boardx), board.col, board.row)

    @staticmethod
    def __moveUp(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() < board.col - 1:
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() - board.col, board.getEmptyIndex())

    @staticmethod
    def __moveDown(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() > len(board.getBoard()) - board.col - 1:
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() + board.col, board.getEmptyIndex())

    @staticmethod
    def __moveLeft(board: Board) -> Union[None, Board]:
        if board.getEmptyIndex() % board.col == 0:
            return
        return MutableBoard.__getSwappedBoard(board, board.getEmptyIndex() - 1, board.getEmptyIndex())

    @staticmethod
    def __moveRight(board: Board) -> Union[None, Board]:
        if (board.getEmptyIndex() + 1) % board.col == 0:
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

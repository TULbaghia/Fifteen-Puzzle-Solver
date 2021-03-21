import re
from queue import LifoQueue

from board.model.Board import Board
from board.MutableBoard import MutableBoard
from board.model.State import State
from board.enum.Move import Move
from board.solver.ISolver import ISolver


class DfsSolver(ISolver):
    RECURSION_LIMIT = 20

    def __init__(self, searchOrder: str):
        if not re.match("^[URDL]{4}$", searchOrder) or len(set(searchOrder)) != 4:
            raise AttributeError(f'{searchOrder} is invalid')
        searchList = []
        for i in searchOrder:
            searchList.append({'U': Move.UP, 'D': Move.DOWN, 'L': Move.LEFT, 'R': Move.RIGHT}[i])
        self.searchOrder = tuple(searchList)

    def solve(self, initialState: State, finalView: Board) -> State:
        if initialState.board == finalView:
            return initialState
        toVisit = LifoQueue()
        toVisit.put_nowait(initialState)
        visited = set()
        while not toVisit.empty():
            state = toVisit.get_nowait()
            visited.add(state)

            if state.epoch < self.RECURSION_LIMIT:
                MutableBoard.mutate(state, Move.ALL)

                for order in self.searchOrder:
                    if state.children.get(order, None) is not None and state.children[order] not in visited \
                            and state.children[order] not in toVisit.queue:
                        if state.children[order].board == finalView:
                            return state.children[order]
                        toVisit.put_nowait(state.children[order])

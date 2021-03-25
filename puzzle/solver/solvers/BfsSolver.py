import re
from collections import deque

from puzzle.model.Board import Board
from puzzle.MutableBoard import MutableBoard
from puzzle.model.State import State
from puzzle.enum.Move import Move
from puzzle.solver.solvers.ISolver import ISolver


class BfsSolver(ISolver):

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
        toVisit = deque()
        toVisit.append(initialState)
        visited = set()

        while toVisit:
            state = toVisit.popleft()
            visited.add(state)
            MutableBoard.mutate(state, Move.ALL)

            for order in self.searchOrder:
                child = state.children.get(order, None)
                if child is not None and child not in visited and child not in toVisit:
                    if child.board == finalView:
                        return child
                    toVisit.append(child)

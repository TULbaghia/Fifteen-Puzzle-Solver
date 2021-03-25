import re
from queue import LifoQueue

from puzzle.model.Board import Board
from puzzle.MutableBoard import MutableBoard
from puzzle.model.Result import Result
from puzzle.model.State import State
from puzzle.enum.Move import Move
from puzzle.solver.solvers.ISolver import ISolver


class DfsSolver(ISolver):
    RECURSION_LIMIT = 20

    def __init__(self, searchOrder: str):
        self.maxDepth = 0
        if not re.match("^[URDL]{4}$", searchOrder) or len(set(searchOrder)) != 4:
            raise AttributeError(f'{searchOrder} is invalid')
        searchList = []
        for i in searchOrder:
            searchList.append({'U': Move.UP, 'D': Move.DOWN, 'L': Move.LEFT, 'R': Move.RIGHT}[i])
        self.searchOrder = tuple(searchList)

    def solve(self, initialState: State, finalView: Board) -> Result:
        result = Result()
        if initialState.board == finalView:
            result.finalState = initialState
            return result
        toVisit = LifoQueue()
        toVisit.put_nowait(initialState)
        visited = set()

        result.toVisit = toVisit
        result.visited = visited

        while not toVisit.empty():
            state = toVisit.get_nowait()
            visited.add(state)

            if state.epoch <= self.RECURSION_LIMIT:
                MutableBoard.mutate(state, Move.ALL)

                for order in self.searchOrder:
                    child = state.children.get(order, None)
                    if child is not None and child not in visited and child not in toVisit.queue:
                        if self.maxDepth < child.epoch:
                            self.maxDepth = child.epoch
                        if child.board == finalView:
                            result.maxDepth = self.maxDepth
                            result.finalState = child
                            return result
                        toVisit.put_nowait(child)

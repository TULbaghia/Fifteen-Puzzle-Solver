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
        self.searchOrder = tuple(searchList[::-1])

    def solve(self, initialState: State, finalView: Board) -> Result:
        if initialState.board == finalView:
            return Result(initialState)

        toVisit = LifoQueue()
        toVisit.put_nowait(initialState)
        visited = set()

        while not toVisit.empty():
            state = toVisit.get_nowait()
            visited.add(state)

            if state.epoch < self.RECURSION_LIMIT:
                MutableBoard.mutate(state, Move.ALL)

                for order in self.searchOrder:
                    child = state.children.get(order, None)
                    if child is not None:  # and self.shouldBeInserted(visited, toVisit, child):
                        if self.maxDepth < child.epoch:
                            self.maxDepth = child.epoch
                        if child.board == finalView:
                            return Result(child, self.maxDepth, toVisit.qsize(), len(visited))
                        toVisit.put_nowait(child)
        if toVisit.empty():
            return Result(None, self.maxDepth, 0, len(visited))

    def shouldBeInserted(self, visited, toVisit, state: State) -> bool:
        if state in visited:
            test = self.getEarliestEpochEqual(visited, state)
            if test is not None and test.epoch < state.epoch:
                visited.remove(test)
                return True
            else:
                return False

        # if state in toVisit.queue and self.getEarliestEpochEqual(toVisit.queue, state) < state:
        #     return False

        return True

    def getEarliestEpochEqual(self, collection, state) -> State:
        return min(collection, key=lambda x: x == state and x.epoch < state.epoch)

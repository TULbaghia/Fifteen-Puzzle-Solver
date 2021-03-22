from collections import deque
from typing import Callable

from puzzle.MutableBoard import MutableBoard
from puzzle.enum.Move import Move
from puzzle.model.Board import Board
from puzzle.model.State import State
from puzzle.solver.solvers.ISolver import ISolver


class AStarSolver(ISolver):

    def __init__(self, heuristics: Callable):
        self.heuristics = heuristics

    def solve(self, initialState: State, finalView: Board) -> State:
        if initialState.board == finalView:
            return initialState
        toVisit = deque([initialState])
        visited = set()

        while toVisit:
            toVisit = deque(sorted(toVisit, key=lambda item: item.score))

            state = toVisit.popleft()
            visited.add(state)
            MutableBoard.mutate(state, Move.ALL)

            for move in state.children:
                child = state.children[move]
                if child is not None and child not in visited and child not in toVisit:
                    if child.board == finalView:
                        return child
                    child.score = self.heuristics(child, finalView)
                    toVisit.append(child)

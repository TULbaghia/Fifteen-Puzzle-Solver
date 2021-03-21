from collections import deque

from board.MutableBoard import MutableBoard
from board.enum.Move import Move
from board.model.Board import Board
from board.model.State import State
from board.solver.ISolver import ISolver


class HammingAStrSolver(ISolver):

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
                    child.score = self.__getScore(child, finalView)
                    toVisit.append(child)

    def __getScore(self, candidate: State, finalView: Board) -> int:
        res = 0
        candidate = candidate.board.getBoard()
        finalView = finalView.getBoard()
        for i in range(len(candidate)):
            if candidate[i] != 0 and candidate[i] != finalView[i]:
                res += 1
        return res

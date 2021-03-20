from collections import deque

from board.State import State
from board.enum.Move import Move


class SolverBfs(object):

    def __init__(self, board: [], endBoard: []):
        self.rootState = State(board)
        self.endState = State(endBoard)

    def bfs(self) -> State:
        if self.rootState == self.endState:
            return self.rootState
        toVisit = deque([self.rootState])
        visited = set()
        while toVisit:
            state = toVisit.popleft()
            visited.add(state)
            state.calculateChildren(Move.ALL)
            for child in state.children:
                if child not in visited:
                    if child == self.endState:
                        return child
                    toVisit.append(child)

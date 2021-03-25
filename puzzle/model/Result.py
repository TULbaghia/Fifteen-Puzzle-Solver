from collections import deque
from queue import LifoQueue

from puzzle.model.State import State


class Result(object):
    def __init__(self, toVisit: deque = None, visited: set = None, finalState: State = None):
        self.maxDepth = 0
        self.toVisit = toVisit
        self.visited = visited
        self.finalState = finalState

    def getNumberOfVisitedStates(self):
        return len(self.visited)

    def getNumberOfProcessedStates(self):
        return len(self.visited) + len(list(self.toVisit))

    def printTreeForState(self):
        if self.finalState is not None:
            self.finalState.printTree()

from collections import deque
from queue import LifoQueue

from puzzle.model.State import State


class Result(object):
    def __init__(self, finalState: State = None, maxDepth: int = 0, numberOfStatesToVisit: int = 0,
                 numberOfVisitedStates: int = 0):
        self.maxDepth = maxDepth
        self.finalState = finalState
        self.numberOfStatesToVisit = numberOfStatesToVisit
        self.numberOfVisitedStates = numberOfVisitedStates

    def getNumberOfProcessedStates(self):
        return self.numberOfVisitedStates + self.numberOfStatesToVisit

    def printTreeForState(self):
        if self.finalState is not None:
            self.finalState.printTree()

from typing import Union

from board.solver.BfsSolver import BfsSolver
from board.solver.DfsSolver import DfsSolver
from board.solver.ISolver import ISolver


class SolverFactory(object):

    @staticmethod
    def createSolver(solver: str, arg: str) -> Union[ISolver]:
        if solver == 'bfs':
            return BfsSolver(arg)
        elif solver == 'dfs':
            return DfsSolver(arg)
        elif solver == 'astr':
            raise NotImplementedError
        else:
            raise NotImplementedError

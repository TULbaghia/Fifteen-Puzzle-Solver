from typing import Union

from puzzle.solver.solvers.AStarSolver import AStarSolver
from puzzle.solver.solvers.BfsSolver import BfsSolver
from puzzle.solver.solvers.DfsSolver import DfsSolver
from puzzle.solver.solvers.ISolver import ISolver
from puzzle.solver.heuristics.Heuristics import Heuristics


class SolverFactory(object):

    @staticmethod
    def createSolver(solver: str, arg: str) -> Union[ISolver]:
        if solver == 'bfs':
            return BfsSolver(arg)
        elif solver == 'dfs':
            return DfsSolver(arg)
        elif solver == 'astr' and arg == 'hamm':
            return AStarSolver(Heuristics.hamming)
        elif solver == 'astr' and arg == 'manh':
            return AStarSolver(Heuristics.manhattan)
        else:
            raise NotImplementedError

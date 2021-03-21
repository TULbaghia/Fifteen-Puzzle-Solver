from board.model.Board import Board
from board.model.State import State

from board.solver.SolverFactory import SolverFactory


def main():
    # arr = [1, 3, 0, 4, 5, 2, 6, 8, 9, 10, 7, 12, 13, 14, 11, 15]
    arr = (2, 5, 3, 4, 1, 10, 6, 8, 9, 14, 7, 12, 13, 0, 11, 15)

    solver = SolverFactory.createSolver('dfs', 'LRUD')
    solved = solver.solve(State(Board(arr)), Board((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)))

    while solved is not None:
        print(solved.__str__())
        solved = solved.parent


if __name__ == '__main__':
    main()

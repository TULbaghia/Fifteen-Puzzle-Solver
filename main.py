from random import shuffle

from puzzle.model.Board import Board
from puzzle.model.State import State

from puzzle.solver.SolverFactory import SolverFactory


def main():
    # arr = [1, 3, 0, 4, 5, 2, 6, 8, 9, 10, 7, 12, 13, 14, 11, 15]
    # arr = [2, 5, 3, 4, 1, 10, 6, 8, 9, 14, 7, 12, 13, 0, 11, 15]
    # arr = [2, 4, 0, 12, 1, 6, 7, 8, 5, 10, 3, 15, 9, 13, 14, 11]
    # # shuffle(arr)
    #
    # solver = SolverFactory.createSolver('astr', 'manh')
    # solved = solver.solve(State(Board(tuple(arr), 4, 4)), Board((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), 4, 4))

    arr = [1, 2, 3, 6, 9, 0, 4, 7, 5, 10, 8, 11]
    solver = SolverFactory.createSolver('astr', 'manh')
    solved = solver.solve(State(Board(tuple(arr), 3, 4)),
                          Board((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0), 3, 4))

    while solved is not None:
        print(str(solved))
        solved = solved.parent


if __name__ == '__main__':
    main()

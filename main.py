from board.Board import Board
from board.solver.SolverBfs import SolverBfs

import random


def main():
    # arr = [1, 3, 0, 4, 5, 2, 6, 8, 9, 10, 7, 12, 13, 14, 11, 15]
    arr = [2, 5, 3, 4, 1, 10, 6, 8, 9, 14, 7, 12, 13, 0, 11, 15]
    # random.shuffle(arr)
    solver = SolverBfs(Board(arr),
                       Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]))

    solved = solver.bfs()

    item = solved
    while item is not None:
        print(item.__str__())
        item = item.parent



if __name__ == '__main__':
    main()

from puzzle.file.FileWriter import FileWriter
from puzzle.model.Board import Board
from puzzle.model.State import State
from timeit import default_timer as timer

from puzzle.solver.SolverFactory import SolverFactory
from puzzle.file.FileReader import FileReader


def main():
    # arr = [1, 3, 0, 4, 5, 2, 6, 8, 9, 10, 7, 12, 13, 14, 11, 15]
    # arr = [2, 5, 3, 4, 1, 10, 6, 8, 9, 14, 7, 12, 13, 0, 11, 15]
    # arr = [2, 4, 0, 12, 1, 6, 7, 8, 5, 10, 3, 15, 9, 13, 14, 11]
    # shuffle(arr)
    #
    # solver = SolverFactory.createSolver('astr', 'manh')
    # start_time = time.time()
    # solved = solver.solve(State(Board(tuple(arr), 4, 4)),
    #                       Board((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0), 4, 4))
    # end_time = time.time()
    #
    # print(end_time - start_time)

    # arr = [1, 2, 3, 6, 9, 0, 4, 7, 5, 10, 8, 11]
    # solver = SolverFactory.createSolver('astr', 'manh')
    # solved = solver.solve(State(Board(tuple(arr), 3, 4)),
    #                       Board((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0), 3, 4))

    # arr = [1, 4, 8, 10, 13, 2, 9, 0, 7, 5, 6, 11, 3, 18, 15, 16, 17, 14, 19, 12]

    solver = SolverFactory.createSolver('astr', 'manh')

    start = timer()
    board, row, col, model_board = FileReader.readFile("initial_file.txt")

    solved = solver.solve(State(Board(tuple(board), row, col)),
                          Board(model_board, row, col))
    end = timer()
    timeInMillis = (end - start) * 1000
    print(timeInMillis)
    FileWriter.saveSolution("solved.txt", solved)
    FileWriter.saveStats("stats.txt", solved, round(timeInMillis, 3))


    # solved.printTreeForState()
    # print(solved.maxDepth)
    # print(solved.numberOfVisitedStates)
    # print(solved.numberOfStatesToVisit)
    # print(solved.getNumberOfProcessedStates())


if __name__ == '__main__':
    main()

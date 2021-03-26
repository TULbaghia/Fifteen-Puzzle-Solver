import argparse

from puzzle.file.FileWriter import FileWriter
from puzzle.model.Board import Board
from puzzle.model.Result import Result
from puzzle.model.State import State
from timeit import default_timer as timer

from puzzle.solver.CheckSolvable import CheckSolvable
from puzzle.solver.SolverFactory import SolverFactory
from puzzle.file.FileReader import FileReader

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Strategy, strategy parameter, initial file, solution file, "
                                                 "statistics file.")
    parser.add_argument('strategy')
    parser.add_argument('strategy_param')
    parser.add_argument('init_file')
    parser.add_argument('solution_file')
    parser.add_argument('stats_file')
    args = parser.parse_args()

    solver = SolverFactory.createSolver(args.strategy, args.strategy_param)
    board, row, col, model_board = FileReader.readFile(args.init_file)

    start = timer()
    if CheckSolvable.isSolvable(Board(tuple(board), row, col)):
        solved = solver.solve(State(Board(tuple(board), row, col)),
                              Board(model_board, row, col))
    else:
        solved = Result()
    end = timer()
    timeInMillis = (end - start) * 1000

    FileWriter.saveSolution(args.solution_file, solved)
    FileWriter.saveStats(args.stats_file, solved, round(timeInMillis, 3))

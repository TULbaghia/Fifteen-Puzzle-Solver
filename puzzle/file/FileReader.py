import numpy as np


def moveZero(arr):
    return [nonZero for nonZero in arr if nonZero != 0] + [zero for zero in arr if zero == 0]


class FileReader(object):

    @staticmethod
    def readFile(filePath) -> tuple:
        with open(filePath) as file:
            row, col = [int(number) for number in next(file).split()]
            board = np.array([[int(number) for number in line.split()] for line in file])
        return board.flatten(), row, col, moveZero(sorted(board.flatten()))

from puzzle.model.Board import Board


class CheckSolvable:

    # @staticmethod
    # def isSolvable(board: Board) -> bool:
    #     isColNumberEven = False if board.getCol() % 2 else True
    #
    #     zeroInEvenRow = False if ((len(board.getBoard()) - board.getEmptyIndex() - 1) // board.getCol()) % 2 else True
    #
    #     inversionCounter = 0
    #     for i in range(len(board.getBoard())):
    #         for j in range(i + 1, len(board.getBoard())):
    #             if board.getBoard()[j] != 0 and board.getBoard()[i] != 0 and board.getBoard()[i] > board.getBoard()[j]:
    #                 inversionCounter += 1
    #     isInversionEven = False if inversionCounter % 2 else True
    #
    #     if not isColNumberEven:
    #         return isInversionEven
    #     else:
    #         if zeroInEvenRow:
    #             return not isInversionEven
    #         else:
    #             return isInversionEven

    @staticmethod
    def isSolvable(board: Board) -> bool:
        parity = 0
        gridWidth = board.getCol()
        row = 0
        blankRow = 0

        for i in range(len(board.getBoard())):
            if i % gridWidth == 0:
                row += 1
            if board.getBoard()[i] == 0:
                blankRow = row
                continue
            for j in range(i + 1, len(board.getBoard())):
                if board.getBoard()[i] > board.getBoard()[j] and board.getBoard()[j] != 0:
                    parity += 1

        if gridWidth % 2 == 0:
            if blankRow % 2 == 0:
                return parity % 2 == 0
            else:
                return parity % 2 != 0
        else:
            return parity % 2 == 0
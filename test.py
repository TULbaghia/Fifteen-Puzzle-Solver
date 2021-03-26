from puzzle.model.Board import Board


def test():
    moves = 'DRDDLURULDDRULUURDDLURULDDRDRULDLURRDLLURULURDDLUURRDLLURDRURDLDRUULDRDLURDLUULLDDRULURRDDLURDLURRDLLDRUURDLULDRDLLUUURDDLDRRULLUURRRDDLLDRRULU'
    board = Board(tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]), 4, 4)

    for move in moves:
        print(str(board))
        bboard = list(board.getBoard())
        if move == 'D':
            bboard[board.getEmptyIndex()], bboard[board.getEmptyIndex() - board.getCol()] \
                = bboard[board.getEmptyIndex() - board.getCol()], bboard[board.getEmptyIndex()]
        elif move == 'U':
            bboard[board.getEmptyIndex()], bboard[board.getEmptyIndex() + board.getCol()] \
                = bboard[board.getEmptyIndex() + board.getCol()], bboard[board.getEmptyIndex()]
        elif move == 'R':
            bboard[board.getEmptyIndex()], bboard[board.getEmptyIndex() - 1] \
                = bboard[board.getEmptyIndex() - 1], bboard[board.getEmptyIndex()]
        elif move == 'L':
            bboard[board.getEmptyIndex()], bboard[board.getEmptyIndex() + 1] \
                = bboard[board.getEmptyIndex() + 1], bboard[board.getEmptyIndex()]
        else:
            pass
        board = Board(bboard, board.getCol(), board.getRow())


if __name__ == '__main__':
    test()

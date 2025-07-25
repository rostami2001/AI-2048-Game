from Board import Board
from Mode import Mode


class Action:

    @staticmethod
    def left(board: Board, mode: Mode):
        for i in range(board.height - 1):
            for j in range(board.width):
                if mode == Mode.Advance and board.gird[j][i] != board.gird[j][i + 1] and board.gird[j][i] != 0 and \
                        board.gird[j][i + 1] != 0:
                    continue
                board.gird[j][i] += board.gird[j][i + 1]
                board.gird[j][i + 1] = 0

    @staticmethod
    def right(board: Board, mode: Mode):
        for i in range(board.height - 1, 0, -1):
            for j in range(board.width):
                if mode == Mode.Advance and board.gird[j][i] != board.gird[j][i - 1] and board.gird[j][i] != 0 and \
                        board.gird[j][i - 1] != 0:
                    continue
                board.gird[j][i] += board.gird[j][i - 1]
                board.gird[j][i - 1] = 0

    @staticmethod
    def down(board: Board, mode: Mode):
        for i in range(board.width - 1, 0, -1):
            for j in range(board.height):
                if mode == Mode.Advance and board.gird[i][j] != board.gird[i - 1][j] and board.gird[i][j] != 0 and \
                        board.gird[i - 1][j] != 0:
                    continue
                board.gird[i][j] += board.gird[i - 1][j]
                board.gird[i - 1][j] = 0

    @staticmethod
    def up(board: Board, mode: Mode):
        for i in range(board.width - 1):
            for j in range(board.height - 1):
                if mode == Mode.Advance and board.gird[i][j] != board.gird[i + 1][j] and board.gird[i][j] != 0 and \
                        board.gird[i + 1][j] != 0:
                    continue
                board.gird[i][j] += board.gird[i + 1][j]
                board.gird[i + 1][j] = 0

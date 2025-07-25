from Board import Board
from Problem import Problem
from Mode import Mode
from State import State
from Search import Search

if __name__ == '__main__':
    test_path = './tests/6.txt'
    file = open(test_path, 'r')
    lines = [i.replace('\n', '') for i in file.readlines()]
    goal = int(lines[0])
    row, col = [int(i) for i in lines[1].split(' ')]
    arr = []
    for i in lines[2:]:
        arr.append([int(j) for j in i.split(' ')])
    # s = Search.bfs(Problem(State(Board(row, col, arr), None, 0, '',Mode.Advance), goal, Mode.Advance))
    # s = Search.dfs(Problem(State(Board(row, col, arr), None, 0, '', Mode.Advance), goal, Mode.Advance))
    # s = Search.gbfs(Problem(State(Board(row, col, arr), None, 0, '', Mode.Advance), goal, Mode.Advance))
    # s = Search.ids(Problem(State(Board(row, col, arr), None, 0, '', Mode.Advance), goal, Mode.Advance))
    # s = Search.astar(Problem(State(Board(row, col, arr), None, 0, '', Mode.Advance), goal, Mode.Advance))
    s = Search.idastar(Problem(State(Board(row, col, arr), None, 0, '', Mode.Advance), goal, Mode.Advance))
    s.print_path()

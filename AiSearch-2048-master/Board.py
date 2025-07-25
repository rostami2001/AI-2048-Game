from tabulate import tabulate


class Board:
    def __init__(self, width: int, height: int, gird: list):
        self.width = width
        self.height = height
        self.gird = gird

    def print_board(self):
        print(tabulate(self.gird, tablefmt="fancy_grid"))
        print()

    def __hash__(self):
        hash_string = ''
        for i in self.gird:
            for j in i:
                hash_string += str(j) + '###'
            hash_string += '$$$'
        return hash_string

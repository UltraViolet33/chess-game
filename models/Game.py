from . import Board


class Game:

    def __init__(self, board: Board) -> None:
        self.board = board


    def display_board(self)-> None:
        for i in range(len(self.board.board_array)):
            for j in range(len(self.board.board_array)):
                if j % 8 == 0:
                    print("\n")
                cell = self.board.board_array[i][j]
                cell.print_location()

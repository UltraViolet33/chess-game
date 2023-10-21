from . import Board


class Game:

    def __init__(self, board: Board) -> None:
        self.board = board


    def display_board(self)-> None:
        print(self.board.board_array)
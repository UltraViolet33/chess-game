from .Cell import Cell
from settings import INITIAL_BOARD


class Board:
    def __init__(self) -> None:
        self._board_array = self.init_board() 


    def init_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Cell(i, j, INITIAL_BOARD[i][j]))
            board.append(row)
        return board

    @property
    def board_array(self)-> list:
        return self._board_array
    
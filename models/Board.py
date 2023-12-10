from .Cell import Cell


class Board:
    def __init__(self) -> None:
        self._board_array = self.init_board() 




    def init_board(self):
        board = []
        for i in range(8):
            for j in range(8):
                board.append(Cell(i, j))
        return board

    @property
    def board_array(self)-> list:
        return self._board_array
    
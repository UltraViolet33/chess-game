from .Cell import Cell
from settings import *
import pygame as pg
from .Piece import Piece, Pawn


class Board:
    def __init__(self) -> None:
        self._board_array = self.init_board() 


    def init_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                x_start = 10 + j * CELL_SIZE
                y_start = 10 + i * CELL_SIZE
                rect = pg.Rect(x_start, y_start, CELL_SIZE, CELL_SIZE)

                piece_txt = INITIAL_BOARD[i][j]
                piece = None
                if piece_txt == 'B-P':
                    piece = Pawn('black')
                elif piece_txt == 'W-P':
                    piece = Pawn('white')

                row.append(Cell(j, i, INITIAL_BOARD[i][j], rect, piece))
            board.append(row)
        return board

    @property
    def board_array(self)-> list:
        return self._board_array


    def reset_cells(self, screen, font):
        for i in range(8):
            for j in range(8):
                cell = self.board_array[i][j]
                cell.reset(screen, font)

    def get_cells_from_locations(self, locations):
        cells = []
        print(locations)
        for i in range(8):
            for j in range(8):
                cell = self.board_array[i][j]
                for location in locations:
                    if cell.location.x == location.x and cell.location.y == location.y:
                        cells.append(cell)

        return cells
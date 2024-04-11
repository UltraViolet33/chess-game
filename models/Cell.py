from inspect import _void
import pygame as pg
from settings import *


class Location:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y



class Cell:
    def __init__(self, x: int, y:int, piece=None, rect=None) -> None:
        self.location = Location(x, y)
        self.piece = piece
        self.rect = rect
        x, y, w, h = rect 
        self.inner_rect = pg.Rect(x - CELL_BORDER_WIDTH, y - CELL_BORDER_WIDTH,
                                      w + 2 * CELL_BORDER_WIDTH, h + 2 * CELL_BORDER_WIDTH)


    def has_piece(self)-> bool:
        return self.piece

    def print_location(self):
        if self.has_piece():
            print(f"{self.piece}", end="")
        else:
            print("- ", end="")

    def focus(self, screen)->_void:
        pg.draw.rect(screen, (255, 255, 255), self.inner_rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect)

    def draw(self, screen, font)->_void:
        pg.draw.rect(screen, (255, 0, 0), self.inner_rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect)
        text_surface = font.render(self.piece, False, (255, 0, 0))
        screen.blit(text_surface, (self.rect.x ,self.rect.y))

    def reset(self, screen, font)->_void:
        pg.draw.rect(screen, (0, 0, 0), self.inner_rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect)
        self.draw(screen, font)

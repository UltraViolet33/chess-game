import pygame as pg
import sys
from settings import *
from models.Game import Game

class GameController:
    def __init__(self, game:Game):
        self.game = game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.font.init()
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        self.next_is_move = False
        self.active_cell = None

    def update(self):
        pg.display.flip()

    def draw(self):
        for i in range(8):
            for j in range(8):
                cell = self.game.board.board_array[i][j]
                cell.draw(self.screen, self.font)
                self.update()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            for i in range(8):
                for j in range(8):
                    cell = self.game.board.board_array[i][j]

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if cell.rect.collidepoint(event.pos):
                                print('clicked  ' + cell.piece)
                                print(self.next_is_move)
                                # first click to select the piece
                                if not self.next_is_move:
                                    self.game.board.reset_cells(self.screen, self.font)
                                    possible_moves = cell.focus(self.screen, self.font)
                                    self.active_cell = cell 
                                    if possible_moves:
                                        self.next_is_move = True
                                        possibles_moves_cells = self.game.board.get_cells_from_locations(possible_moves)
                                        print(possibles_moves_cells)

                                        for cell in possibles_moves_cells:
                                            cell.focus_possible_move(self.screen)
                                #second click to move the piece
                                else:
                                    print('move piece')
                                    cell.piece = self.active_cell.piece
                                    self.active_cell.piece = None
                                    self.game.board.reset_cells(self.screen, self.font)
                                    self.next_is_move = False
                                    self.active_cell = None



    def run(self):
        self.draw()
        while True:
            self.check_events()
            self.update()
            self.clock.tick(FPS)
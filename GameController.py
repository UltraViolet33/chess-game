import pygame as pg
import sys
from settings import *
from models.Game import Game

BLACK ='black'
WHITE = 'white'

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
        self.player_turn = WHITE
        self.possible_moves = []
        self.possibles_eats = []

    def get_next_player_turn(self):
        if self.player_turn == WHITE:
            return BLACK
        return WHITE

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
                                         # first click to select the piece
                                
                                # if not self.next_is_move:
                                #     if cell.piece_obj.color == self.player_turn:
                                #         self.game.board.reset_cells(self.screen, self.font)
                                #         possible_moves = cell.focus(self.screen, self.font)
                                #         self.active_cell = cell 
                                #         if possible_moves:
                                #             self.next_is_move = True
                                #             possibles_moves_cells = self.game.board.get_cells_from_locations(possible_moves)
                                #             print(possibles_moves_cells)

                                #             for cell in possibles_moves_cells:
                                #                 cell.focus_possible_move(self.screen)
                                # #second click to move the piece
                                # else:
                                #     print('move piece')
                                #     cell.piece = self.active_cell.piece
                                #     self.active_cell.piece = None
                                #     self.game.board.reset_cells(self.screen, self.font)
                                #     self.next_is_move = False
                                #     self.active_cell = None

                            # if not self.next_is_move:
                            #     if cell.piece_obj.color == self.player_turn:
                            #         self.game.board.reset_cells(self.screen, self.font)
                            #         possible_moves = cell.focus(self.screen, self.font)
                            #         self.active_cell = cell 
                            #         if possible_moves:
                            #             self.next_is_move = True
                            #             possibles_moves_cells = self.game.board.get_cells_from_locations(possible_moves)
                            #             print(possibles_moves_cells)

                            #             for cell in possibles_moves_cells:
                            #                 cell.focus_possible_move(self.screen)
                            # #second click to move the piece
                            # else:
                            #     print('move piece')
                            #     cell.piece = self.active_cell.piece
                            #     self.active_cell.piece = None
                            #     self.game.board.reset_cells(self.screen, self.font)
                            #     self.next_is_move = False
                            #     self.active_cell = None
                             
                     
                                self.game.board.reset_cells(self.screen, self.font)
                                if self.active_cell and self.possible_moves  and (cell.is_in_locations(self.possible_moves) or cell.is_in_locations(self.possible_eats)):
                                    #move the piece
                                    print('move')
                                    cell.piece = self.active_cell.piece
                                    cell.piece_obj = self.active_cell.piece_obj
                                    self.active_cell.piece = None
                                    # self.active_cell.draw(self.screen, self.font)
                                    # cell.draw(self.screen, self.font)
                                    self.game.board.reset_cells(self.screen, self.font)
                                    # self.update()
                                    # self.draw()
                                    self.active_cell = None
                                    self.possible_moves = None
                                    self.player_turn = self.get_next_player_turn()
                                elif cell.is_empty():
                                    #click on an empty cell
                                    pass 
                                elif cell.piece_obj.color != self.player_turn:
                                   pass
                                else:
                                    # display possible moves
                                    self.game.board.reset_cells(self.screen, self.font)
                                    [possible_moves, possible_eats] = cell.focus(self.screen, self.font, self.game.board)
                                    if possible_moves:
                                        possibles_moves_cells = self.game.board.get_cells_from_locations(possible_moves)
                                        self.active_cell = cell
                                        self.possible_moves = possible_moves
                                        for cell in possibles_moves_cells:
                                            cell.focus_possible_move(self.screen)
                                    if possible_eats:
                                        possibles_eats_cells = self.game.board.get_cells_from_locations(possible_eats)
                                        # self.active_cell = cell
                                        self.possible_eats = possible_eats
                                        for cell in possibles_eats_cells:
                                            cell.focus_possible_eats(self.screen, self.font)
                                    else:
                                        pass     
    def run(self):
        self.draw()
        while True:
            self.check_events()
            self.update()
            self.clock.tick(FPS)
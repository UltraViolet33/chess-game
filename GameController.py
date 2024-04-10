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

    def update(self):
        pg.display.flip()

    def draw(self):
        line_color = (255, 0, 0)

        x_start = 10
        x_end = WIDTH - 10
        y_start = 10
        y_end = y_start

        for row in self.game.board.board_array:
            pg.draw.line(self.screen, line_color, (x_start, y_start), (x_end, y_end))
            y_start += CELL_SIZE
            y_end = y_start
            self.update()

        x_start = 10
        x_end = 10
        y_start = 10
        y_end = HEIGHT - 10
        
        for row in self.game.board.board_array:
            pg.draw.line(self.screen, line_color, (x_start, y_start), (x_end, y_end))
            x_start += CELL_SIZE
            x_end = x_start
            self.update()

        pg.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        my_font = pg.font.SysFont('Comic Sans MS', 30)


        for i in range(8):
            for j in range(8):
                cell = self.game.board.board_array[i][j]
                print(cell.piece)
                text_surface = my_font.render(cell.piece, False, (255, 0, 0))
                self.screen.blit(text_surface, (CELL_SIZE * j,CELL_SIZE * i))
                self.update()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            line_color = (255, 0, 0)

            for i in range(8):
                for j in range(8):
                    cell = self.game.board.board_array[i][j]
                    x_start = 10 + j * CELL_SIZE
                    y_start = 10 + i * CELL_SIZE


                    area = pg.Rect(x_start, y_start, CELL_SIZE, CELL_SIZE)
                    color = (255,0,0)

                    if event.type == pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if area.collidepoint(event.pos):
                                print('clicked  ' + cell.piece)



    def run(self):
        self.draw()
        while True:
            self.check_events()
            self.update()
            self.clock.tick(FPS)
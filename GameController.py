import pygame as pg
import sys
from settings import *
from models.Game import Game

class GameController:
    def __init__(self, game:Game):
        self.game = game
        pass

        # pg.init()
        # self.screen = pg.display.set_mode(RES)
        # self.clock = pg.time.Clock()

    def update(self):
        pg.display.flip()

    def draw(self):
        pass

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        self.game.display_board()
        # while True:
        #     self.check_events()
        #     self.update()
        #     self.clock.tick(FPS)
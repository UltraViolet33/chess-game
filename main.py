from GameController import GameController
from models.Game import Game
from models.Board import Board

if __name__ == "__main__":
    board = Board()
    game = Game(board)
    gameController = GameController(game)
    gameController.run()
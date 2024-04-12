from models.Cell import Location


class Piece:
    def __init__(self, color) -> None:
        self.color = color
        self.BLACK ='black'
        self.WHITE = 'white'


class Pawn(Piece):

    def print(self):
        return f"pawn-{self.color}"

    def get_possible_moves(self, location):
        print(location.x)
        print(location.y)
        possible_moves = []
        if self.color == self.WHITE:
            possible_moves.append(Location(location.x, location.y - 1))
            possible_moves.append(Location(location.x, location.y - 2))

        return possible_moves
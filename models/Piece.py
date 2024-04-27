from models.Cell import Location


class Piece:
    def print(self):
        return f"pawn-{self.color}"
    
    def __init__(self, color) -> None:
        self.color = color
        self.BLACK ='black'
        self.WHITE = 'white'


class Pawn(Piece):
    def get_possible_moves(self, location):
        print(location.x)
        print(location.y)
        possible_moves = []
        if self.color == self.WHITE:
            possible_moves.append(Location(location.x, location.y - 1))
            possible_moves.append(Location(location.x, location.y - 2))
        else:
            possible_moves.append(Location(location.x, location.y + 1))
            possible_moves.append(Location(location.x, location.y + 2))

        return possible_moves
    
    
class Rook(Piece):
    def get_possible_moves(self, location):
        possible_moves = []

        return possible_moves
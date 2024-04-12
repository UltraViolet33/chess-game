class Piece:
    def __init__(self, color) -> None:
        self.color = color


class Pawn(Piece):

    def print(self):
        return f"pawn-{self.color}"

    def get_possible_moves(self, location):
        print(location.x)
        print(location.y)


class Location:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


   


class Cell:
    def __init__(self, x: int, y:int, piece=None) -> None:
        self.location = Location(x, y)
        self.piece = piece


    def has_piece(self)-> bool:
        return self.piece

    def print_location(self):
        if self.has_piece():
            print("P ", end="")
        else:
            print("- ", end="")
        # print("x: ", self.location.x, " y: ", self.location.y, " \n")
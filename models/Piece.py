from models.Cell import Location


class Piece:
    def print(self):
        return f"pawn-{self.color}"
    
    def __init__(self, color) -> None:
        self.color = color
        self.BLACK ='black'
        self.WHITE = 'white'


    def get_possible_moves(self, location, board):
        pass 


class Pawn(Piece):
    def get_possible_moves(self, location, board):
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
    def get_possible_moves(self, location, board):
        possible_moves = []
        # vertical
        print(location.y)
        next_y = location.y - 1
        while next_y > 0:
            cell = board.board_array[next_y][location.x]
            print(cell.print_location())
            if cell.is_empty():
                possible_moves.append(Location(location.x, next_y))
            else:
                break
            next_y -= 1

        next_y = location.y + 1
        while next_y < 8:
            cell = board.board_array[next_y][location.x]
            print(cell.print_location())
            if cell.is_empty():
                possible_moves.append(Location(location.x, next_y))
            else:
                break
            next_y += 1

        #horizontal move
        next_x = location.x - 1
        while next_x > 0:
            cell = board.board_array[location.y][next_x]
            print(cell.print_location())
            if cell.is_empty():
                possible_moves.append(Location(next_x, location.y))
            else:
                break
            next_x -= 1

        next_x = location.x + 1
        while next_x < 8:
            cell = board.board_array[location.y][next_x]
            print(cell.print_location())
            if cell.is_empty():
                possible_moves.append(Location(next_x, location.y))
            else:
                break
            next_x += 1

        return possible_moves



class Bishop(Piece):
    def get_possible_moves(self, location, board):
        possible_moves = []

        # upper-right
        next_y = location.y - 1
        next_x = location.x + 1
        while next_x < 8 and next_y > 0:
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
            else:
                break
            
            next_y -= 1
            next_x += 1


        return possible_moves
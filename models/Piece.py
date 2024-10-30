from models.Cell import Location
from typing import List
from . import Board


class Piece:
    def print(self):
        return f"pawn-{self.color}"

    def __init__(self, color) -> None:
        self.color = color
        self.BLACK = "black"
        self.WHITE = "white"

    def get_possible_moves(self, location, board):
        pass


class Pawn(Piece):
    def get_possible_moves(self, location, board):
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
        return self.static_get_possible_moves(location, board)
    
    @staticmethod
    def static_get_possible_moves(location: Location, board: Board) -> List[Location]:
        possible_moves = []
        
        # vertical
        next_y = location.y - 1
        while next_y >= 0:
            cell = board.board_array[next_y][location.x]
            if cell.is_empty():
                possible_moves.append(Location(location.x, next_y))
            else:
                break
            next_y -= 1

        next_y = location.y + 1
        while next_y < 8:
            cell = board.board_array[next_y][location.x]
            if cell.is_empty():
                possible_moves.append(Location(location.x, next_y))
            else:
                break
            next_y += 1

        # horizontal move
        next_x = location.x - 1
        while next_x >= 0:
            cell = board.board_array[location.y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, location.y))
            else:
                break
            next_x -= 1

        next_x = location.x + 1
        while next_x < 8:
            cell = board.board_array[location.y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, location.y))
            else:
                break
            next_x += 1

        return possible_moves


class Bishop(Piece):
    def get_possible_moves(self, location: Location, board: Board) -> List[Location]:
        return self.static_get_possible_moves(location, board)

    @staticmethod
    def static_get_possible_moves(location: Location, board: Board) -> List[Location]:
        possible_moves = []

        # Upper right
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

        # Upper left
        next_y = location.y - 1
        next_x = location.x - 1
        while next_x >= 0 and next_y > 0:
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
            else:
                break

            next_y -= 1
            next_x -= 1

        # Down right
        next_y = location.y + 1
        next_x = location.x + 1
        while next_x < 8 and next_y < 8:
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
            else:
                break

            next_y += 1
            next_x += 1

        # Down left
        next_y = location.y + 1
        next_x = location.x - 1
        while next_x >= 0 and next_y < 8:
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
            else:
                break

            next_y += 1
            next_x -= 1

        return possible_moves


class Knight(Piece):
    def get_possible_moves(self, location: Location, board: Board) -> List[Location]:
        possible_moves = []

        # Left up up
        if location.x > 0 and location.y > 1:
            next_x = location.x - 1
            next_y = location.y - 2
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        # right up up
        if location.x < 7 and location.y > 1:
            next_x = location.x + 1
            next_y = location.y - 2
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        # Left down down
        if location.x > 0 and location.y < 6:
            next_x = location.x - 1
            next_y = location.y + 2
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        # Right down down
        if location.x < 7 and location.y < 6:
            next_x = location.x + 1
            next_y = location.y + 2
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        # Up left left
        if location.x > 1 and location.y > 0:
            next_x = location.x - 2
            next_y = location.y - 1
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        # Up right right
        if location.x < 6 and location.y > 0:
            next_x = location.x + 2
            next_y = location.y - 1
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
        
        # Down left left
        if location.x > 1 and location.y < 7:
            next_x = location.x - 2
            next_y = location.y + 1
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))
        
        # Down right right
        if location.x < 6 and location.y < 7:
            next_x = location.x + 2
            next_y = location.y + 1
            cell = board.board_array[next_y][next_x]
            if cell.is_empty():
                possible_moves.append(Location(next_x, next_y))

        return possible_moves


class Queen(Piece):
    def get_possible_moves(self, location: Location, board: Board) -> List[Location]:
        possible_moves = []

        # Rook moves
        possible_moves.extend(Rook.static_get_possible_moves(location, board))

        # Bishop moves
        possible_moves.extend(Bishop.static_get_possible_moves(location, board))
    
        return possible_moves


class King(Piece):
    def  get_possible_moves(self, location: Location, board: Board) -> List[Location]:
        possible_moves = []

        # Up
        if location.y > 0:
            cell = board.board_array[location.y - 1][location.x]
            if cell.is_empty():
                possible_moves.append(Location(location.x, location.y - 1))

        # Down
        if location.y < 7:
            cell = board.board_array[location.y + 1][location.x]
            if cell.is_empty():
                possible_moves.append(Location(location.x, location.y + 1))
        
        # Left
        if location.x > 0:
            cell = board.board_array[location.y][location.x - 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x - 1, location.y))

        # Right
        if location.x < 7:
            cell = board.board_array[location.y][location.x + 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x + 1, location.y))

        # Upper right
        if location.x < 7 and location.y > 0:
            cell = board.board_array[location.y - 1][location.x + 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x + 1, location.y - 1))

        # Upper left
        if location.x > 0 and location.y > 0:
            cell = board.board_array[location.y - 1][location.x - 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x - 1, location.y - 1))

        # Down right
        if location.x < 7 and location.y < 7:
            cell = board.board_array[location.y + 1][location.x + 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x + 1, location.y + 1))
        
        # Down left
        if location.x > 0 and location.y < 7:
            cell = board.board_array[location.y + 1][location.x - 1]
            if cell.is_empty():
                possible_moves.append(Location(location.x - 1, location.y + 1))
        
        return possible_moves
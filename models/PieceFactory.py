from .Piece import Piece, Pawn, Rook, Bishop

class PieceFactory():
   
   @staticmethod
   def create_piece_object(text_desc):
        color_dict = {'B': 'black', 'W':'white'}
        pieces_dict = {'P': Pawn, 'R': Rook, 'K': Rook, 'B': Bishop, 'Q': Rook, 'K': Rook}
        if text_desc == '':
            return None
        text_split = text_desc.split('-')
        color = color_dict[text_split[0]]
        piece = pieces_dict[text_split[1]]
        
        return piece(color)

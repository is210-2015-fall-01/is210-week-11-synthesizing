# usr/bin/env python
# -*- coding: utf-8 -*-
"""Chess"""

import time


class ChessPiece(object):
    """The base class for bishop, king and rook classes.

    Attribute:
             prefix- which is set as an empty string.
    """
    
    prefix = ""
    
    def __init__(self, position):
        """Constructor which has 'position' as an attribute.

        Arg:
            position which effectively represents its starting position.

        Attributes:
          position- stores the tile notation of its current position (eg, 'a8'
          moves (list) is a list that store information about the moves.
        """
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []

        
    def is_legal_move(self, tile):
        """Function that checks if a move is legal or not."""
        if self.algebraic_to_numeric(tile):
            return True
        else:
            return False

        
    def algebraic_to_numeric(self, tile):
        """Converts the algebraic string to a numeric
        one and returns a tuple."""
        first = int(ord(tile[0])-96)
        second = int(tile[1])
        if first >= 1 and first <= 8 and second >= 1 and second <= 8:
            return (first-1, second-1)
        else:
            return None

        
    def move(self, new_position):
        """This function uses the move method."""
        if self.is_legal_move(new_position):
            tupple = (self.prefix+self.position, self.prefix+new_position,\
                 time.time())
            self.position = new_position
            self.moves.append(tupple)
            return tupple
        else:
            return False


class Rook(ChessPiece):
    """The rook class inherits from the ChessPiece class."""
    prefix = "R"

    
    def __init__(self, position):
        """The Constructor for this rook class."""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """The overrided is_legal_move method for the rook class."""
         if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            else:
                if int(self.position[1]) == int(position[1]):
                    return True
        else:
           return False


class Bishop(ChessPiece):
    """The Bishop class which inherits from the ChessPiece class."""
    prefix = "B"

    
    def __init__(self, position):
        """The Constructor for this Bishop class. Checks if the move is legal.
        """
        if not super(Bishop, self).is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []

        
    def is_legal_move(self, pos):
        """The overrided is_legal_move method for the Bishop class."""
        tupple = super(Bishop, self).is_legal_move(pos)
        new_position = self.algebraic_to_numeric(pos)
        current_position = self.algebraic_to_numeric(self.position)
        if tupple:
            if abs(new_position[0]-current_position[0]) == \
            abs(new_position[1]-current_position[1]):
                return True
        return False

    
class King(ChessPiece):
    """The King class which inherits from the ChessPiece class."""
    prefix = "K"

    
    def __init__(self, position):
        """The Constructor for this King class."""
        if not super(King, self).is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []

        
    def is_legal_move(self, pos):
        """The overrided is_legal_move method for the King class."""
        tupple = super(King, self).is_legal_move(pos)
        new_position = self.algebraic_to_numeric(pos)
        current_position = self.algebraic_to_numeric(self.position)
        if tupple:
            if (abs(new_position[0]-current_position[0]) + \
                abs(new_position[1]-current_position[1])) <= 2:
                return True
        return False
    
class ChessMatch:
    """The ChessMatch class."""
    def __init__(self, pieces=None):
        """Constructor to the ChessMatch class."""
        if pieces == None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []
    def reset(self):
        """The reset function defined for the ChessMatch class,
        which gives an initial set of positions."""
        self.pieces['Ra1'] = Rook('a1')
        self.pieces['Rh1'] = Rook('h1')
        self.pieces['Ra8'] = Rook('a8')
        self.pieces['Rh8'] = Rook('h8')
        self.pieces['Bc1'] = Bishop('c1')
        self.pieces['Bf1'] = Bishop('f1')
        self.pieces['Bc8'] = Bishop('c8')
        self.pieces['Bf8'] = Bishop('f8')
        self.pieces['Ke1'] = King('e1')
        self.pieces['Ke8'] = King('e8')
    def move(self, piece, destination):
        """The move class ,  which implements the move for the Chessboard."""
        if self.pieces[piece].move(destination) == False:
            return False
        else:
            value = self.pieces[piece].move(destination)
            self.pieces[value[1]] = self.pieces.pop(value[0])
            self.log.append(value)
    def __len__(self):
        """Magic method implemented."""
        return len(self.log)


    
    
    

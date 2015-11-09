#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ChessMaster"""


import time


class ChessPiece(object):
    """ChessPiece setup
    attribute:
        prefix (str}: holds index
    """

    prefix = ''

    def __init__(self, position):
        """Constructor.

        Args: None.

        Returns:
            ChessPiece move

        Example
                >>> piece = ChessPiece('a1')
                >>> piece.position
                'a1'
        """

        if ChessPiece.is_legal_move(self, position):
            self.position = position
            self.moves = []
        else:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Takes a single string argument, tile, and converts it to a tuple with
           two values,a 0-based y-coordinate and a 0-based x-coordinate.
        args:
            tile(str): a 0-based y-coordinate and a 0-based x-coordinate.

        attributes:
            tile(string): a 0-based y-coordinate and a 0-based x-coordinate.

        return:
            Valid Move or None.
        """

        newtile = []
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        number = [1, 2, 3, 4, 5, 6, 7, 8]

        for num in number:
            for alge in letter:
                newtile.append(alge + str(num))
        if tile in newtile:
            xpo = letter.index(tile[0])
            ypo = number.index(int(tile[1]))
            return xpo, ypo
        else:
            return None

    def is_legal_move(self, position):
        """ Legal or not.
        Args:
            None.
        Returns(bool):
            True if the move is legal and False if not.
        """

        if self.algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        """Move piece.

        Args:
            None.

        Returns:
           Valid move or False.
        """

        if self.is_legal_move(position):
            oldpos = self.prefix + self.position
            newpos = self.prefix + position
            moves = ((oldpos, newpos, time.time()))
            self.moves.append(moves)
            self.position = position
            return moves
        else:
            return False

# Task 2


class Rook(ChessPiece):
    """Rook Chess Piece.
    attributes:
       prefix(str): character of the chess pieces.
    """

    prefix = 'R'

    def __init__(self, position):

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):

        rookposone = self.algebraic_to_numeric(position)
        rookpostwo = self.algebraic_to_numeric(self.position)
        if ChessPiece.is_legal_move(self, position):
            amove = abs(rookposone[0] == rookpostwo[0])
            bmove = abs(rookposone[1] == rookpostwo[1])
            if amove or bmove:
                return True
        else:
            return False

# Task 3


class Bishop(ChessPiece):
    """Bishop Chess Piece.
    attributes:
       prefix(str): character of the chess pieces.
    """

    prefix = 'B'

    def __init__(self, position):

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):

        bishopone = self.algebraic_to_numeric(position)
        bishoptwo = self.algebraic_to_numeric(self.position)
        amove = abs(bishoptwo[0] - bishopone[0])
        bmove = abs(bishoptwo[1] - bishopone[1])
        if ChessPiece.is_legal_move(self, position):
            if amove == bmove:
                return True
        else:
            return False

# Task 4

"""class King(ChessPiece):
    King Chess Piece.
    attributes:
       prefix(str): character of the chess pieces.
    

    prefix = 'K'

    def __init__(self, position):

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):

    """

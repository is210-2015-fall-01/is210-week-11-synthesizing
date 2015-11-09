#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chess - a thinker's game."""


import time


class ChessPiece(object):
    """class docstring

    Information about the moves of the chess pieces.

    Attributes:
        prefix: by default, set as an empty string
    """
    prefix = ''

    def __init__(self, position):
        """class constructor docstring

        Information about the moves of the chess pieces.

        Args:
            position: stores the tile notation of its current position. eg 'a8'
            moves: list stores tuples of information about each move a piece
            has taken
        """
        if ChessPiece.is_legal_move(self, position):
            self.position = position
            self.moves = []
        else:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """converts a position to a two-value tuple.

        Args:
            tile: location of piece (e.g. 'a1')

        Returns:
            tuple containing (row, col) location format
        """

        if len(tile) == 2:
            if (97 <= ord(tile[:1]) <= 104) and (49 <= ord(tile[-1:]) <= 56):
                # ascii char 'a'-'h' = 97-104 & ascii char '1'-'8' = 49-56
                # e.g. ord('a') = 97 / chr(97) = 'a'
                row = tile[:1]  # first character (letter)
                col = tile[-1:]  # last character (number)
                if row == 'a':
                    return (0, int(col)-1)
                if row == 'b':
                    return (1, int(col)-1)
                if row == 'c':
                    return (2, int(col)-1)
                if row == 'd':
                    return (3, int(col)-1)
                if row == 'e':
                    return (4, int(col)-1)
                if row == 'f':
                    return (5, int(col)-1)
                if row == 'g':
                    return (6, int(col)-1)
                if row == 'h':
                    return (7, int(col)-1)
                else:
                    return None
        else:
            return None

    def is_legal_move(self, position):
        """Checks whether a move is legal.

        Is the move outside of the 8x8 board?

        Args:
            position: algebraic notation of the new position to which this piece
            should be moved

        Returns:
            True if legal, else False
        """
        algnot = self.algebraic_to_numeric(position)
        if algnot is None:
            return False
        elif (0 <= algnot[0] <= 7) and (0 <= algnot[1] <= 7):
            return True
        else:
            return False

    def move(self, position):
        """function docstring"""
        if self.is_legal_move(position):
            movetup = (self.prefix + self.position, self.prefix + position,
                       time.time())
            self.moves.append(movetup)
            self.position = position
            return movetup
        else:
            return False


class Rook(ChessPiece):
    """A Chess Piece, Rook, subclassed from ChessPiece."""
    prefix = 'R'

    def __init__(self, position):
        """Construction docstring"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Function docstring"""
        if ChessPiece.is_legal_move(self, position):
            if self.position[0] is position[0]:
                if int(self.position[1]) != int(position[1]):
                    return True
            elif int(self.position[1]) == int(position[1]):
                return True
        else:
            return False


class Bishop(ChessPiece):
    """A Chess Piece, Bishop, subclassed from ChessPiece."""
    prefix = 'B'

    def __init__(self, position):
        """Construction docstring"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Method docstring"""
        if ChessPiece.is_legal_move(self, position):
            if abs(ord(self.position[0]) - ord(position[0])) != \
               abs(ord(self.position[1]) - ord(position[1])):
                return False
            else:
                return True


class King(ChessPiece):
    """A Chess Piece, King, subclassed from ChessPiece."""
    prefix = 'K'

    def __init__(self, position):
        """Construction docstring"""
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Method docstring"""
        if ChessPiece.is_legal_move(self, position):
            if (abs(ord(self.position[0]) - ord(position[0])) == 1) and \
               (ord(self.position[1]) == ord(position[1])):
                return True
            elif (ord(self.position[0]) == ord(position[0])) and \
                 (abs(ord(self.position[1]) - ord(position[1])) == 1):
                return True
            elif (abs(ord(self.position[0]) - ord(position[0])) == 1) and \
                 (abs(ord(self.position[1]) - ord(position[1])) == 1):
                return True
        else:
            return False


class ChessMatch(object):
    """Class docstring"""

    def __init__(self, pieces=None):
        """construction docstring"""
        if pieces is None:
            self.reset(pieces)
        else:
            self.pieces = pieces
            self.log = []

    def reset(self, match):
        """method docstring"""
        match.log = []
        match.pieces = dict([('Ra1', 'a1'), (), (), (), (), (), (), (),
                             (), (), ('Ke8', 'e8')])
        return match

    def move(self, piecename, coord):
        """method docstring"""

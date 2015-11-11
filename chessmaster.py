#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A chess game """

import time


class ChessPiece(object):
    """Moving piece in a game of chess."""
    prefix = ''

    def __init__(self, position):
        """An instance.
        Args:
            position: an alphanumeric position on the board.
        Attribute:
            prefix: an empty string by default.
        """
        if not ChessPiece.is_legal_move(self, position):
            excep = '{} is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """A tile as a two value tuple used as position.
        Arg:
            tile: tuple consisting two value of the position on the board.
        Returns:
            Converts alpha-numeric characters into coordinates.
            Returns invalid coordinates.
        Example:
            >>> piece = ChessPiece('a1')
            >>> piece.position
            'a1'
            >>> piece.algebraic_to_numeric('e7')
            (4,6)
            >>> piece.algebraic_to_numeric('j9')
            None
        """
        x_axis = 'abcdefgh'
        y_axis = [1, 2, 3, 4, 5, 6, 7, 8]
        if tile[0] in x_axis and int(tile[1]) in y_axis:
            return (x_axis.find(tile[0]), (int(tile[1]) - 1))
        else:
            return None

    def is_legal_move(self, position):
        """To test if new position is legal to move.
        Args:
            position: an allowed position on the board.
        Attribute:
            newpos: a new position on the board.
        Returns:
            Returns 'True' for a legal move; and 'False' for not a legal move.
        Example:
            >>> piece.move('j9')
            False
        """
        newpos = self.algebraic_to_numeric
        if newpos(position):
            return True
        else:
            return False

    def move(self, position):
        """Pieces to move.
        Args:
            position: an allowed position on the board.
        Attribute:
            newpos: a new position on the board.
        Return:
            Returns a legal move on the board.
        Examples:
            >>> piece.move('e7')
            ('a1', 'e7', 1413252815.610075)
            >>> piece.position
            'e7'
        """
        newpos = self.is_legal_move(position)
        if newpos:
            tup = (self.prefix + self.position,
                   self.prefix + position, time.time())
            self.moves.append(tup)
            self.position = position
            return tup
        else:
            return False


class Rook(ChessPiece):
    """A child class of ChessPiece."""
    prefix = 'R'

    def __init__(self, position):
        """An override instance.
        Args:
            position: an alphanumeric position on the board.
        Attribute:
            prefix: A(str) by default 'R'.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Constructor for Rook.
        Args:
            position: an allowed position on the board.
        Returns:
            Checks if move does not work.
        Examples:
            >>> rook = Rook('a1')
            >>> rook.prefix
            'R'
            >>> rook.move('b2')
            False
            >>> rook.move('h1')
            ('Ra1', 'Rh1', 1413252817.89340)
        """
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
    """A child clas of ChessPiece.
    """
    prefix = 'B'

    def __init__(self, position):
        """An override instance.
        Args:
            position: an alphanumeric position on the board.
        Attribute:
            prefix: A(str) by default 'B'.
        """
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Constructor for Bishop.
        Args:
            position: an allowed position on the board.
        Returns:
            A coordinate value if the move is legal or 'False' if it's not.
        Examples:
            >>> bishop = Bishop('a1')
            >>> bishop.prefix
            'B'
            >>> bishop.move('a2')
            False
            >>> bishop.move('c3')
            ('Ba1', 'Bc1', 1413252817.89340)
        """
        old = self.algebraic_to_numeric(position)
        new = self.algebraic_to_numeric(position)
        if ChessPiece.is_legal_move(self, position):
            if (old[0] + new[0]) == (old[1] + new[1]):
                return True
        else:
            return False

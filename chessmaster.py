#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long task"""


import time


class ChessPiece(object):
    """A class that stores ChessPiece data, and imports from time module."""
    prefix = ''

    def __init__(self, position):
        """A constructor for ChessPiece() class.

        Args:
            position:??

        Attributes:
            position:??

        """
        legal_move_test = ChessPiece.is_legal_move(self, position)
        if legal_move_test is False:
            excep = '`{}` is not legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """This method will convert algebraic positions to numeric.

        Args:
            tile(string): An algebraic position on the chessboard.

        Attributes:
            tile(string): An algebraic position on the chessboard.

        Returns:
            This method returns a tuple containing numeric positions.
            Returns None if the algebraic position is invalid

        Example:
            >>>
            (2, 5)

        """
        valid_tile = True

        if len(tile) != 2:
            valid_tile = False
        else:
            my_y = int(tile[1]) - 1
            if my_y >= 8:
                valid_tile = False
            else:
                origx = tile[0]
                if origx == 'a':
                    my_x = 0
                elif origx == 'b':
                    my_x = 1
                elif origx == 'c':
                    my_x = 2
                elif origx == 'd':
                    my_x = 3
                elif origx == 'e':
                    my_x = 4
                elif origx == 'f':
                    my_x = 5
                elif origx == 'g':
                    my_x = 6
                elif origx == 'h':
                    my_x = 7
                else:
                    valid_tile = False
        if valid_tile is False:
            my_tup = None
        else:
            my_tup = (my_x, my_y)
        return my_tup

    def is_legal_move(self, position):
        """This method will ensure that the chess move is valid, and raise a\
            flag if need be.

        Args:
            position:

        Attributes:
            numeric_position: converted tuple

        Returns:
            It returns a boolean

        Example:
            >>>
            False

        """
        numeric_position = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if numeric_position is None:
            legal_move_flag = False
        return legal_move_flag

    def move(self, position):
        """This method will calculate the tuple with three values.

        Args:
            position:

        Attributes:
            position:

        Returns:
            It returns a tuple, containing 2 strings and a timestamp.
            It returns false if the move is not valid

        Example:
            >>>
            ('a3', 'd4', 1447029111.336016)

        """
        legal_move = self.is_legal_move(position)
        if legal_move is True:
            oldposition = self.prefix + self.position
            newposition = self.prefix + position
            final_tup = (oldposition, newposition, time.time())
            self.moves.append(final_tup)
            self.position = position
            return final_tup
        else:
            return False


class Rook(ChessPiece):
    """A class that stores Rook data."""

    prefix = 'R'

    def is_legal_move(self, position):
        """This method will control the Rook's moves on chessboard.

        Args:
            position:

        Attributes:
            current_position: A converted tuple
            new_position: A converted tuple

        Returns:
            It returns a boolean for legal_move_flag.

        Example:
            >>>
            False

        """
        current_position = self.algebraic_to_numeric(self.position)
        new_position = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if new_position is None:
            legal_move_flag = False
        else:
            if current_position[0] != new_position[0]:
                position_x_different = True
            else:
                position_x_different = False
            if current_position[1] != new_position[1]:
                position_y_different = True
            else:
                position_y_different = False
            if position_x_different and position_y_different:
                legal_move_flag = False
        return legal_move_flag


class Bishop(ChessPiece):
    """A class that stores Bishop's data"""

    prefix = 'B'

    def is_legal_move(self, position):
        """This method will control the Bishop's moves on chessboard.

        Args:
            position:

        Attributes:
            old_tup: A tuple of old values
            new_tup: A tuple of new values

        Returns:
            It returns a boolean for legal_move_flag.

        Example:
            >>>
            False

        """
        old_tup = self.algebraic_to_numeric(self.position)
        new_tup = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if new_tup is None:
            legal_move_flag = False
        else:
            if abs(old_tup[0] - new_tup[0]) != abs(old_tup[1] - new_tup[1]):
                legal_move_flag = False
        return legal_move_flag


class Queen(ChessPiece):
    """A class that stores Queen data."""

    prefix = 'Q'

    def is_legal_move(self, position):
        """This method will control the Queen's moves on chessboard.

        Args:
            position:

        Attributes:
            current_position: A converted tuple
            new_position: A converted tuple

        Returns:
            It returns a boolean for legal_move_flag.

        Example:
            >>>
            False

        """
        current_position = self.algebraic_to_numeric(self.position)
        new_position = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if new_position is None:
            legal_move_flag = False
        else:
            if current_position[0] != new_position[0]:
                position_x_different = True
            else:
                position_x_different = False
            if current_position[1] != new_position[1]:
                position_y_different = True
            else:
                position_y_different = False
            if position_x_different and position_y_different:
                legal_move_flag = False
            if abs(current_position[0] - new_position[0]) \
               != abs(current_position[1] - new_position[1]):
                legal_move_flag = False
        return legal_move_flag


class King(ChessPiece):
    """A class that stores King's data"""

    prefix = 'K'

    def is_legal_move(self, position):
        """This method will control the King's moves on chessboard.

        Args:
            position:

        Attributes:
            old_tup: Tuple containg current values
            new_tup: Tuple containing new values

        Returns:
            It returns tuples and a boolean for legal_move_flag.

        Example:
            >>>
            (4, 0) (4, 1)

        """
        old_tup = self.algebraic_to_numeric(self.position)
        new_tup = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if new_tup is None:
            legal_move_flag = False
        else:
            if (abs(old_tup[0] - new_tup[0]) > 1) \
               or (abs(old_tup[1] - new_tup[1]) > 1):
                legal_move_flag = False
        return legal_move_flag


class ChessMatch(object):
    """A class that stores ChessMatch's data"""

    def __init__(self, pieces=None):
        """A constructor for ChessMatch() class.

        Args:
            pieces = set to a default value of None

        Attributes:
            pieces = set to a default value of None

        """
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """A method to reset the chessboard.

        Attributes:
            log: A empty list
            pieces: An dictionary

        """
        self.log = []
        self.pieces = {}

        chessobj = Rook("h8")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Rook("a1")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Bishop("f1")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Bishop("c8")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = King("e1")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Rook("h1")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Rook("a8")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Bishop("c1")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = Bishop("f8")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

        chessobj = King("e8")
        self.pieces[chessobj.prefix + chessobj.position] = chessobj

    def move(self, fullnotation, dest_position):
        """A method to makes chess moves.

        Args:
            fullnotation:
            dest_position:

        Attributes:
            my_tup: A set of 2 tuples

        """
        my_tup = self.pieces[fullnotation].move(dest_position)
        if my_tup is False:
            return False
        else:
            self.log.append(my_tup)
            chessobj = self.pieces.pop(fullnotation)
            self.pieces[chessobj.prefix + dest_position] = chessobj
            return True

    def __len__(self):
        """A method to determine the length of log.

        Returns: An integer

        """
        return len(self.log)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster"""

import time


class ChessPiece(object):
    """Determines whther piece in on chess board and tracks moves"""

    prefix = ''

    def __init__(self, position):
        """Constructor"""
        self.position = position
        self.moves = []
        legmove = self.is_legal_move(position)
        if not legmove:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Returns coordinates as numeric tuple.
        Args:
            tile (str): list of two-item string with coordinates a-h, 1-8
        Returns:
            Two-item numeric tuple
        Examples:
            algebraic_to_numeric('c5')
            >>>(2, 4)
        """
        list1 = []
        coordict = {
            '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7
        }
        if len(tile) != 2:
            return None
        for item in tile:
            item = str(item)
            if item not in coordict:
                return None
            else:
                coordinate = coordict[item]
                list1.append(coordinate)
                result = tuple(list1)
        return result

    def is_legal_move(self, position):
        """Test to make sure piece in on board
        Args:
            position (str): chess board coordinates
        Returns: True or False
        Examples:
            is_legal_move('a1')
            >>>True
        """
        tupval = self.algebraic_to_numeric(position)
        if tupval:
            return True
        else:
            return False

    def move(self, position):
        """Tracks moves of pieces"""
        islegal = self.is_legal_move(position)
        if islegal:
            oldposition = self.prefix + self.position
            self.position = position
            newposition = self.prefix + position
            timestamp = time.time()
            tupval = (oldposition, newposition, timestamp)
            self.moves.append(tupval)
            return tupval
        else:
            return False


class Rook(ChessPiece):
    """Rook piece"""

    prefix = 'R'

    def is_legal_move(self, position):
        """determines whether movment of Rook is valid"""
        islegal = ChessPiece.is_legal_move(self, position)
        if islegal:
            xmove = self.position[0]
            ymove = self.position[1]
            if xmove != position[0]:
                if ymove == position[1]:
                    return True
                else:
                    return False
            elif ymove != position[1]:
                if xmove == position[0]:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


class Bishop(ChessPiece):
    """Bishop Piece"""

    prefix = 'B'

    def is_legal_move(self, position):
        """Determines whether movement of Bishop is valid"""
        oldcoordinates = self.algebraic_to_numeric(self.position)
        newcoordinates = self.algebraic_to_numeric(position)
        islegal = ChessPiece.is_legal_move(self, position)
        if islegal:
            xdistance = int(newcoordinates[0] - oldcoordinates[0])
            ydistance = int(newcoordinates[1] - oldcoordinates[1])
            if abs(xdistance) == abs(ydistance):
                return True
        else:
            return False


class King(ChessPiece):
    """King piece"""

    prefix = 'K'

    def is_legal_move(self, position):
        """Determines whether movement of King is valid"""
        oldcoordinates = self.algebraic_to_numeric(self.position)
        newcoordinates = self.algebraic_to_numeric(position)
        islegal = ChessPiece.is_legal_move(self, position)
        if islegal:
            xdistance = int(newcoordinates[0] - oldcoordinates[0])
            ydistance = int(newcoordinates[1] - oldcoordinates[1])
            if abs(xdistance) <= 1 and abs(ydistance) <= 1:
                return True
            elif abs(xdistance) == 1 and abs(ydistance) == 0:
                return True
            elif abs(xdistance) == 0 and abs(ydistance) == 1:
                return True
        else:
            return False

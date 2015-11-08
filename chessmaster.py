#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chessmaster"""

import time

class ChessPiece(object):

    prefix = ''
    def __init__(self, position):
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
        list = []
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
                list.append(coordinate)
                result = tuple(list)
        return result

    def is_legal_move(self, position):
        tupval = self.algebraic_to_numeric(position)
        if tupval:
            return True
        else:
            return False
    

    def move(self, position):
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

    prefix = 'R'


    def is_legal_move(self, position):
        islegal = ChessPiece.is_legal_move(self, position)
        if islegal:
            xmove = self.position[0]
            ymove = self.position[1]
            if xmove != position[0]:
                if ymove == position[1]:
                    return True
            elif ymove != position[1]:
                if xmove == position[0]:
                    return True
            else:
                return True

            

            
            
            
            
    

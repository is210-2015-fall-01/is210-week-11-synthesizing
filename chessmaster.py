#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long task"""


import time


class ChessPiece(object):
    """doc"""
    prefix = ''

    def __init__(self, position):
        """doc"""
        legal_move_test = ChessPiece.is_legal_move(self, position)
        if legal_move_test is False:
            excep = '`{}` is not legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """doc"""
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
        """doc"""
        numeric_position = self.algebraic_to_numeric(position)
        legal_move_flag = True
        if numeric_position is None:
            legal_move_flag = False
        return legal_move_flag

    def move(self, position):
        """doc"""
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


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long task"""


import chessmaster


class Rook(chessmaster.ChessPiece):
    """doc"""
    prefix = 'R'

    def is_legal_move(self, position):
        """doc"""
        current_position = self.algebraic_to_numeric(self.position)
        new_position = self.algebraic_to_numeric(position)
        print current_position, new_position
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

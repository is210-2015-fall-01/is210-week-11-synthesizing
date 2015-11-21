"""Chess"""


import time


class ChessPiece(object):
    """ object of chessPiece class
    attribute:
        prefix (string): by default, set as an empty string
    """

    prefix = ''

    def __init__(self, position):
        """ chessPiece construct
        args:
            position (string):
                stores the tile notation of its current position (eg, 'a8')
            moves Lists):
                list that stores tuples of information about each move
         attributes:
            position (string):
                stores the tile notation of its current position (eg, 'a8')
            moves Lists):
                list that stores tuples of information about each move
            return:
                move(lists):
                    lists of the postion of each move
            example
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
        """class function that takes a single string argument, tile, and convert
           it to a tuple with two values, a 0-based y-coordinate and a 0-based
           x-coordinate
        args:
            tile(string): string to be converts it to a tuple with two values,
                          a 0-based y-coordinate and a 0-based x-coordinate.
        attributes:
            tile(string): string to be converts it to a tuple with two values,
                          a 0-based y-coordinate and a 0-based x-coordinate.
        return:
            tuples ofalid move or none if not invalid
        example:
            >>> piece.algebraic_to_numeric('e7')
            (4,6)
            >>> piece.algebraic_to_numeric('j9')
            None
            >>> piece.move('j9')
            False
        """

        newtile = []
        algebraicnotation = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        numericnotation = range(1, 9)

        for numeric in numericnotation:
            for algebraic in algebraicnotation:
                newtile.append(algebraic + str(numeric))
        if tile in newtile:
            x_cord = algebraicnotation.index(tile[0])
            y_cord = numericnotation.index(int(tile[1]))
            return x_cord, y_cord
        else:
            return None

    def is_legal_move(self, position):
        """ a fuction that test if the suggested move is a legal move
        args:
            postion(string): the  algebraic notation of the new position to
                             which this piece should be moved
            return (bool):
                Return True if the move is legal and False if it is not
            example:
            piece = ChessPiece('e91')
            Traceback (most recent call last):
            File "<pyshell#216>", line 1, in <module>
            piece = ChessPiece('e91')
            raise ValueError(excep.format(position))
            ValueError: `e91` is not a legal start position
            example:
            >>> piece = ChessPiece('e1')
            >>> piece.move('e7')
            [('e1', 'e7', 1429395759.478843)]
        """

        if self.algebraic_to_numeric(position) is None:

            return False
        else:
            return True

    def move(self, position):
        """a function to actually move our piece.
        args:
            the algebraic notation of the new position to be moved.
        return:
            Return the above tuple is position is a valid move or
            If it is not legal, return False
        """

        if self.is_legal_move(position):

            oldposition = self.prefix + self.position
            newposition = self.prefix + position
            moves = ((oldposition, newposition, time.time()))
            self.moves.append(moves)
            self.position = position
            print "in move"
            print self.position
           # position = self.prefix + position
            return moves
        else:
            return False


class Rook(ChessPiece):
    """  Rook class a subclasses of ChessPiece"
    args:
        the algebraic notation of the new position to be moved.attributes:
        prefix (string): first character of the chess pieces
    """

    prefix = 'R'

    def __init__(self, position):

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):

        rook_new_position = self.algebraic_to_numeric(position)
        rook_old_position = self.algebraic_to_numeric(self.position)

        if ChessPiece.is_legal_move(self, position):
            x_move = abs(rook_new_position[0] == rook_old_position[0])
            y_move = abs(rook_new_position[1] == rook_old_position[1])
            if y_move or x_move:
                return True

        else:
            return False


class Bishop(ChessPiece):
    """  Bishop class a subclasses of ChessPiece"
    attributes:
        prefix (string): first character of the chess pieces
    """

    prefix = 'B'

    def __init__(self, position):

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        bishop_new_position = self.algebraic_to_numeric(position)

        bishop_old_position = self.algebraic_to_numeric(self.position)
        x_move_diff = abs(bishop_old_position[0] - bishop_new_position[0])
        y_move_diff = abs(bishop_old_position[1] - bishop_new_position[1])
        if ChessPiece.is_legal_move(self, position):
            if x_move_diff == y_move_diff:
                return True
        else:
            return False


class King(ChessPiece):
    """ King class, a  subclass of ChessPiece
    attributes:
        prefix (string): first character of the chess pieces
    """
    prefix = 'K'

    def __init__(self, position):
        """ king constructor
        args:
        the algebraic notation of the new position to be moved.
        """

        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """ a fuction that test if the king suggested move is a legal move
        args:
            postion(string): the  algebraic notation of the new position to
                             which this piece should be moved
            return (bool):
                Return True if the move is legal and False if it is not
        example:
        >>> king = King('a1')
        >>> king.prefix
        'K'
        >>> king.move('a3')
        False
        >>> king.move('b1')
        ('Ka1', 'Kb1', 1429497441.23176)
        >>> king.move('a2')
        ('Kb1', 'Ka2', 1429497448.906799)
        """

        king_new_position = self.algebraic_to_numeric(position)

        king_old_position = self.algebraic_to_numeric(self.position)

        x_move_diff = abs(king_new_position[0] - king_old_position[0])
        y_move_diff = abs(king_new_position[1] - king_old_position[1])
        if ChessPiece.is_legal_move(self, position):

            if x_move_diff == 0 and y_move_diff == 1:
                return True
            elif x_move_diff == 1 and y_move_diff == 0:
                return True
            elif x_move_diff == 1 and y_move_diff == 1:
                return True

        else:
            return False


class ChessMatch(object):
    """match class declaratioon
    attributes:
        None
    """

    def __init__(self, pieces=None):
        """Chassmatch constructor
        args:
            piece(lists): a dict of pieces keyed by their positions on the board
            log (list): log lits of game
        return:
        """

        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """ a funct that resets the match log to an empty list and places
            our pieces back at their starting positions:
        return:
            dict of piece current position in Full Notation is the key
        exampe:
            >>> match.reset()
            >>> len(match)
            0
            >>> len(match.pieces)
            10
        """
        self.log = []
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}

        return self.pieces


def move(self, piece, position):
    """
    args:
        pieces(dicts): The name of the piece in Full Notation
        position(string): The destination coordinate in short notation(eg,'a7')
    return:
        returns False, If a piece is unable to move to the coordinate
    example:
        >>> match.move('Ke1', 'e2')
        >>> match.pieces
        {'Ke2': <__main__.King object at 0x70000000000>, 'Ke8':
        <__main__.King object at 0x7000000000a>}
    """

    ChessPiece.move.__init__(self)
    if piece in self.pieces:
        chesspiece = self.pieces[piece]
        moved = chesspiece.move(position)
        self.log.append(moved)
        self.pieces.pop(piece)
        self.pieces.update({moved[1]: chesspiece})


def __len__(self):

    return len(self.pieces)

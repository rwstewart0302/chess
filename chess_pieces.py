W_PAWN = 'WP'
W_ROOK = 'WR'
W_KNIGHT = 'WN'
W_BISHOP = 'WB'
W_QUEEN = 'WQ'
W_KING = 'WK'

B_PAWN = 'BP'
B_ROOK = 'BR'
B_KNIGHT = 'BN'
B_BISHOP = 'BB'
B_QUEEN = 'BQ'
B_KING = 'BK'

class PieceMovement:
    def __init__(self, board):
        self.board = board
        self.piece = None
        self.player = None
        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None


    def move(self, piece, player, r_start, c_start, r_end, c_end, board):
        self.player = player
        self.piece = piece
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if player == 'white':
            if piece == W_PAWN:
                if board[r_end, c_end] = '00':
                    board[r_end, c_end] = piece

        elif player == 'black':
            pass # move black pawn pieces
        return board

class Rook:
    def __init__(self):
        self.rook = 5

    def move(player):
        if player == 'white':
            pass # move white pieces
        elif player == 'black':
            pass # move black pieces

class Knight:
    def __init__(self):
        self.knight = 3

    def move(player):
        if player == 'white':
            pass # move white pieces
        elif player == 'black':
            pass # move black pieces

class Bishop:
    def __init__(self):
        self.bishop = 3

    def move(player):
        if player == 'white':
            pass # move white pieces
        elif player == 'black':
            pass # move black pieces

class Queen:
    def __init__(self):
        self.queen = 9

    def move(player):
        if player == 'white':
            pass # move white pieces
        elif player == 'black':
            pass # move black pieces

class King:
    def __init__(self):
        self.king = 1_000

    def move(player):
        if player == 'white':
            pass # move white pieces
        elif player == 'black':
            pass # move black pieces

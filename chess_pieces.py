import piece_movement as pm

PIECES = {
    'White':
    {
        'PAWN' : 'WP',
        'ROOK' : 'WR',
        'KNIGHT' : 'WN',
        'BISHOP' : 'WB',
        'QUEEN' : 'WQ',
        'KING' : 'WK'
    },
    'Black':
    {
        'PAWN' : 'BP',
        'ROOK' : 'BR',
        'KNIGHT' : 'BN',
        'BISHOP' : 'BB',
        'QUEEN' : 'BQ',
        'KING' : 'BK'
    },
    'EMPTY': '00'
    }

W_PAWN = PIECES['White']['PAWN']
W_ROOK = PIECES['White']['ROOK']
W_KNIGHT = PIECES['White']['KNIGHT']
W_BISHOP = PIECES['White']['BISHOP']
W_QUEEN = PIECES['White']['QUEEN']
W_KING = PIECES['White']['KING']

B_PAWN = PIECES['Black']['PAWN']
B_ROOK = PIECES['Black']['ROOK']
B_KNIGHT = PIECES['Black']['KNIGHT']
B_BISHOP = PIECES['Black']['BISHOP']
B_QUEEN = PIECES['Black']['QUEEN']
B_KING = PIECES['Black']['KING']

EMPTY = PIECES['EMPTY']

PLAYER_1 = list(PIECES.keys())[0]
PLAYER_2 = list(PIECES.keys())[1]

RANKS = 8
FILES = 8

class Pawn:
    def __init__(self, board, player, turn, prev_r_delta, prev_c_end, prev_moved_piece):
        self.value = 1
        self.board = board
        self.turn = turn
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        if self.player == PLAYER_1:
            self.piece = W_PAWN
        elif self.player == PLAYER_2:
            self.piece = B_PAWN

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None


    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if self.piece == W_PAWN or self.piece == B_PAWN:
            print('test: ', pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.turn, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece))
            if pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.turn, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
                self.board[self.r_start, self.c_start] = EMPTY
                self.board[self.r_end, self.c_end] = self.piece

        elif self.player == 'test':
            pass # move black pawn pieces
        return self.board

### TODO - FIX ALL SYNTAX ERRORS IN IF STATEMENTS ###




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

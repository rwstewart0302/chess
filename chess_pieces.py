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

class Pawn:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        if player == 'white':
            self.piece = W_PAWN
        else:
            self.piece = B_PAWN

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None


    def move(self, r_start, c_start, r_end, c_end, board):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if self.piece == W_PAWN or self.piece == B_PAWN:
            if lambda : is_valid_pawn_move(piece, player, r_start, c_start, board):
                board[r_start, c_start] = '00'
                board[r_end, c_end] = 'WP'

        elif player == 'test':
            pass # move black pawn pieces
        return board


    def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board):
        if player == 'white':
            try:
                if r_start == 6:
                    if board[r_start-1, c_start] == '00' and board[r_start-1, c_start-1] != '00' and board[r_start-1, c_start+1] != '00':
                        if (r_end == r_start - 1 and c_end == c_start) or (r_end == r_start - 1 and c_end == c_start - 1) or (r_end == r_start - 1 and c_end == c_start + 1:):
                            return True
                    elif board[r_start-1, c_start] == '00' and board[r_start-2, c_start] == '00' board[r_start-1, c_start-1] != '00' and board[r_start-1, c_start+1] != '00':
                        if (r_end == r_start - 1 and c_end == c_start) or (r_end == r_start - 1 and c_end == c_start - 1) or (r_end == r_start - 1 and c_end == c_start + 1:):
                            return True
                if board[r_start-1, c_start] == '00' and board[r_start-1, c_start-1] != '00' and board[r_start-1, c_start+1] != '00':
                    if (r_end == r_start - 1 and c_end == c_start) or (r_end == r_start - 1 and c_end == c_start - 1) or (r_end == r_start - 1 and c_end == c_start + 1:):
                        return True
                elif board[r_start-1, c_start] == '00' and board[r_start-1, c_start-1] != '00' and board[r_start-1, c_start+1] != '00':
                    if (r_end == r_start - 1 and c_end == c_start) or (r_end == r_start - 1 and c_end == c_start - 1) or (r_end == r_start - 1 and c_end == c_start + 1:):
                        return True
                else:
                    return False
            except IndexError:
                if c_start == 0 and (board[r_start-1, c_start] == '00' or board[r_start-1, c_start+1] != '00'):
                    print('2')
                    return True
                elif c_start == 7 and (board[r_start-1, c_start] == '00' or board[r_start-1, c_start-1] != '00'):
                    print('3')
                    return True
                else:
                    return False


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

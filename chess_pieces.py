import piece_movement as pm
import check

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
    def __init__(self, board, player, prev_r_delta, prev_c_end, prev_moved_piece):
        self.value = 1
        self.board = board
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
        self.temp_board = None


    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        self.temp_board = self.board

        print('test: ', pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece))

        if pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece) == 'en passant':
            self.temp_board[self.r_start, self.c_start] = EMPTY
            self.temp_board[self.r_start, self.prev_c_end] = EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            print('test check: ', check.is_check(self.player, self.temp_board))
            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True

        elif pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
            self.temp_board[self.r_start, self.c_start] = EMPTY
            if self.player == PLAYER_1 and self.r_end == 0: # pawn promotion
                promotion_piece = eval(input("1 ---> Queen \n 2 ---> Rook \n 3 ---> Bishop \n 4 ---> Knight \n: "))
                if promotion_piece == 1:
                    self.piece = W_QUEEN
                elif promotion_piece == 2:
                    self.piece = W_ROOK
                elif promotion_piece == 3:
                    self.piece = W_BISHOP
                elif promotion_piece == 4:
                    self.piece = W_KNIGHT
            elif self.player == PLAYER_2 and self.r_end == 7: # pawn promotion
                promotion_piece = eval(input("1 ---> Queen \n 2 ---> Rook \n 3 ---> Bishop \n 4 ---> Knight \n: "))
                if promotion_piece == 1:
                    self.piece = B_QUEEN
                elif promotion_piece == 2:
                    self.piece = B_ROOK
                elif promotion_piece == 3:
                    self.piece = B_BISHOP
                elif promotion_piece == 4:
                    self.piece = B_KNIGHT
            else:
                pass

            self.temp_board[self.r_end, self.c_end] = self.piece
            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True

        else:
            return self.board, False

class Rook:
    def __init__(self, board, player):
        self.rook = 5
        self.board = board
        self.player = player
        if self.player == PLAYER_1:
            self.piece = W_ROOK
        elif self.player == PLAYER_2:
            self.piece = B_ROOK

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None
        self.temp_board = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        self.temp_board = self.board

        if pm.is_valid_rook_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True
        else:
            return self.board, False

class Knight:
    def __init__(self, board, player):
        self.knight = 3
        self.player = player
        self.board = board
        if self.player == PLAYER_1:
            self.piece = W_KNIGHT
        elif self.player == PLAYER_2:
            self.piece = B_KNIGHT

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None
        self.temp_board = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        self.temp_board = self.board

        print('test: ', pm.is_valid_knight_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board))

        if pm.is_valid_knight_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            # should check for checks in the main function as well!!!
            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True
        else:
            return self.board, False

class Bishop:
    def __init__(board, player, turn, prev_r_delta, prev_c_end, prev_moved_piece):
        self.bishop = 3
        self.board = board
        self.turn = turn
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        if self.player == PLAYER_1:
            self.piece = W_BISHOP
        elif self.player == PLAYER_2:
            self.piece = B_BISHOP

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if self.piece == W_BISHOP or self.piece == B_BISHOP:
            if pm.is_valid_bishop_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
                self.board[self.r_start, self.c_start] = EMPTY
                self.board[self.r_end, self.c_end] = self.piece
        return self.board

class Queen:
    def __init__(board, player, turn, prev_r_delta, prev_c_end, prev_moved_piece):
        self.queen = 9
        self.board = board
        self.turn = turn
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        if self.player == PLAYER_1:
            self.piece = W_QUEEN
        elif self.player == PLAYER_2:
            self.piece = B_QUEEN

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if self.piece == W_QUEEN or self.piece == B_QUEEN:
            if pm.is_valid_queen_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
                self.board[self.r_start, self.c_start] = EMPTY
                self.board[self.r_end, self.c_end] = self.piece
        return self.board

class King:
    def __init__(board, player, turn, prev_r_delta, prev_c_end, prev_moved_piece):
        self.queen = 1_000_000
        self.board = board
        self.turn = turn
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        if self.player == PLAYER_1:
            self.piece = W_KING
        elif self.player == PLAYER_2:
            self.piece = B_KING

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end
        if self.piece == W_KING or self.piece == B_KING:
            if pm.is_valid_king_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
                self.board[self.r_start, self.c_start] = EMPTY
                self.board[self.r_end, self.c_end] = self.piece
        return self.board

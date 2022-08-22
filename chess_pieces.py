import check, config
import piece_movement as pm
import castle_movement as cm

class Pawn:
    def __init__(self, board, player, prev_r_delta, prev_c_end, prev_moved_piece):
        self.value = 1
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        if self.player == config.PLAYER_1:
            self.piece = config.W_PAWN
        elif self.player == config.PLAYER_2:
            self.piece = config.B_PAWN

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece) == 'en passant':
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
            self.temp_board[self.r_start, self.prev_c_end] = config.EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True

        elif pm.is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
            if self.player == config.PLAYER_1 and self.r_end == 0: # pawn promotion
                promotion_piece = eval(input("\n 1 ---> Queen \n 2 ---> Rook \n 3 ---> Bishop \n 4 ---> Knight \n: "))
                if promotion_piece == 1:
                    self.piece = config.W_QUEEN
                elif promotion_piece == 2:
                    self.piece = config.W_ROOK
                elif promotion_piece == 3:
                    self.piece = config.W_BISHOP
                elif promotion_piece == 4:
                    self.piece = config.W_KNIGHT
            elif self.player == config.PLAYER_2 and self.r_end == 7: # pawn promotion
                promotion_piece = eval(input("\n 1 ---> Queen \n 2 ---> Rook \n 3 ---> Bishop \n 4 ---> Knight \n: "))
                if promotion_piece == 1:
                    self.piece = config.B_QUEEN
                elif promotion_piece == 2:
                    self.piece = config.B_ROOK
                elif promotion_piece == 3:
                    self.piece = config.B_BISHOP
                elif promotion_piece == 4:
                    self.piece = config.B_KNIGHT
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

class Knight:
    def __init__(self, board, player):
        self.knight = 3
        self.player = player
        self.board = board
        self.temp_board = board.copy()
        if self.player == config.PLAYER_1:
            self.piece = config.W_KNIGHT
        elif self.player == config.PLAYER_2:
            self.piece = config.B_KNIGHT

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_knight_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
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
    def __init__(self, board, player):
        self.rook = 3
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        if self.player == config.PLAYER_1:
            self.piece = config.W_BISHOP
        elif self.player == config.PLAYER_2:
            self.piece = config.B_BISHOP

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_bishop_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
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
    def __init__(self, board, player, piece):
        self.rook = 5
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        self.piece = piece

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_rook_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True
        else:
            return self.board, False

class Queen:
    def __init__(self, board, player):
        self.rook = 9
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        if self.player == config.PLAYER_1:
            self.piece = config.W_QUEEN
        elif self.player == config.PLAYER_2:
            self.piece = config.B_QUEEN

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_queen_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True
        else:
            return self.board, False

class King:
    def __init__(self, board, player, can_castle_queenside, can_castle_kingside):
        self.rook = 1_000_000
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        self.can_castle_queenside = can_castle_queenside
        self.can_castle_kingside = can_castle_kingside
        if self.player == config.PLAYER_1:
            self.piece = config.W_KING
        elif self.player == config.PLAYER_2:
            self.piece = config.B_KING

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

    def move(self, r_start, c_start, r_end, c_end):
        self.r_start = r_start
        self.c_start = c_start
        self.r_end = r_end
        self.c_end = c_end

        if pm.is_valid_king_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board):
            self.temp_board[self.r_start, self.c_start] = config.EMPTY
            self.temp_board[self.r_end, self.c_end] = self.piece

            if check.is_check(self.player, self.temp_board):
                print(f'not a valid move {self.player} is in check!')
                return self.board, False

            elif not check.is_check(self.player, self.temp_board):
                self.board = self.temp_board
                return self.board, True

        elif cm.is_valid_castle(self.player, self.can_castle_queenside, self.can_castle_kingside, self.r_start, self.c_start, self.r_end, self.c_end, self.board) == 'kingside':
            self.board[self.r_start, self.c_start] = config.EMPTY
            self.board[self.r_start, self.c_start+3] = config.EMPTY
            if self.player == config.PLAYER_1:
                self.board[self.r_start, self.c_start+1] = config.W_KING_ROOK
            elif self.player == config.PLAYER_2:
                self.board[self.r_start, self.c_start+1] = config.B_KING_ROOK
            self.board[self.r_end, self.c_end] = self.piece
            return self.board, True

        elif cm.is_valid_castle(self.player, self.can_castle_queenside, self.can_castle_kingside, self.r_start, self.c_start, self.r_end, self.c_end, self.board) == 'queenside':
            self.board[self.r_start, self.c_start] = config.EMPTY
            self.board[self.r_start, self.c_start-4] = config.EMPTY
            if self.player == config.PLAYER_1:
                self.board[self.r_start, self.c_start-1] = config.W_KING_ROOK
            elif self.player == config.PLAYER_2:
                self.board[self.r_start, self.c_start-1] = config.B_KING_ROOK
            self.board[self.r_end, self.c_end] = self.piece
            return self.board, True

        else:
            return self.board, False

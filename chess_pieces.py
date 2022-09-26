import check, config
import piece_movement as pm
import castle_movement as cm

class Pieces:
    def __init__(self, board, player, prev_r_delta, prev_c_end, prev_moved_piece, piece, can_castle_queenside, can_castle_kingside):
        self.board = board
        self.temp_board = board.copy()
        self.player = player
        self.prev_r_delta = prev_r_delta
        self.prev_c_end = prev_c_end
        self.prev_moved_piece = prev_moved_piece
        self.piece = piece
        self.can_castle_queenside = can_castle_queenside
        self.can_castle_kingside = can_castle_kingside

        self.r_start = None
        self.c_start = None
        self.r_end = None
        self.c_end = None

        if self.piece == config.W_PAWN or self.piece == config.B_PAWN:
            self.piece_selector = self.Pawn(board, player, prev_r_delta, prev_c_end, prev_moved_piece, piece)
        elif self.piece == config.W_KNIGHT or self.piece == config.B_KNIGHT:
            self.piece_selector = self.Knight(board, player, piece)
        elif self.piece == config.W_BISHOP or self.piece == config.B_BISHOP:
            self.piece_selector = self.Bishop(board, player, piece)
        elif self.piece == config.W_QUEEN_ROOK or self.piece == config.W_KING_ROOK or self.piece == config.B_QUEEN_ROOK or self.piece == config.B_KING_ROOK:
            self.piece_selector = self.Rook(board, player, piece)
        elif self.piece == config.W_QUEEN or self.piece == config.B_QUEEN:
            self.piece_selector = self.Queen(board, player, piece)
        elif self.piece == config.W_KING or self.piece == config.B_KING:
            self.piece_selector = self.King(board, player, piece, can_castle_queenside, can_castle_kingside)

    class Pawn:
        def __init__(self, board, player, prev_r_delta, prev_c_end, prev_moved_piece, piece):
            self.value = 1
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.prev_r_delta = prev_r_delta
            self.prev_c_end = prev_c_end
            self.prev_moved_piece = prev_moved_piece
            self.piece = piece

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
        def __init__(self, board, player, piece):
            self.value = 3
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.piece = piece

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
        def __init__(self, board, player, piece):
            self.value = 3
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.piece = piece

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
            self.value = 5
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.piece = piece

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
        def __init__(self, board, player, piece):
            self.value = 9
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.piece = piece

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
        def __init__(self, board, player, piece, can_castle_queenside, can_castle_kingside):
            self.value = 1_000_000
            self.board = board
            self.temp_board = board.copy()
            self.player = player
            self.piece = piece
            self.can_castle_queenside = can_castle_queenside
            self.can_castle_kingside = can_castle_kingside

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
                self.temp_board[self.r_start, self.c_start] = config.EMPTY
                self.temp_board[self.r_start, self.c_start+3] = config.EMPTY
                if self.player == config.PLAYER_1:
                    self.temp_board[self.r_start, self.c_start+1] = config.W_KING_ROOK
                elif self.player == config.PLAYER_2:
                    self.temp_board[self.r_start, self.c_start+1] = config.B_KING_ROOK
                self.temp_board[self.r_end, self.c_end] = self.piece

                self.board = self.temp_board
                return self.board, True

            elif cm.is_valid_castle(self.player, self.can_castle_queenside, self.can_castle_kingside, self.r_start, self.c_start, self.r_end, self.c_end, self.board) == 'queenside':
                self.temp_board[self.r_start, self.c_start] = config.EMPTY
                self.temp_board[self.r_start, self.c_start-4] = config.EMPTY
                if self.player == config.PLAYER_1:
                    self.temp_board[self.r_start, self.c_start-1] = config.W_KING_ROOK
                elif self.player == config.PLAYER_2:
                    self.temp_board[self.r_start, self.c_start-1] = config.B_KING_ROOK
                self.temp_board[self.r_end, self.c_end] = self.piece

                self.board = self.temp_board
                return self.board, True

            else:
                return self.board, False

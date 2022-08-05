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

EMPTY = '00'

PLAYER_1 = 'white'
PLAYER_2 = 'black'

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
            if lambda : is_valid_pawn_move(self.piece, self.player, self.r_start, self.c_start, self.r_end, self.c_end, self.board, self.turn, self.prev_r_delta, self.prev_c_end, self.prev_moved_piece):
                self.board[self.r_start, self.c_start] = EMPTY
                self.board[self.r_end, self.c_end] = self.piece

        elif self.player == 'test':
            pass # move black pawn pieces
        return self.board


    def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board, turn, prev_r_delta, prev_c_end, prev_moved_piece):
        if player == PLAYER_1:
            if r_start == RANKS - 2: # checking pawns in their starting position
                if 0 < c_start < RANKS - 1:
                    if
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False

                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

                elif c_start == RANKS - 1:
                    if
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                        ):
                            return True
                        else:
                            return False

                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] != EMPTY and
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start-1] == EMPTY and
                    ):
                        if
                        (
                            r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == 0:
                    if
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False

                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] == EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 2 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start+1] != EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            (r_end == r_start - 1 and c_end == c_start) or
                        ):
                            return True
                        else:
                            return False
                    elif
                    (
                        board[r_start-1, c_start] == EMPTY and
                        board[r_start-2, c_start] != EMPTY and
                        board[r_start-1, c_start+1] == EMPTY
                    ):
                        if
                        (
                            r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

            elif r_start != RANKS - 2: # checking all other pawn non-starting positions (except promotion square)
                if r_start == 4 and prev_r_delta == 2 and prev_piece_moved == B_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
                    if 0 < c_start < RANKS - 1:
                        if prev_c_end - 1 == c_start:
                            if
                            (
                                board[r_start-1, c_start] == EMPTY and
                                board[r_start-1, c_start+1] == EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] == EMPTY and
                                board[r_start-1, c_start+1] != EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                                    (r_end == r_start - 1 and c_end == c_start + 1)
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                                board[r_start-1, c_start+1] == EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                                board[r_start-1, c_start+1] != EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                                    (r_end == r_start - 1 and c_end == c_start + 1)
                                ):
                                    return True
                                else:
                                    return False
                        elif prev_c_end + 1 == c_start:
                            if
                            (
                                board[r_start-1, c_start] == EMPTY and
                                board[r_start-1, c_start-1] == EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] == EMPTY and
                                board[r_start-1, c_start-1] != EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start + 1) or # en passant
                                    (r_end == r_start - 1 and c_end == c_start - 1)
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                                board[r_start-1, c_start-1] == EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                                board[r_start-1, c_start-1] != EMPTY
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start - 1) or
                                    (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                    elif c_start == RANKS - 1:
                        if prev_c_end - 1 == c_start:
                            if
                            (
                                board[r_start-1, c_start] == EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] == EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                                ):
                                    return True
                                else:
                                    return False
                    elif c_start == 0:
                        if prev_c_end + 1 == c_start:
                            if
                            (
                                board[r_start-1, c_start] == EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] == EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start) or
                                    (r_end == r_start - 1 and c_end == c_start + 1) or # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif
                            (
                                board[r_start-1, c_start] != EMPTY and
                            ):
                                if
                                (
                                    (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                else: # checking all but promotion square (en passant not possible)
                    if 0 < c_start < RANKS - 1:
                        pass
                    elif c_start == RANKS - 1:
                        pass
                    elif c_start == 0:
                        pass

            elif r_start == RANKS - 2: # checking if moving to promotion square (last rank)
                if 0 < c_start < RANKS - 1:
                    pass
                elif c_start == RANKS - 1:
                    pass
                elif c_start == 0:
                    pass



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

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

def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board, turn, prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        if r_start == RANKS - 2: # checking pawns in their starting position
            if 0 < c_start < RANKS - 1:
                if (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False

                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and                        (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    r_end == r_start - 1 and c_end == c_start
                    ):
                        return True
                    else:
                        return False
                else:
                    return False

            elif c_start == RANKS - 1:
                if (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False

                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] == EMPTY and board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start - 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                ):
                    if (
                    r_end == r_start - 1 and c_end == c_start
                    ):
                        return True
                    else:
                        return False
                else:
                    return False
            elif c_start == 0:
                if (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] == EMPTY and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 2 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start) or
                    (r_end == r_start - 1 and c_end == c_start + 1)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    (r_end == r_start - 1 and c_end == c_start)
                    ):
                        return True
                    else:
                        return False
                elif (
                board[r_start-1, c_start] == EMPTY and
                board[r_start-2, c_start] != EMPTY and
                (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                ):
                    if (
                    r_end == r_start - 1 and c_end == c_start
                    ):
                        return True
                    else:
                        return False
                else:
                    return False

        elif r_start != RANKS - 2: # checking all other pawn non-starting positions (except promotion square)
            if r_start == 3 and prev_r_delta == 2 and prev_piece_moved == B_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
                if 0 < c_start < RANKS - 1:
                    if prev_c_end - 1 == c_start:
                        if (
                        board[r_start-1, c_start] == EMPTY and
                        (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == EMPTY and
                        (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY and
                        (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY and
                        (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                    elif prev_c_end + 1 == c_start:
                        if (
                        board[r_start-1, c_start] == EMPTY and
                        (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == EMPTY and
                        (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1) or # en passant
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY and
                        (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY and
                        (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                            (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                            ):
                                return True
                            else:
                                return False
                elif c_start == RANKS - 1:
                    if prev_c_end - 1 == c_start:
                        if (
                        board[r_start-1, c_start] == EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                            board[r_start-1, c_start] != EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                            ):
                                return True
                            else:
                                return False
                elif c_start == 0:
                    if prev_c_end + 1 == c_start:
                        if (
                        board[r_start-1, c_start] == EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != EMPTY
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                            ):
                                return True
                            else:
                                return False
            else: # checking all but promotion square (en passant not possible)
                if 0 < c_start < RANKS - 1:
                    if (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False

                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == RANKS - 1:
                    if (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start-1] == EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == 0:
                    if (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if(
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == EMPTY and
                    (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

    elif player == PLAYER_2:
        pass
        # if r_start == 1: # checking pawns in their starting position
        #     if 0 < c_start < RANKS - 1:
        #         if
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values())) and                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values())) and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 r_end == r_start + 1 and c_end == c_start
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             return False
        #
        #     elif c_start == RANKS - 1:
        #         if
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY and board[r_start+1, c_start-1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start - 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 r_end == r_start + 1 and c_end == c_start
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             return False
        #     elif c_start == 0:
        #         if
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] == EMPTY and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 2 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #                 (r_end == r_start + 1 and c_end == c_start + 1)
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 (r_end == r_start + 1 and c_end == c_start) or
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         elif
        #         (
        #             board[r_start+1, c_start] == EMPTY and
        #             board[r_start+2, c_start] != EMPTY and
        #             (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['White'].values()))
        #         ):
        #             if
        #             (
        #                 r_end == r_start + 1 and c_end == c_start
        #             ):
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             return False
        #
        # elif r_start != 1: # checking all other pawn non-starting positions (except promotion square)
            # if r_start == 4 and prev_r_delta == 2 and prev_piece_moved == W_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
            #     if 0 < c_start < RANKS - 1:
            #         if prev_c_end - 1 == c_start:
            #             if
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #                 (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start - 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #                 (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
            #                     (r_end == r_start - 1 and c_end == c_start + 1)
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #                 (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #                 (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
            #                     (r_end == r_start - 1 and c_end == c_start + 1)
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #         elif prev_c_end + 1 == c_start:
            #             if
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #                 (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start + 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #                 (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start + 1) or # en passant
            #                     (r_end == r_start - 1 and c_end == c_start - 1)
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #                 (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #                 (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start - 1) or
            #                     (r_end == r_start - 1 and c_end == c_start + 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #     elif c_start == RANKS - 1:
            #         if prev_c_end - 1 == c_start:
            #             if
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start - 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start - 1) or # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #     elif c_start == 0:
            #         if prev_c_end + 1 == c_start:
            #             if
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start + 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] == EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start) or
            #                     (r_end == r_start - 1 and c_end == c_start + 1) or # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            #             elif
            #             (
            #                 board[r_start-1, c_start] != EMPTY and
            #             ):
            #                 if
            #                 (
            #                     (r_end == r_start - 1 and c_end == c_start + 1) # en passant
            #                 ):
            #                     return True
            #                 else:
            #                     return False
            # else: # checking all but promotion square (en passant not possible)
                # if 0 < c_start < RANKS - 1:
                #     if
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1) or
                #             (r_end == r_start - 1 and c_end == c_start + 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start + 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1) or
                #             (r_end == r_start - 1 and c_end == c_start + 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start + 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         board[r_start-1, c_start-1] == EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #         (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             r_end == r_start - 1 and c_end == c_start
                #         ):
                #             return True
                #         else:
                #             return False
                #     else:
                #         return False
                # elif c_start == RANKS - 1:
                #     if
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] == EMPTY or board[r_start-1, c_start-1] in list(PIECES['White'].values())) and
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         (board[r_start-1, c_start-1] != EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values()))
                #     ):
                #         if
                #         (
                #             (r_end == r_start - 1 and c_end == c_start) or
                #             (r_end == r_start - 1 and c_end == c_start - 1)
                #         ):
                #             return True
                #         else:
                #             return False
                #     elif
                #     (
                #         board[r_start-1, c_start] == EMPTY and
                #         board[r_start-1, c_start-1] == EMPTY and board[r_start-1, c_start-1] not in list(PIECES['White'].values())) and
                #     ):
                #         if
                #         (
                #             r_end == r_start - 1 and c_end == c_start
                #         ):
                #             return True
                #         else:
                #             return False
                #     else:
                #         return False
                # elif c_start == 0:
                    # if
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #         (r_end == r_start - 1 and c_end == c_start + 1)
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    #
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #         (r_end == r_start - 1 and c_end == c_start + 1)
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start)
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #         (r_end == r_start - 1 and c_end == c_start + 1)
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] != EMPTY and board[r_start-1, c_start+1] not in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #         (r_end == r_start - 1 and c_end == c_start + 1)
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         (r_end == r_start - 1 and c_end == c_start) or
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # elif
                    # (
                    #     board[r_start-1, c_start] == EMPTY and
                    #     (board[r_start-1, c_start+1] == EMPTY or board[r_start-1, c_start+1] in list(PIECES['White'].values()))
                    # ):
                    #     if
                    #     (
                    #         r_end == r_start - 1 and c_end == c_start
                    #     ):
                    #         return True
                    #     else:
                    #         return False
                    # else:
                    #     return False


        # I don't think I need this check
        # elif r_start == RANKS - 2: # checking if moving to promotion square (last rank)
        #     if 0 < c_start < RANKS - 1:
        #         pass
        #     elif c_start == RANKS - 1:
        #         pass
        #     elif c_start == 0:
        #         pass

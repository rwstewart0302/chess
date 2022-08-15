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

### TODO
### - FIX ALL SYNTAX ERRORS IN IF STATEMENTS ###
### - CHANGE r_start - 1 to r_start + 1 for player_2
### - CHANGE PIECES['White'] to PIECES['Black'] for player_2
### - ADD CHECK AND CHECKMATE CONDITIONS using check.is_check() and check.is_checkmate() to player_1 and player_2


def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    try:
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
            if r_start == 1: # checking pawns in their starting position
                if 0 < c_start < RANKS - 1:
                    if (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False

                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

                elif c_start == RANKS - 1:
                    if (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False

                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY and board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == 0:
                    if (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] == EMPTY and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == EMPTY and
                    board[r_start+2, c_start] != EMPTY and
                    (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

            elif r_start != 1: # checking all other pawn non-starting positions (except promotion square)
                if r_start == 4 and prev_r_delta == 2 and prev_piece_moved == W_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
                    if 0 < c_start < RANKS - 1:
                        if prev_c_end - 1 == c_start:
                            if (
                            board[r_start+1, c_start] == EMPTY and
                            (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] == EMPTY and
                            (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start - 1) or # en passant
                                (r_end == r_start + 1 and c_end == c_start + 1)
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY and
                            (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY and
                            (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1) or # en passant
                                (r_end == r_start + 1 and c_end == c_start + 1)
                                ):
                                    return True
                                else:
                                    return False
                        elif prev_c_end + 1 == c_start:
                            if (
                            board[r_start+1, c_start] == EMPTY and
                            (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] == EMPTY and
                            (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start + 1) or # en passant
                                (r_end == r_start + 1 and c_end == c_start - 1)
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY and
                            (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY and
                            (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1) or
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                    elif c_start == RANKS - 1:
                        if prev_c_end - 1 == c_start:
                            if (
                            board[r_start+1, c_start] == EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                    elif c_start == 0:
                        if prev_c_end + 1 == c_start:
                            if (
                            board[r_start+1, c_start] == EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return True
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return True
                                else:
                                    return False
                else: # checking all but promotion square (en passant not possible)
                    if 0 < c_start < RANKS - 1:
                        if (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False

                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values())) and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            r_end == r_start + 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == RANKS - 1:
                        if (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False

                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY or board[r_start+1, c_start-1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] != EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start-1] == EMPTY and board[r_start+1, c_start-1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            r_end == r_start + 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == 0:
                        if (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False

                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] != EMPTY and board[r_start+1, c_start+1] not in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == EMPTY and
                        (board[r_start+1, c_start+1] == EMPTY or board[r_start+1, c_start+1] in list(PIECES['Black'].values()))
                        ):
                            if (
                            r_end == r_start + 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
    except IndexError:
        return False

def is_valid_knight_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        if 2 <= r_start <= 5:
            if 2 <= c_start <= 5:
                pass

def is_valid_bishop_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        pass
    elif player == PLAYER_2:
        pass

def is_valid_rook_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        pass
    elif player == PLAYER_2:
        pass

def is_valid_queen_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        pass
    elif player == PLAYER_2:
        pass

def is_valid_king_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == PLAYER_1:
        pass
    elif player == PLAYER_2:
        pass

def is_valid_check_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    pass
    # if piece == 'test'
    # if is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece)

import config

### TODO
### - MIGHT BE ABLE TO SIMPLIFY PAWN MOVEMENT BECAUSE OF TRY/EXCEPT...TRY CUTTING DOWN ON CONDITIONALS

def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    try:
        if player == config.PLAYER_1:
            if r_start == config.RANKS - 2: # checking pawns in their starting position
                if 0 < c_start < config.RANKS - 1:
                    if (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start - 1) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

                elif c_start == config.RANKS - 1:
                    if (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY and board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] != config.EMPTY and
                    (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start - 1
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == 0:
                    if (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] == config.EMPTY and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start) or
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] == config.EMPTY and
                    board[r_start-2, c_start] != config.EMPTY and
                    (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                    ):
                        if (
                        r_end == r_start - 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start-1, c_start] != config.EMPTY and
                    (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                    ):
                        if (
                        (r_end == r_start - 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

            elif r_start != config.RANKS - 2: # checking all other pawn non-starting positions (except promotion square)
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.B_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
                    if 0 < c_start < config.RANKS - 1:
                        if prev_c_end + 1 == c_start:
                            if (
                            board[r_start-1, c_start] == config.EMPTY and
                            (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] == config.EMPTY and
                            (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start) or
                                (r_end == r_start - 1 and c_end == c_start + 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY and
                            (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY and
                            (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start + 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                        elif prev_c_end - 1 == c_start:
                            if (
                            board[r_start-1, c_start] == config.EMPTY and
                            (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] == config.EMPTY and
                            (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start) or
                                (r_end == r_start - 1 and c_end == c_start - 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY and
                            (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY and
                            (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start - 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                    elif c_start == config.RANKS - 1:
                        if prev_c_end + 1 == c_start:
                            if (
                            board[r_start-1, c_start] == config.EMPTY
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                    elif c_start == 0:
                        if prev_c_end - 1 == c_start:
                            if (
                            board[r_start-1, c_start] == config.EMPTY
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start - 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start-1, c_start] != config.EMPTY
                            ):
                                if (
                                (r_end == r_start - 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False

                else: # checking all but promotion square (en passant not possible)
                    if 0 < c_start < config.RANKS - 1:
                        if (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
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
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            r_end == r_start - 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES) and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == config.RANKS - 1:
                        if (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start-1] == config.EMPTY or board[r_start-1, c_start-1] in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != config.EMPTY and
                        (board[r_start-1, c_start-1] != config.EMPTY and board[r_start-1, c_start-1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == 0:
                        if (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start) or
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] == config.EMPTY and
                        (board[r_start-1, c_start+1] == config.EMPTY or board[r_start-1, c_start+1] in config.PLAYER_1_PIECES)
                        ):
                            if(
                            (r_end == r_start - 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start-1, c_start] != config.EMPTY and
                        (board[r_start-1, c_start+1] != config.EMPTY and board[r_start-1, c_start+1] not in config.PLAYER_1_PIECES)
                        ):
                            if (
                            (r_end == r_start - 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False

        elif player == config.PLAYER_2:
            if r_start == 1: # checking pawns in their starting position
                if 0 < c_start < config.RANKS - 1:
                    if (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start - 1) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

                elif c_start == config.RANKS - 1:
                    if (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY and board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start - 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] != config.EMPTY and
                    (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start - 1
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif c_start == 0:
                    if (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] == config.EMPTY and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 2 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start) or
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start)
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] == config.EMPTY and
                    board[r_start+2, c_start] != config.EMPTY and
                    (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                    ):
                        if (
                        r_end == r_start + 1 and c_end == c_start
                        ):
                            return True
                        else:
                            return False
                    elif (
                    board[r_start+1, c_start] != config.EMPTY and
                    (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                    ):
                        if (
                        (r_end == r_start + 1 and c_end == c_start + 1)
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False

            elif r_start != 1: # checking all other pawn non-starting positions (except promotion square)
                if r_start == 4 and prev_r_delta == 2 and prev_moved_piece == config.W_PAWN and (prev_c_end - 1 == c_start or prev_c_end + 1 == c_start): # en passant
                    if 0 < c_start < config.RANKS - 1:
                        if prev_c_end + 1 == c_start:
                            if (
                            board[r_start+1, c_start] == config.EMPTY and
                            (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] == config.EMPTY and
                            (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start + 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY and
                            (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY and
                            (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start + 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                        elif prev_c_end - 1 == c_start:
                            if (
                            board[r_start+1, c_start] == config.EMPTY and
                            (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] == config.EMPTY and
                            (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_star-1] not in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start) or
                                (r_end == r_start + 1 and c_end == c_start - 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY and
                            (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY and
                            (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                    elif c_start == config.RANKS - 1:
                        if prev_c_end + 1 == c_start:
                            if (
                            board[r_start+1, c_start] == config.EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start)
                                ):
                                    return True
                                elif(
                                (r_end == r_start + 1 and c_end == c_start - 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start - 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                    elif c_start == 0:
                        if prev_c_end - 1 == c_start:
                            if (
                            board[r_start+1, c_start] == config.EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start)
                                ):
                                    return True
                                elif (
                                (r_end == r_start + 1 and c_end == c_start + 1) # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            elif (
                            board[r_start+1, c_start] != config.EMPTY
                            ):
                                if (
                                (r_end == r_start + 1 and c_end == c_start + 1)  # en passant
                                ):
                                    return 'en passant'
                                else:
                                    return False
                            else:
                                return False
                else: # checking all but promotion square (en passant not possible)
                    if 0 < c_start < config.RANKS - 1:
                        if (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
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
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            r_end == r_start + 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] != config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] != config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start - 1) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] != config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES) and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == config.RANKS - 1:
                        if (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False

                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start-1] == config.EMPTY or board[r_start+1, c_start-1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] != config.EMPTY and
                        (board[r_start+1, c_start-1] != config.EMPTY and board[r_start+1, c_start-1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start - 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif c_start == 0:
                        if (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start) or
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] == config.EMPTY and
                        (board[r_start+1, c_start+1] == config.EMPTY or board[r_start+1, c_start+1] in config.PLAYER_2_PIECES)
                        ):
                            if (
                            r_end == r_start + 1 and c_end == c_start
                            ):
                                return True
                            else:
                                return False
                        elif (
                        board[r_start+1, c_start] != config.EMPTY and
                        (board[r_start+1, c_start+1] != config.EMPTY and board[r_start+1, c_start+1] not in config.PLAYER_2_PIECES)
                        ):
                            if (
                            (r_end == r_start + 1 and c_end == c_start + 1)
                            ):
                                return True
                            else:
                                return False
                        else:
                            return False
    except IndexError:
        return False

def is_valid_knight_move(piece, player, r_start, c_start, r_end, c_end, board):
    try:
        if player == config.PLAYER_1:
            if r_end == r_start - 2 and c_end == c_start + 1:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start - 2 and c_end == c_start - 1:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start + 2 and c_end == c_start + 1:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start + 2 and c_end == c_start - 1:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start + 1 and c_end == c_start - 2:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start - 1 and c_end == c_start - 2:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start + 1 and c_end == c_start + 2:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            elif r_end == r_start - 1 and c_end == c_start + 2:
                if board[r_end, c_end] not in config.PLAYER_1_PIECES:
                    return True
            else:
                return False

        elif player == config.PLAYER_2:
            if r_end == r_start - 2 and c_end == c_start + 1:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start - 2 and c_end == c_start - 1:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start + 2 and c_end == c_start + 1:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start + 2 and c_end == c_start - 1:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start + 1 and c_end == c_start - 2:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start - 1 and c_end == c_start - 2:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start + 1 and c_end == c_start + 2:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            elif r_end == r_start - 1 and c_end == c_start + 2:
                if board[r_end, c_end] not in config.PLAYER_2_PIECES:
                    return True
            else:
                return False

    except IndexError:
        return False

def is_valid_bishop_move(piece, player, r_start, c_start, r_end, c_end, board):
    try:
        if player == config.PLAYER_1:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_2_PIECES:
                    if r_end < r_start and c_end > c_start:
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end > c_start:
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end < c_start:
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end < c_start:
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False

                    else:
                        return False
                else:
                    return False

        elif player == config.PLAYER_2:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_1_PIECES:
                    if r_end < r_start and c_end > c_start:
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end > c_start:
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end < c_start:
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end < c_start:
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

    except IndexError:
        return False

def is_valid_rook_move(piece, player, r_start, c_start, r_end, c_end, board):
    try:
        if player == config.PLAYER_1:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_2_PIECES:
                    if r_end == r_start and c_end > c_start:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

        elif player == config.PLAYER_2:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_1_PIECES:
                    if r_end == r_start and c_end > c_start:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

    except IndexError:
        return False

def is_valid_queen_move(piece, player, r_start, c_start, r_end, c_end, board):
    try:
        if player == config.PLAYER_1:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_2_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start:
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end > c_start:
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end < c_start:
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False
                    elif r_end < r_start and c_end < c_start:
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

        elif player == config.PLAYER_2:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_1_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start:
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end > c_start:
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end < c_start:
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False
                    elif r_end < r_start and c_end < c_start:
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

    except IndexError:
        return False

def is_valid_king_move(piece, player, r_start, c_start, r_end, c_end, board):
    try:
        if player == config.PLAYER_1:
            for i in range(config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_2_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start and (r_end == r_start - 1 and c_end == c_start + 1):
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end > c_start and (r_end == r_start + 1 and c_end == c_start + 1):
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end < c_start and (r_end == r_start + 1 and c_end == c_start - 1):
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False
                    elif r_end < r_start and c_end < c_start and (r_end == r_start - 1 and c_end == c_start - 1):
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start and c_end == c_start + 1:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start and c_end == c_start - 1:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start and r_end == r_start + 1:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start and r_end == r_start - 1:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

        elif player == config.PLAYER_2:
            for i in range(1, config.RANKS):
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_1_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start and (r_end == r_start - 1 and c_end == c_start + 1):
                        if board[r_end+i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end+i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end > c_start and (r_end == r_start + 1 and c_end == c_start + 1):
                        if board[r_end-i, c_end-i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end-i, c_end-i] != config.EMPTY:
                            return False
                    elif r_end > r_start and c_end < c_start and (r_end == r_start + 1 and c_end == c_start - 1):
                        if board[r_end-i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end-i, c_end+i] != config.EMPTY:
                            return False
                    elif r_end < r_start and c_end < c_start and (r_end == r_start - 1 and c_end == c_start - 1):
                        if board[r_end+i, c_end+i] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end+i, c_end+i] != config.EMPTY:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start and c_end == c_start + 1:
                        if board[r_end, c_end-i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end-i == c_start:
                            return True
                        elif board[r_end, c_end-i] != config.EMPTY:
                            return False

                    elif r_end == r_start and c_end < c_start and c_end == c_start - 1:
                        if board[r_end, c_end+i] == config.EMPTY:
                            pass
                        elif r_end == r_start and c_end+i == c_start:
                            return True
                        elif board[r_end, c_end+i] != config.EMPTY:
                            return False

                    elif r_end > r_start and c_end == c_start and r_end == r_start + 1:
                        if board[r_end-i, c_end] == config.EMPTY:
                            pass
                        elif r_end-i == r_start and c_end == c_start:
                            return True
                        elif board[r_end-i, c_end] != config.EMPTY:
                            return False

                    elif r_end < r_start and c_end == c_start and r_end == r_start - 1:
                        if board[r_end+i, c_end] == config.EMPTY:
                            pass
                        elif r_end+i == r_start and c_end == c_start:
                            return True
                        elif board[r_end+i, c_end] != config.EMPTY:
                            return False
                    else:
                        return False
                else:
                    return False

    except IndexError:
        return False

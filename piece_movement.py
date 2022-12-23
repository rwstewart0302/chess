import config

def is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if player == config.PLAYER_1:
        # capturing pieces
        if c_start != c_end:
            if 0 < c_start < 7:
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.B_PAWN:
                    if prev_c_end == c_start - 1: # en passant left
                        if r_end == r_start - 1 and c_end == c_start - 1:
                            return 'en passant'
                    elif prev_c_end == c_start + 1: # en passant right
                        if r_end == r_start - 1 and c_end == c_start + 1:
                            return 'en passant'
                if board[r_start - 1, c_start - 1] in config.PLAYER_2_PIECES:
                    return (r_end == r_start - 1 and c_end == c_start - 1) # capture left
                if board[r_start - 1, c_start + 1] in config.PLAYER_2_PIECES:
                    return (r_end == r_start - 1 and c_end == c_start + 1) # capture right
                    

            elif c_start == 0:
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.B_PAWN:
                    if prev_c_end == c_start + 1: # en passant right
                        if r_end == r_start - 1 and c_end == c_start + 1:
                            return 'en passant'
                if board[r_start - 1, c_start + 1] in config.PLAYER_2_PIECES:
                    return (r_end == r_start - 1 and c_end == c_start + 1)
            
            elif c_start == 7:
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.B_PAWN:
                    if prev_c_end == c_start - 1: # en passant left
                        if r_end == r_start - 1 and c_end == c_start - 1:
                            return 'en passant'
                if board[r_start - 1, c_start - 1] in config.PLAYER_2_PIECES:
                    return (r_end == r_start - 1 and c_end == c_start - 1)
        
        # forward movement
        elif c_end == c_start:
            if r_start == 6:
                if (
                    board[r_start - 2, c_start] == config.EMPTY and
                    board[r_start - 1, c_start] == config.EMPTY
                ):
                    return (r_end == r_start - 2) or (r_end == r_start - 1)
            if board[r_start - 1, c_start] == config.EMPTY:
                return r_end == r_start - 1


    elif player == config.PLAYER_2:      
        # capturing pieces
        if c_start != c_end:
            if 0 < c_start < 7:
                if r_start == 4 and prev_r_delta == 2 and prev_moved_piece == config.W_PAWN:
                    if prev_c_end == c_start - 1: # en passant left
                        if r_end == r_start + 1 and c_end == c_start - 1:
                            return 'en passant'
                    elif prev_c_end == c_start + 1: # en passant right
                        if r_end == r_start + 1 and c_end == c_start + 1:
                            return 'en passant'

                if board[r_start + 1, c_start - 1] in config.PLAYER_1_PIECES:
                    return (r_end == r_start + 1 and c_end == c_start - 1) # capture left
                if board[r_start + 1, c_start + 1] in config.PLAYER_1_PIECES:
                    return (r_end == r_start + 1 and c_end == c_start + 1) # capture right
            
            elif c_start == 0:
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.W_PAWN:
                    if prev_c_end == c_start + 1: # en passant right
                        if r_end == r_start + 1 and c_end == c_start + 1:
                            return 'en passant'
                if board[r_start + 1, c_start + 1] in config.PLAYER_1_PIECES:
                    return (r_end == r_start + 1 and c_end == c_start + 1)
            
            elif c_start == 7:
                if r_start == 3 and prev_r_delta == 2 and prev_moved_piece == config.W_PAWN:
                    if prev_c_end == c_start - 1: # en passant left
                        if r_end == r_start + 1 and c_end == c_start - 1:
                            return 'en passant'

                if board[r_start + 1, c_start - 1] in config.PLAYER_1_PIECES:
                    return (r_end == r_start + 1 and c_end == c_start - 1)

        # forward movement
        elif c_end == c_start:
            if r_start == 1:
                if (
                    board[r_start + 2, c_start] == config.EMPTY and
                    board[r_start + 1, c_start] == config.EMPTY
                ):
                    return (r_end == r_start + 2) or (r_end == r_start + 1)
            if board[r_start + 1, c_start] == config.EMPTY:
                return r_end == r_start + 1


def is_valid_knight_move(piece, player, r_start, c_start, r_end, c_end, board):
    if r_end >= 0 and c_end >= 0:
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
    else:
        return False

def is_valid_bishop_move(piece, player, r_start, c_start, r_end, c_end, board):
    if r_end >= 0 and c_end >= 0:
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
    else:
        return False

def is_valid_rook_move(piece, player, r_start, c_start, r_end, c_end, board):
    if r_end >= 0 and c_end >= 0:
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
    else:
        return False

def is_valid_queen_move(piece, player, r_start, c_start, r_end, c_end, board):
    if r_end >= 0 and c_end >= 0:
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
    else:
        return False

def is_valid_king_move(piece, player, r_start, c_start, r_end, c_end, board):
    if r_end >= 0 and c_end >= 0:
        try:
            if player == config.PLAYER_1:
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_2_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start:
                        if r_end == r_start - 1 and c_end == c_start + 1:
                            return True
                        else:
                            return False
                    elif r_end > r_start and c_end > c_start:
                        if r_end == r_start + 1 and c_end == c_start + 1:
                            return True
                        else:
                            return False

                    elif r_end > r_start and c_end < c_start:
                        if r_end == r_start + 1 and c_end == c_start - 1:
                            return True
                        else:
                            return False

                    elif r_end < r_start and c_end < c_start:
                        if r_end == r_start - 1 and c_end == c_start - 1:
                            return True
                        else:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start:
                        if c_end == c_start + 1:
                            return True
                        else:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if c_end == c_start - 1:
                            return True
                        else:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if r_end == r_start + 1:
                            return True
                        else:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if r_end == r_start - 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            elif player == config.PLAYER_2:
                if board[r_end, c_end] == config.EMPTY or board[r_end, c_end] in config.PLAYER_1_PIECES:
                # diagonal movement
                    if r_end < r_start and c_end > c_start:
                        if r_end == r_start - 1 and c_end == c_start + 1:
                            return True
                        else:
                            return False

                    elif r_end > r_start and c_end > c_start:
                        if r_end == r_start + 1 and c_end == c_start + 1:
                            return True
                        else:
                            return False

                    elif r_end > r_start and c_end < c_start:
                        if r_end == r_start + 1 and c_end == c_start - 1:
                            return True
                        else:
                            return False
                    elif r_end < r_start and c_end < c_start:
                        if r_end == r_start - 1 and c_end == c_start - 1:
                            return True
                        else:
                            return False

                # horizontal or vertical movement
                    elif r_end == r_start and c_end > c_start:
                        if c_end == c_start + 1:
                            return True
                        else:
                            return False

                    elif r_end == r_start and c_end < c_start:
                        if c_end == c_start - 1:
                            return True
                        else:
                            return False

                    elif r_end > r_start and c_end == c_start:
                        if r_end == r_start + 1:
                            return True
                        else:
                            return False

                    elif r_end < r_start and c_end == c_start:
                        if r_end == r_start - 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

        except IndexError:
            return False
    else:
        return False

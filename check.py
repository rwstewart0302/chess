import config
import numpy as np
import piece_movement as pm

prev_r_delta = 0
prev_c_end = 0
prev_moved_piece = config.EMPTY

def is_check(player, board):
    if player == config.PLAYER_1:
        index_king = np.where(board == config.W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        piece = config.B_PAWN
        pawn_index = np.where(board == piece)
        r_pawn = list(pawn_index[0])
        c_pawn = list(pawn_index[1])
        for r_start, c_start in zip(r_pawn, c_pawn):
            if pm.is_valid_pawn_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                return True
            else:
                pass

        piece = config.B_KNIGHT
        knight_index = np.where(board == piece) # knight check
        r_knight = list(knight_index[0])
        c_knight = list(knight_index[1])
        for r_start, c_start in zip(r_knight, c_knight):
            if pm.is_valid_knight_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.B_BISHOP
        bishop_index = np.where(board == piece) # bishop check
        r_bishop = list(bishop_index[0])
        c_bishop = list(bishop_index[1])
        for r_start, c_start in zip(r_bishop, c_bishop):
            if pm.is_valid_bishop_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.B_QUEEN_ROOK
        rook_index = np.where(board == piece) # rook check
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            if pm.is_valid_rook_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.B_KING_ROOK
        rook_index = np.where(board == piece) # rook check
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            if pm.is_valid_rook_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass


        piece = config.B_QUEEN
        queen_index = np.where(board == piece) # rook check
        r_queen = list(queen_index[0])
        c_queen = list(queen_index[1])
        for r_start, c_start in zip(r_queen, c_queen):
            if pm.is_valid_queen_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.B_KING
        king_index = np.where(board == piece) # rook check
        r_king_b = list(king_index[0])
        c_king_b = list(king_index[1])
        for r_start, c_start in zip(r_king_b, c_king_b):
            if pm.is_valid_king_move(piece, config.PLAYER_2, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        return False

    if player == config.PLAYER_2:
        # checking if config.PLAYER_2's king is in check
        index_king = np.where(board == config.B_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        piece = config.W_PAWN
        pawn_index = np.where(board == piece)
        r_pawn = list(pawn_index[0])
        c_pawn = list(pawn_index[1])
        for r_start, c_start in zip(r_pawn, c_pawn):
            if pm.is_valid_pawn_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                return True
            else:
                pass

        piece = config.W_KNIGHT
        knight_index = np.where(board == piece) # knight check
        r_knight = list(knight_index[0])
        c_knight = list(knight_index[1])
        for r_start, c_start in zip(r_knight, c_knight):
            if pm.is_valid_knight_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.W_BISHOP
        bishop_index = np.where(board == piece) # bishop check
        r_bishop = list(bishop_index[0])
        c_bishop = list(bishop_index[1])
        for r_start, c_start in zip(r_bishop, c_bishop):
            if pm.is_valid_bishop_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.W_QUEEN_ROOK
        rook_index = np.where(board == piece) # rook check
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            if pm.is_valid_rook_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.W_KING_ROOK
        rook_index = np.where(board == piece) # rook check
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            if pm.is_valid_rook_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.W_QUEEN
        queen_index = np.where(board == piece) # rook check
        r_queen = list(queen_index[0])
        c_queen = list(queen_index[1])
        for r_start, c_start in zip(r_queen, c_queen):
            if pm.is_valid_queen_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        piece = config.W_KING
        king_index = np.where(board == piece) # rook check
        r_king_w = list(king_index[0])
        c_king_w = list(king_index[1])
        for r_start, c_start in zip(r_king_w, c_king_w):
            if pm.is_valid_king_move(piece, config.PLAYER_1, r_start, c_start, r_king, c_king, board):
                return True
            else:
                pass

        return False


def is_game_over(player, board):
    if player == config.PLAYER_1:
        index_king = np.where(board == config.W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        # pawn check
        piece = config.W_PAWN
        pawn_index = np.where(board == piece)
        r_pawn = list(pawn_index[0])
        c_pawn = list(pawn_index[1])
        for r_start, c_start in zip(r_pawn, c_pawn):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_pawn_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_pawn_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass

        # knight check
        piece = config.W_KNIGHT
        knight_index = np.where(board == piece)
        r_knight = list(knight_index[0])
        c_knight = list(knight_index[1])
        for r_start, c_start in zip(r_knight, c_knight):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        # bishop check
        piece = config.W_BISHOP
        bishop_index = np.where(board == piece)
        r_bishop = list(bishop_index[0])
        c_bishop = list(bishop_index[1])
        for r_start, c_start in zip(r_bishop, c_bishop):
            for i in range(config.RANKS):
                if pm.is_valid_bishop_move(piece, player, r_start, c_start, r_start+i, c_start+i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start+i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_bishop_move(piece, player, r_start, c_start, r_start-i, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start-i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                else:
                    pass

        # rook check
        piece = config.W_QUEEN_ROOK
        rook_index = np.where(board == piece)
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            for i in range(config.RANKS):
                if pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start+i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start-i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                    except IndexError:
                        pass
                else:
                    pass

        piece = config.W_KING_ROOK
        rook_index = np.where(board == piece)
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            for i in range(config.RANKS):
                if pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start+i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start-i] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start] = piece
                        if config.W_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                    except IndexError:
                        pass
                else:
                    pass

        # queen check
        piece = config.W_QUEEN
        queen_index = np.where(board == piece)
        r_queen = list(queen_index[0])
        c_queen = list(queen_index[1])
        for r_start, c_start in zip(r_queen, c_queen):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        # king check
        piece = config.W_KING
        king_index = np.where(board == piece)
        r_king = list(king_index[0])
        c_king = list(king_index[1])
        for r_start, c_start in zip(r_king, c_king):
            for r in range(2):
                for c in range(2):
                    if pm.is_valid_king_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.W_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        return True


    elif player == config.PLAYER_2:
        index_king = np.where(board == config.B_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        # pawn check
        piece = config.B_PAWN
        pawn_index = np.where(board == piece)
        r_pawn = list(pawn_index[0])
        c_pawn = list(pawn_index[1])
        for r_start, c_start in zip(r_pawn, c_pawn):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_pawn_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_pawn_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        # knight check
        piece = config.B_KNIGHT
        knight_index = np.where(board == piece)
        r_knight = list(knight_index[0])
        c_knight = list(knight_index[1])
        for r_start, c_start in zip(r_knight, c_knight):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        # bishop check
        piece = config.B_BISHOP
        bishop_index = np.where(board == piece)
        r_bishop = list(bishop_index[0])
        c_bishop = list(bishop_index[1])
        for r_start, c_start in zip(r_bishop, c_bishop):
            for i in range(config.RANKS):
                if pm.is_valid_bishop_move(piece, player, r_start, c_start, r_start+i, c_start+i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start+i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_bishop_move(piece, player, r_start, c_start, r_start-i, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start-i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                else:
                    pass

        # rook check
        piece = config.B_QUEEN_ROOK
        rook_index = np.where(board == piece)
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            for i in range(config.RANKS):
                if pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start+i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start-i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                else:
                    pass

        piece = config.B_KING_ROOK
        rook_index = np.where(board == piece)
        r_rook = list(rook_index[0])
        c_rook = list(rook_index[1])
        for r_start, c_start in zip(r_rook, c_rook):
            for i in range(config.RANKS):
                if pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board):
                    print('black king rook move?')
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start+i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start, c_start-i] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start+i, c_start] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                elif pm.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board):
                    try:
                        t_board = board.copy()
                        t_board[r_start, c_start] = config.EMPTY
                        t_board[r_start-i, c_start] = piece
                        if config.B_KING in t_board:
                            if not is_check(player, t_board):
                                return False
                        else:
                            pass
                    except IndexError:
                        pass
                else:
                    pass

        # queen check
        piece = config.B_QUEEN
        queen_index = np.where(board == piece)
        r_queen = list(queen_index[0])
        c_queen = list(queen_index[1])
        for r_start, c_start in zip(r_queen, c_queen):
            for r in range(config.RANKS):
                for c in range(config.FILES):
                    if pm.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        # king check
        piece = config.B_KING
        king_index = np.where(board == piece)
        r_king = list(king_index[0])
        c_king = list(king_index[1])
        for r_start, c_start in zip(r_king, c_king):
            for r in range(2):
                for c in range(2):
                    if pm.is_valid_king_move(piece, player, r_start, c_start, r_start+r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start+r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start+r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start-r, c_start+c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start+c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    elif pm.is_valid_king_move(piece, player, r_start, c_start, r_start-r, c_start-c, board):
                        try:
                            t_board = board.copy()
                            t_board[r_start, c_start] = config.EMPTY
                            t_board[r_start-r, c_start-c] = piece
                            if config.B_KING in t_board:
                                if not is_check(player, t_board):
                                    return False
                            else:
                                pass
                        except IndexError:
                            pass
                    else:
                        pass

        return True

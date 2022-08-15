import numpy as np

import piece_movement as py

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

prev_r_delta = 0
prev_c_end = 0
prev_moved_piece = EMPTY

def is_check(player, board):
    # checking if player_1's king is in check
    if player == PLAYER_1:
        index_king = np.where(board == W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        if r_king > 1: # checking for pawn checks
            piece = B_PAWN
            pawn_index = np.where(board == piece)
            r_pawn = list(pawn_index[0])
            c_pawn = list(pawn_index[1])
            for r_start, c_start in zip(r_pawn, c_pawn):
                if py.is_valid_pawn_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

        else: # check for all other piece checks
            piece = B_KNIGHT
            knight_index = np.where(board == piece) # knight check
            r_knight = list(knight_index[0])
            c_knight = list(knight_index[1])
            for r_start, c_start in zip(r_knight, c_knight):
                if py.is_valid_knight_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board):
                    return True
                else:
                    pass

            piece = B_BISHOP
            bishop_index = np.where(board == piece) # bishop check
            r_bishop = list(bishop_index[0])
            c_bishop = list(bishop_index[1])
            for r_start, c_start in zip(r_bishop, c_bishop):
                if py.is_valid_bishop_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

            piece = B_ROOK
            rook_index = np.where(board == piece) # rook check
            r_rook = list(rook_index[0])
            c_rook = list(rook_index[1])
            for r_start, c_start in zip(r_rook, c_rook):
                if py.is_valid_rook_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

            piece = B_QUEEN
            queen_index = np.where(board == piece) # rook check
            r_queen = list(queen_index[0])
            c_queen = list(queen_index[1])
            for r_start, c_start in zip(r_queen, c_queen):
                if py.is_valid_queen_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

        return False

    if player == PLAYER_2:
        # checking if player_2's king is in check
        index_king = np.where(board == B_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

        if r_king < 6: # checking for pawn checks
            piece = W_PAWN
            pawn_index = np.where(board == piece)
            r_pawn = list(pawn_index[0])
            c_pawn = list(pawn_index[1])
            for r_start, c_start in zip(r_pawn, c_pawn):
                if py.is_valid_pawn_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

        else: # check for all other piece checks
            piece = W_KNIGHT
            knight_index = np.where(board == piece) # knight check
            r_knight = list(knight_index[0])
            c_knight = list(knight_index[1])
            for r_start, c_start in zip(r_knight, c_knight):
                if py.is_valid_knight_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board):
                    return True
                else:
                    pass

            piece = W_BISHOP
            bishop_index = np.where(board == piece) # bishop check
            r_bishop = list(bishop_index[0])
            c_bishop = list(bishop_index[1])
            for r_start, c_start in zip(r_bishop, c_bishop):
                if py.is_valid_bishop_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

            piece = W_ROOK
            rook_index = np.where(board == piece) # rook check
            r_rook = list(rook_index[0])
            c_rook = list(rook_index[1])
            for r_start, c_start in zip(r_rook, c_rook):
                if py.is_valid_rook_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

            piece = W_QUEEN
            queen_index = np.where(board == piece) # rook check
            r_queen = list(queen_index[0])
            c_queen = list(queen_index[1])
            for r_start, c_start in zip(r_queen, c_queen):
                if py.is_valid_queen_move(piece, PLAYER_2, r_start, c_start, r_king, c_king, board, prev_r_delta, prev_c_end, prev_moved_piece):
                    return True
                else:
                    pass

        return False



def is_checkmate(player, board):
    if is_check(player, board): # checking if player_1's king is in checkmate
        if player == PLAYER_1:
            index_king = np.where(board == W_KING)
            r_king = int(index_king[0])
            c_king = int(index_king[1])

            # pawn check
            piece = W_PAWN
            pawn_index = np.where(board == piece)
            r_pawn = list(pawn_index[0])
            c_pawn = list(pawn_index[1])
            for r_start, c_start in zip(r_pawn, c_pawn):
                for r in range(RANKS):
                    for c in range(FILES):
                        if py.is_valid_pawn_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_pawn_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        else:
                            pass

            # knight check
            piece = W_KNIGHT
            knight_index = np.where(board == piece)
            r_knight = list(knight_index[0])
            c_knight = list(knight_index[1])
            for r_start, c_start in zip(r_knight, c_knight):
                for r in range(RANKS):
                    for c in range(FILES):
                        if py.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        else:
                            pass

            # bishop check
            piece = W_BISHOP
            bishop_index = np.where(board == piece)
            r_bishop = list(bishop_index[0])
            c_bishop = list(bishop_index[1])
            for r_start, c_start in zip(r_bishop, c_bishop):
                for i in range(RANKS):
                    if py.is_valid_bishop_move(piece, player, r_start, c_start, r_start+i, c_start+i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    elif py.is_valid_bishop_move(piece, player, r_start, c_start, r_start-i, c_start-i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    else:
                        pass

            # rook check
            piece = W_ROOK
            rook_index = np.where(board == piece)
            r_rook = list(rook_index[0])
            c_rook = list(rook_index[1])
            for r_start, c_start in zip(r_rook, c_rook):
                for i in range(RANKS):
                    if py.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board, prev_r_delta, prev_c_end, prev_moved_piece):
                        temp_board = board
                        temp_board[r_start, c_start] = EMPTY
                        temp_board[r_start+r, c_start+c] = piece
                        if not is_check(piece, player, temp_board):
                            return False
                    else:
                        pass

            # queen check
            piece = W_QUEEN
            queen_index = np.where(board == piece)
            r_queen = list(queen_index[0])
            c_queen = list(queen_index[1])
            for r_start, c_start in zip(r_queen, c_queen):
                for r in range(RANKS):
                    for c in range(FILES):
                        if py.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        else:
                            pass

            return True

        if player == PLAYER_2:
                index_king = np.where(board == B_KING)
                r_king = int(index_king[0])
                c_king = int(index_king[1])

                # pawn check
                piece = B_PAWN
                pawn_index = np.where(board == piece)
                r_pawn = list(pawn_index[0])
                c_pawn = list(pawn_index[1])
                for r_start, c_start in zip(r_pawn, c_pawn):
                    for r in range(RANKS):
                        for c in range(FILES):
                            if py.is_valid_pawn_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_pawn_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            else:
                                pass

                # knight check
                piece = B_KNIGHT
                knight_index = np.where(board == piece)
                r_knight = list(knight_index[0])
                c_knight = list(knight_index[1])
                for r_start, c_start in zip(r_knight, c_knight):
                    for r in range(RANKS):
                        for c in range(FILES):
                            if py.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_knight_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            else:
                                pass

                # bishop check
                piece = B_BISHOP
                bishop_index = np.where(board == piece)
                r_bishop = list(bishop_index[0])
                c_bishop = list(bishop_index[1])
                for r_start, c_start in zip(r_bishop, c_bishop):
                    for i in range(RANKS):
                        if py.is_valid_bishop_move(piece, player, r_start, c_start, r_start+i, c_start+i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_bishop_move(piece, player, r_start, c_start, r_start-i, c_start-i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        else:
                            pass

                # rook check
                piece = B_ROOK
                rook_index = np.where(board == piece)
                r_rook = list(rook_index[0])
                c_rook = list(rook_index[1])
                for r_start, c_start in zip(r_rook, c_rook):
                    for i in range(RANKS):
                        if py.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start+i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start, c_start-i, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start+i, c_start, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        elif py.is_valid_rook_move(piece, player, r_start, c_start, r_start-i, c_start, board, prev_r_delta, prev_c_end, prev_moved_piece):
                            temp_board = board
                            temp_board[r_start, c_start] = EMPTY
                            temp_board[r_start+r, c_start+c] = piece
                            if not is_check(piece, player, temp_board):
                                return False
                        else:
                            pass

                # queen check
                piece = B_QUEEN
                queen_index = np.where(board == piece)
                r_queen = list(queen_index[0])
                c_queen = list(queen_index[1])
                for r_start, c_start in zip(r_queen, c_queen):
                    for r in range(RANKS):
                        for c in range(FILES):
                            if py.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start+r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start+c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            elif py.is_valid_queen_move(piece, player, r_start, c_start, r_start-r, c_start-c, board, prev_r_delta, prev_c_end, prev_moved_piece):
                                temp_board = board
                                temp_board[r_start, c_start] = EMPTY
                                temp_board[r_start+r, c_start+c] = piece
                                if not is_check(piece, player, temp_board):
                                    return False
                            else:
                                pass

                return False

### I DON'T THINK I NEED THIS FUNCTION
# def is_not_check_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
#     if piece == W_PAWN or piece == B_PAWN:
#         while True:
#             if pm.is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
#                 check_board = board
#                 check_board[r_start, c_start] = EMPTY
#                 check_board[r_end, c_end] = piece
#                 # return not check.is_check(check_board, OTHER_VARIABLES):
#                 pass

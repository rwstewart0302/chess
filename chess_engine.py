import config, random

import numpy as np
import chess_pieces as cp

def board_state(player, board):
    b_state = 0

    for piece in config.ALL_PIECES:
        if piece == config.W_PAWN:
            p_value = len(np.where(board == piece)[0]) * 1
            b_state += p_value
        if piece == config.B_PAWN:
            p_value = len(np.where(board == piece)[0]) * 1
            b_state -= p_value
        elif piece == config.W_KNIGHT or piece == config.W_BISHOP:
            bishop_knight_value = len(np.where(board == piece)[0]) * 3
            b_state += bishop_knight_value
        elif piece == config.B_KNIGHT or piece == config.B_BISHOP:
            bishop_knight_value = len(np.where(board == piece)[0]) * 3
            b_state -= bishop_knight_value
        elif piece == config.W_KING_ROOK or piece == config.W_QUEEN_ROOK:
            rook_value = len(np.where(board == piece)[0]) * 5
            b_state += rook_value
        elif piece == config.B_KING_ROOK or piece == config.B_QUEEN_ROOK:
            rook_value = len(np.where(board == piece)[0]) * 5
            b_state -= rook_value
        elif piece == config.W_QUEEN:
            queen_value = len(np.where(board == piece)[0]) * 9
            b_state += queen_value
        elif piece == config.B_QUEEN:
            queen_value = len(np.where(board == piece)[0]) * 9
            b_state -= len(np.where(board == piece)[0]) * 9

    return b_state


def ai_engine(can_castle_kingside, can_castle_queenside, board, player, valid_pieces, prev_r_delta, prev_c_end, prev_moved_piece):

    b_state = board_state(player, board)

    best_move = ()
    valid_moves = []
    for piece in valid_pieces:
        index_piece = np.where(board == piece)
        selected_piece = piece
        r_piece = index_piece[0]
        c_piece = index_piece[1]
        for r_start, c_start in zip(r_piece, c_piece):
            for r_end in range(config.RANKS):
                for c_end in range(config.FILES):
                    pieces = cp.Pieces(board, player, prev_r_delta, prev_c_end, prev_moved_piece, selected_piece, can_castle_queenside, can_castle_kingside)
                    piece_move = pieces.piece_selector
                    temp_board, move_check = piece_move.move(r_start, c_start, r_end, c_end)
                    if move_check:
                        if abs(board_state(player, temp_board)) > abs(b_state):
                            best_move = (selected_piece, r_start, c_start, r_end, c_end, temp_board)
                            b_state = abs(board_state(player, temp_board))
                        else:
                            valid_moves.append((selected_piece, r_start, c_start, r_end, c_end, temp_board))

    if len(best_move) > 0:
        piece_move_selection = best_move
    elif len(best_move) == 0:
        piece_move_selection = random.choice(valid_moves)

    selected_piece = piece_move_selection[0]
    r_start =  piece_move_selection[1]
    c_start = piece_move_selection[2]
    r_end = piece_move_selection[3]
    c_end = piece_move_selection[4]
    b_state = board_state(player, piece_move_selection[5])
    print('board state: ', abs(b_state))

    pieces = cp.Pieces(board, player, prev_r_delta, prev_c_end, prev_moved_piece, selected_piece, can_castle_queenside, can_castle_kingside)
    piece_move = pieces.piece_selector
    board, move_check = piece_move.move(r_start, c_start, r_end, c_end)

    if (selected_piece == config.W_QUEEN_ROOK or selected_piece == config.B_QUEEN_ROOK) and can_castle_queenside:
        can_castle_queenside = False

    elif (selected_piece == config.W_KING_ROOK or selected_piece == config.B_KING_ROOK) and can_castle_kingside:
        can_castle_kingside = False


    elif (selected_piece == config.W_KING or selected_piece == config.B_KING) and (can_castle_queenside or can_castle_kingside):
        if (
        r_start + 1 == r_end or
        r_start - 1 == r_end or
        c_start + 1 == c_end or
        c_start - 1 == c_end
        ):
            can_castle_queenside = False
            can_castle_kingside = False
    else:
        pass

    prev_r_delta = abs(r_end - r_start)
    curr_piece_r = np.nan
    curr_piece_c = np.nan
    prev_piece_r = r_end
    prev_piece_c = c_end
    prev_empty_r = curr_piece_r
    prev_empty_c = curr_piece_c
    prev_c_end = c_end
    prev_moved_piece = selected_piece

    return board, curr_piece_r, curr_piece_c, prev_moved_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c, prev_c_end, can_castle_kingside, can_castle_queenside

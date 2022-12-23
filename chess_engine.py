import config, random

import numpy as np
import chess_pieces as cp

def board_state(player, board):
    white_board_state = 0
    black_board_state = 0

    for piece in config.ALL_PIECES:
        if piece == config.W_PAWN:
            p_value = len(np.where(board == piece)[0]) * 1
            white_board_state += p_value
        if piece == config.B_PAWN:
            p_value = len(np.where(board == piece)[0]) * 1
            black_board_state += p_value
        elif piece == config.W_KNIGHT or piece == config.W_BISHOP:
            bishop_knight_value = len(np.where(board == piece)[0]) * 3
            white_board_state += bishop_knight_value
        elif piece == config.B_KNIGHT or piece == config.B_BISHOP:
            bishop_knight_value = len(np.where(board == piece)[0]) * 3
            black_board_state += bishop_knight_value
        elif piece == config.W_KING_ROOK or piece == config.W_QUEEN_ROOK:
            rook_value = len(np.where(board == piece)[0]) * 5
            white_board_state += rook_value
        elif piece == config.B_KING_ROOK or piece == config.B_QUEEN_ROOK:
            rook_value = len(np.where(board == piece)[0]) * 5
            black_board_state += rook_value
        elif piece == config.W_QUEEN:
            queen_value = len(np.where(board == piece)[0]) * 9
            white_board_state += queen_value
        elif piece == config.B_QUEEN:
            queen_value = len(np.where(board == piece)[0]) * 9
            black_board_state += len(np.where(board == piece)[0]) * 9

    return white_board_state, black_board_state

def valid_moves(can_castle_kingside, can_castle_queenside, board, player, valid_pieces, prev_r_delta, prev_c_end, prev_moved_piece):
    best_move = ()
    valid_moves = {}
    for selected_piece in valid_pieces:
        index_piece = np.where(board == selected_piece)
        r_piece = index_piece[0]
        c_piece = index_piece[1]
        moves = []
        for r_start, c_start in zip(r_piece, c_piece):
            for r_end in range(config.RANKS):
                for c_end in range(config.FILES):
                    pieces = cp.Pieces(board, player, prev_r_delta, prev_c_end, prev_moved_piece, selected_piece, can_castle_queenside, can_castle_kingside)
                    piece_move = pieces.piece_selector
                    temp_board, move_check = piece_move.move(r_start, c_start, r_end, c_end)
                    if move_check:
                        moves.append((r_start, c_start, r_end, c_end))
        valid_moves[selected_piece] = moves

    return valid_moves

def ai_engine(can_castle_kingside, can_castle_queenside, board, player, valid_pieces, prev_r_delta, prev_c_end, prev_moved_piece, depth):

   
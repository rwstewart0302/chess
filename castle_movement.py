import config, check
import numpy as np

def is_valid_castle(player, can_castle_queenside, can_castle_kingside, r_start, c_start, r_end, c_end, board):
    temp_board = board.copy()
    if check.is_check(player, temp_board):
        return False

    elif player == config.PLAYER_1:
        index_king = np.where(board == config.W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

    elif player == config.PLAYER_2:
        index_king = np.where(board == config.B_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

    if c_start - 2 == c_end and r_start == r_end and can_castle_queenside:
        if (
        temp_board[r_king, c_king-1] == config.EMPTY and
        temp_board[r_king, c_king-2] == config.EMPTY and
        temp_board[r_king, c_king-3] == config.EMPTY and
        (temp_board[r_king, c_king-4] == config.W_QUEEN_ROOK or temp_board[r_king, c_king-4] == config.B_QUEEN_ROOK)
        ):
            temp_board[r_king, c_king] = config.EMPTY
            temp_board[r_king, c_king-4] = config.EMPTY
            if player == config.PLAYER_1:
                temp_board[r_king, c_king-1] = config.W_KING
                if check.is_check(player, temp_board):
                    return False
                else:
                    temp_board[r_king, c_king-1] = config.EMPTY
                    temp_board[r_king, c_king-2] = config.W_KING
                    if check.is_check(player, temp_board):
                        return False
                    else:
                        return 'queenside'
            elif player == config.PLAYER_2:
                temp_board[r_king, c_king-1] = config.B_KING
                if check.is_check(player, temp_board):
                    return False
                else:
                    temp_board[r_king, c_king-1] = config.EMPTY
                    temp_board[r_king, c_king-2] = config.B_KING
                    if check.is_check(player, temp_board):
                        return False
                    else:
                        return 'queenside'

    elif c_start + 2 == c_end and r_start == r_end and can_castle_kingside:
        if (
        temp_board[r_king, c_king+1] == config.EMPTY and
        temp_board[r_king, c_king+2] == config.EMPTY and
        (temp_board[r_king, c_king+3] == config.W_KING_ROOK or temp_board[r_king, c_king+3] == config.B_KING_ROOK)
        ):
            temp_board[r_king, c_king] = config.EMPTY
            temp_board[r_king, c_king+3] = config.EMPTY
            if player == config.PLAYER_1:
                temp_board[r_king, c_king+1] = config.W_KING
                if check.is_check(player, temp_board):
                    return False
                else:
                    temp_board[r_king, c_king+1] = config.EMPTY
                    temp_board[r_king, c_king+2] = config.W_KING
                    if check.is_check(player, temp_board):
                        return False
                    else:
                        return 'kingside'
            elif player == config.PLAYER_2:
                temp_board[r_king, c_king+1] = config.B_KING
                if check.is_check(player, temp_board):
                    return False
                else:
                    temp_board[r_king, c_king+1] = config.EMPTY
                    temp_board[r_king, c_king+2] = config.B_KING
                    if check.is_check(player, temp_board):
                        return False
                    else:
                        return 'kingside'

    return False

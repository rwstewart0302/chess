import config, check

import numpy as np

def is_valid_castle(player, can_castle_queenside, can_castle_kingside, r_start, c_start, r_end, c_end, board):
    print('player: ', player)
    print('can_castle_queenside: ', can_castle_queenside)
    print('can_castle_kingside: ', can_castle_kingside)
    print('r_start: ', r_start)
    print('c_start: ', c_start)
    print('r_end: ', r_end)
    print('c_end: ', c_end)

    temp_board = board.copy()
    if (
    player == config.PLAYER_1 and
    r_start == r_end and
    (c_start - 2 == c_end or c_start + 2 == c_end)
    ):
        index_king = np.where(board == config.W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

    elif (
    player == config.PLAYER_2 and
    r_start == r_end and
    (c_start - 2 == c_end or c_start + 2 == c_end)
    ):
        index_king = np.where(board == config.B_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])

    print('temp_board: \n', temp_board)
    if check.is_check(player, temp_board):
        return False
    else:
        if c_start - 2 == c_end and can_castle_queenside:
            for i in range(1, 3):
                temp_board[r_king, c_king-(i-1)] = config.EMPTY
                if player == config.PLAYER_1:
                    temp_board[r_king, c_king-i] = config.W_KING
                elif player == config.PLAYER_2:
                    temp_board[r_king, c_king-i] = config.B_KING
                if check.is_check(player, temp_board):
                    return False
                else:
                    return 'queenside'
        elif c_start + 2 == c_end and can_castle_kingside:
            for i in range(1, 3):
                temp_board[r_king, c_king+(i-1)] = config.EMPTY
                if player == config.PLAYER_1:
                    temp_board[r_king, c_king+i] = config.W_KING
                elif player == config.PLAYER_2:
                    temp_board[r_king, c_king+i] = config.B_KING
                print('temp_board: \n \n \n', temp_board, '\n \n')
                if check.is_check(player, temp_board):
                    return False
                else:
                    return 'kingside'

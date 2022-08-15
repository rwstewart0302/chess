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

def is_check(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    # checking if player_1's king is in check
    if player == PLAYER_1:
        index_king = np.where(board == W_KING)
        r_king = int(index_king[0])
        c_king = int(index_king[1])
        if r_king < 2:
            if py.is_valid_pawn_move(piece, player, r_start, c_start, r_king, c_king, board,  prev_r_delta, prev_c_end, prev_moved_piece)




def is_checkmate():
    pass

def is_not_check_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
    if piece == W_PAWN or piece == B_PAWN:
        while True:
            if pm.is_valid_pawn_move(piece, player, r_start, c_start, r_end, c_end, board,  prev_r_delta, prev_c_end, prev_moved_piece):
                check_board = board
                check_board[r_start, c_start] = EMPTY
                check_board[r_end, c_end] = piece
                # return not check.is_check(check_board, OTHER_VARIABLES):
                pass

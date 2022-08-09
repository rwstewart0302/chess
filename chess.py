# import pygame
import sys
import numpy as np
import chess_pieces as cp

SQUARESIZE = 100 # pixels per square

RANKS = 8
FILES = 8

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

turn_counter = -1

def create_board():
    board = np.full((RANKS, FILES), EMPTY)
    for n_row in range(RANKS):
        for ele in range(FILES):
            if n_row == 1:
                board[n_row, ele] = W_PAWN
            elif n_row == 0:
                if ele == 0 or ele == 7:
                    board[n_row, ele] = W_ROOK
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = W_KNIGHT
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = W_BISHOP
                elif ele == 3:
                    board[n_row, ele] = W_QUEEN
                elif ele == 4:
                    board[n_row, ele] = W_KING

            if n_row == 6:
                board[n_row, ele] = B_PAWN
            elif n_row == 7:
                if ele == 0 or ele == 7:
                    board[n_row, ele] = B_ROOK
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = B_KNIGHT
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = B_BISHOP
                elif ele == 3:
                    board[n_row, ele] = B_QUEEN
                elif ele == 4:
                    board[n_row, ele] = B_KING

    return np.flip(board, 0)


def main():
    player = 'White'
    board = create_board()
    turn_counter = -1
    while True:
        if player == 'White':
            turn_counter += 1
        print(board)
        piece_loc = eval(input('Select a row and column: (piece selection) '))
        r_start = piece_loc[0]
        c_start = piece_loc[1]
        starting_piece = board[r_start, c_start]
        print('starting piece: ', starting_piece)
        if board[r_start, c_start] == W_PAWN:
            if turn_counter == 0:
                pawn_move = cp.Pawn(board, player, turn_counter, prev_r_delta=0, prev_c_end=np.nan, prev_moved_piece=EMPTY)
                piece_move_to = eval(input('Select a row and column: (move selection) '))
                r_end = piece_move_to[0]
                c_end = piece_move_to[1]
                print('square to move to: ', board[r_end, c_end])
                board = pawn_move.move(r_start=r_start, c_start=c_start, r_end=r_end, c_end=c_end)
                prev_r_delta = abs(r_end - r_start)
                prev_c_end = c_end
                prev_moved_piece = starting_piece
            elif turn_counter > 0:
                pawn_move = cp.Pawn(board, player, turn_counter, prev_r_delta=prev_r_delta, prev_c_end=prev_c_end, prev_moved_piece=prev_moved_piece)
                piece_move_to = eval(input('Select a row and column: '))
                r_end = piece_move_to[0]
                c_end = piece_move_to[1]
                print('square to move to: ', board[r_end, c_end])
                board = pawn_move.move(r_start=r_start, c_start=c_start, r_end=r_end, c_end=c_end)
                prev_r_delta = abs(r_end - r_start)
                prev_c_end = c_end
                prev_moved_piece = starting_piece

if __name__ == '__main__':
    main()

# import pygame
import sys
import numpy as np
import chess_pieces as cp

SQUARESIZE = 100 # pixels per square

RANKS = 8
FILES = 8

W_PAWN = 'WP'
W_ROOK = 'WR'
W_KNIGHT = 'WN'
W_BISHOP = 'WB'
W_QUEEN = 'WQ'
W_KING = 'WK'

B_PAWN = 'BP'
B_ROOK = 'BR'
B_KNIGHT = 'BN'
B_BISHOP = 'BB'
B_QUEEN = 'BQ'
B_KING = 'BK'

EMPTY = '00'

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
    player = 'white'
    board = create_board()
    while True:
        if player == 'white':
            turn_counter += 1
        print(board)
        piece_loc = eval(input('Select a row and column: '))
        r_start = piece_loc[0]
        c_start = piece_loc[1]
        starting_piece = board[r_start, c_start]
        if board[r_start, c_start] == W_PAWN:
            pawn_move = cp.Pawn(board, player, turn_counter)
            piece_move_to = eval(input('Select a row and column: '))
            r_end = piece_move_to[0]
            c_end = piece_move_to[1]
            print('square to move to: ', board[r_end, c_end])
            board = pawn_move.move(r_start=r_start, c_start=c_start, r_end=r_end, c_end=c_end, board=board)

if __name__ == '__main__':
    main()

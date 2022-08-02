# import pygame
import sys
import numpy as np
import chess_pieces as cp

SQUARESIZE = 100 # pixels per square

RANKS = 8
FILES = 8


def create_board():
    board = np.zeros((RANKS, FILES))
    for n_row in range(RANKS):
        for ele in range(FILES):
            if n_row == 0 or n_row == 7:
                if ele == 0 or ele == 7:
                    board[n_row, ele] = 5
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = 2
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = 3
                elif ele == 3:
                    board[n_row, ele] = 9
                elif ele == 4:
                    board[n_row, ele] = 1_000
            elif n_row == 1 or n_row == 6:
                board[n_row, ele] = 1
    print(board)


def main():
    player = 'white'
    while True:
        board = create_board()
        print(board)
        piece_loc = eval(input('Select a row and column: '))
        if board[piece_loc[0], piece_loc[1]] ==

if __name__ == '__main__':
    main()

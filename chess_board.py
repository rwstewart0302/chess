import numpy as np
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

RANKS = 8
FILES = 8

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

def draw_board(board):
    for c in range(FILES):
        for r in range(RANKS):
            if (c + r) % 2 == 0:
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            elif (c + r) % 2 != 0:
                pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
    #
    # for c in range(FILES):
    #     for r in range(RANKS):
    #         if board[r, c] == HUMAN_PIECE:
    #             pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(abs(r-(ROW_COUNT-1))*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)
    #         elif board[r, c] == AI_PIECE:
    #             pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), int(abs(r-(ROW_COUNT-1))*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)
    pygame.display.update()

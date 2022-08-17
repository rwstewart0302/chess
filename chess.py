import pygame
import sys
import numpy as np
import chess_pieces as cp
import check

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

### TODO:
### - CLEANOUT ALL PRINTS AND INPUTS WHEN PYGAME IS IMPLEMENTED
### - CREATE GLOBAL JSON FILE FOR PIECE STRING VALUES
### - ADD SOME PRINT STATEMENTS FOR INVALID PIECE SELECTIONS

def main():
    player = 'White'
    board = create_board()
    turn_counter = 0
    while True: # continue playing until checkmate is reached or the game is quit
        # setting our player based on turn
        if turn_counter % 2 == 0:
            player = 'White'
        elif turn_counter % 2 != 0:
            player = 'Black'

        print('checkmate? ', check.is_checkmate(player, board))
        if check.is_checkmate(player, board):
            if player == 'White':
                winning_player = 'Black'
            elif player == 'Black':
                winning_player = 'White'

            print(f'{winning_player} wins!')
            break

        print(board)
        print()
        print(f'It is {player}\s turn...')

        while True: # continue asking for player's piece selection and movement until their choice is valid
            piece_loc = eval(input('Select a row and column: (piece selection) '))
            valid_piece = 1
            piece_move_error = 1
            try:
                r_start = piece_loc[0]
                c_start = piece_loc[1]
                starting_piece = board[r_start, c_start]
                piece_selection_error = 0
                print('starting piece: ', starting_piece)
                if starting_piece in list(PIECES[player].values()):
                    valid_piece = 0
                else:
                    print('invalid piece selected!')
            except IndexError:
                piece_selection_error = 1
                print('select a valid piece!')

            if piece_selection_error == 0 and valid_piece == 0:
                piece_move_to = eval(input('Select a row and column: (move selection) '))
                try:
                    r_end = piece_move_to[0]
                    c_end = piece_move_to[1]
                    piece_move_error = 0
                    print('square to move to: ', board[r_end, c_end])
                except IndexError:
                    print('select a valid move!')

            if piece_move_error == 0:
                if turn_counter == 0: # creating initial values for previous moved pieces to check for en passant
                    prev_r_delta=0
                    prev_c_end=np.nan
                    prev_moved_piece=EMPTY
                else:
                    pass

                # instiatiating the class for the piece selected
                if board[r_start, c_start] == PIECES[player]['PAWN']:
                    piece_move = cp.Pawn(board, player, prev_r_delta=prev_r_delta, prev_c_end=prev_c_end, prev_moved_piece=prev_moved_piece)
                elif board[r_start, c_start] == PIECES[player]['KNIGHT']:
                    piece_move = cp.Knight(board, player)
                elif board[r_start, c_start] == PIECES[player]['BISHOP']:
                    piece_move = cp.Bishop(board, player)
                elif board[r_start, c_start] == PIECES[player]['ROOK']:
                    piece_move = cp.Rook(board, player)
                elif board[r_start, c_start] == PIECES[player]['QUEEN']:
                    piece_move = cp.Queen(board, player)
                elif board[r_start, c_start] == PIECES[player]['KING']:
                    piece_move = cp.King(board, player)

                board, move_check = piece_move.move(r_start=r_start, c_start=c_start, r_end=r_end, c_end=c_end)

                if move_check: # if the move is valid then go to the next player
                    prev_r_delta = abs(r_end - r_start)
                    prev_c_end = c_end
                    prev_moved_piece = starting_piece
                    turn_counter += 1
                    break
                elif not move_check: # if the move is not valid then ask for a move from the next player
                    pass
            else:
                pass

if __name__ == '__main__':
    main()

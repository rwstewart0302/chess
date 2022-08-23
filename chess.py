import pygame, sys, check, config

import numpy as np
import chess_pieces as cp
import chess_board as cb

SQUARESIZE = 100 # pixels per square

width = config.FILES * SQUARESIZE
height = config.RANKS * SQUARESIZE
size = (width, height)

LIGHT_SQUARES = (255, 207, 159)
DARK_SQUARES = (210, 140, 69)
SELECTED_COLOR = (247, 236, 91)

pygame.init()
screen = pygame.display.set_mode(size)

w_pawn_image = pygame.image.load('chess_piece_images/w_pawn.png')
w_pawn_image = pygame.transform.scale(w_pawn_image, (SQUARESIZE, SQUARESIZE))
w_knight_image = pygame.image.load('chess_piece_images/w_knight.png')
w_knight_image = pygame.transform.scale(w_knight_image, (SQUARESIZE, SQUARESIZE))
w_bishop_image = pygame.image.load('chess_piece_images/w_bishop.png')
w_bishop_image = pygame.transform.scale(w_bishop_image, (SQUARESIZE, SQUARESIZE))
w_rook_image = pygame.image.load('chess_piece_images/w_rook.png')
w_rook_image = pygame.transform.scale(w_rook_image, (SQUARESIZE, SQUARESIZE))
w_queen_image = pygame.image.load('chess_piece_images/w_queen.png')
w_queen_image = pygame.transform.scale(w_queen_image, (SQUARESIZE, SQUARESIZE))
w_king_image = pygame.image.load('chess_piece_images/w_king.png')
w_king_image = pygame.transform.scale(w_king_image, (SQUARESIZE, SQUARESIZE))

b_pawn_image = pygame.image.load('chess_piece_images/b_pawn.png')
b_pawn_image = pygame.transform.scale(b_pawn_image, (SQUARESIZE, SQUARESIZE))
b_knight_image = pygame.image.load('chess_piece_images/b_knight.png')
b_knight_image = pygame.transform.scale(b_knight_image, (SQUARESIZE, SQUARESIZE))
b_bishop_image = pygame.image.load('chess_piece_images/b_bishop.png')
b_bishop_image = pygame.transform.scale(b_bishop_image, (SQUARESIZE, SQUARESIZE))
b_rook_image = pygame.image.load('chess_piece_images/b_rook.png')
b_rook_image = pygame.transform.scale(b_rook_image, (SQUARESIZE, SQUARESIZE))
b_queen_image = pygame.image.load('chess_piece_images/b_queen.png')
b_queen_image = pygame.transform.scale(b_queen_image, (SQUARESIZE, SQUARESIZE))
b_king_image = pygame.image.load('chess_piece_images/b_king.png')
b_king_image = pygame.transform.scale(b_king_image, (SQUARESIZE, SQUARESIZE))

def create_board():
    board = np.full((config.RANKS, config.FILES), config.EMPTY)
    for n_row in range(config.RANKS):
        for ele in range(config.FILES):
            if n_row == 1:
                board[n_row, ele] = config.W_PAWN
            elif n_row == 0:
                if ele == 7:
                    board[n_row, ele] = config.W_KING_ROOK
                elif ele == 0:
                    board[n_row, ele] = config.W_QUEEN_ROOK
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = config.W_KNIGHT
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = config.W_BISHOP
                elif ele == 3:
                    board[n_row, ele] = config.W_QUEEN
                elif ele == 4:
                    board[n_row, ele] = config.W_KING

            if n_row == 6:
                board[n_row, ele] = config.B_PAWN
            elif n_row == 7:
                if ele == 7:
                    board[n_row, ele] = config.B_KING_ROOK
                elif ele == 0:
                    board[n_row, ele] = config.B_QUEEN_ROOK
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = config.B_KNIGHT
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = config.B_BISHOP
                elif ele == 3:
                    board[n_row, ele] = config.B_QUEEN
                elif ele == 4:
                    board[n_row, ele] = config.B_KING

    return np.flip(board, 0)

def draw_board(board, move_piece, curr_piece_r, curr_piece_c, prev_move_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c):
    for r in range(config.RANKS):
        for c in range(config.FILES):
            if c != curr_piece_c and r != curr_piece_r:
                if (c+r)%2 == 0:
                    pygame.draw.rect(screen, LIGHT_SQUARES, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
                elif (c+r)%2 != 0:
                    pygame.draw.rect(screen, DARK_SQUARES, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

            elif move_piece and c == curr_piece_c and r == curr_piece_r:
                pygame.draw.rect(screen, SELECTED_COLOR, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

            # elif prev_move_piece and c == curr_piece_c and r == curr_piece_r:
            #     pygame.draw.rect(screen, SELECTED_COLOR, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

            if board[r, c] == config.W_PAWN:
                target_rect = w_pawn_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_pawn_image, target_rect)
            elif board[r, c] == config.W_KNIGHT:
                target_rect = w_knight_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_knight_image, target_rect)
            elif board[r, c] == config.W_BISHOP:
                target_rect = w_bishop_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_bishop_image, target_rect)
            elif board[r, c] == config.W_KING_ROOK:
                target_rect = w_rook_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_rook_image, target_rect)
            elif board[r, c] == config.W_QUEEN_ROOK:
                target_rect = w_rook_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_rook_image, target_rect)
            elif board[r, c] == config.W_QUEEN:
                target_rect = w_queen_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_queen_image, target_rect)
            elif board[r, c] == config.W_KING:
                target_rect = w_king_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_king_image, target_rect)

            elif board[r, c] == config.B_PAWN:
                target_rect = b_pawn_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_pawn_image, target_rect)
            elif board[r, c] == config.B_KNIGHT:
                target_rect = b_knight_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_knight_image, target_rect)
            elif board[r, c] == config.B_BISHOP:
                target_rect = b_bishop_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_bishop_image, target_rect)
            elif board[r, c] == config.B_KING_ROOK:
                target_rect = b_rook_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_rook_image, target_rect)
            elif board[r, c] == config.B_QUEEN_ROOK:
                target_rect = b_rook_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_rook_image, target_rect)
            elif board[r, c] == config.B_QUEEN:
                target_rect = b_queen_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_queen_image, target_rect)
            elif board[r, c] == config.B_KING:
                target_rect = b_king_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_king_image, target_rect)

    pygame.display.update()

### TODO:
### - CLEANOUT ALL PRINTS AND INPUTS WHEN PYGAME IS IMPLEMENTED
### - ADD SOME PRINT STATEMENTS FOR INVALID PIECE SELECTIONS
### - CLEANUP MAIN FILE ---> MAKE VARIABLES AND LOOPS MORE READABLE
### - DEFINE CHESS_BOARD.PY FUNCTION TO HANDLE PYGAME STUFF

def main():
    player = config.PLAYER_1
    board = create_board()

    valid_piece_selection = False
    curr_piece_r = np.nan
    curr_piece_c = np.nan
    prev_piece_r = np.nan
    prev_piece_c = np.nan
    prev_empty_r = np.nan
    prev_empty_c = np.nan

    turn_counter = 0
    three_fold_repition = 0
    turn_start = True
    game_over = False

    board_states = [board]

    white_can_castle_queenside = True
    white_can_castle_kingside = True
    black_can_castle_queenside = True
    black_can_castle_kingside = True

    select_piece = True
    move_piece = False
    prev_move_piece = False
    mouse_click_1 = False
    mouse_click_2 = False
    move_check = False

    while not game_over:
        if turn_start:
            king_draw_check = 1
            three_fold_repition = 0

            if turn_counter > 0:
                for board_state in board_states:
                    if np.all(board == board_state):
                        three_fold_repition += 1
                    else:
                        pass

            if three_fold_repition == 3:
                game_over = True
                print('Threefold Repition Draw!')

            for row in board:
                for piece in row:
                    if piece not in [config.W_KING, config.B_KING, config.EMPTY]:
                        king_draw_check = 0

            if king_draw_check == 1:
                game_over = True
                print('King\'s Only Stalemate!')

            draw_board(board, move_piece, curr_piece_r, curr_piece_c, prev_move_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
            pygame.display.update()

            # setting our player based on turn
            if turn_counter % 2 == 0:
                player = config.PLAYER_1
            elif turn_counter % 2 != 0:
                player = config.PLAYER_2

            if check.is_check(player, board) and not game_over:
                if check.is_game_over(player, board):
                    if player == config.PLAYER_1:
                        winning_player = config.PLAYER_2
                        game_over = True
                        print(f'{winning_player} wins!')
                    elif player == config.PLAYER_2:
                        winning_player = config.PLAYER_1
                        game_over = True
                        print(f'{winning_player} wins!')
                elif not check.is_game_over(player, board):
                        turn_start = False



            elif not check.is_check(player, board) and not game_over:
                if check.is_game_over(player, board):
                    game_over = True
                    print('stalemate')
                else:
                    print(f'It is {player}\'s turn...')
                    turn_start = False

        if player == config.PLAYER_1:
            valid_pieces = config.PLAYER_1_PIECES
        elif player == config.PLAYER_2:
            valid_pieces = config.PLAYER_2_PIECES

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_piece:
                    x_pos = event.pos[0]
                    y_pos = event.pos[1]
                    c_start = int(x_pos//SQUARESIZE)
                    r_start = int(y_pos//SQUARESIZE)
                    mouse_click_1 = True
                    select_piece = False

                if move_piece:
                    x_pos = event.pos[0]
                    y_pos = event.pos[1]
                    c_end = int(x_pos//SQUARESIZE)
                    r_end = int(y_pos//SQUARESIZE)
                    mouse_click_2 = True
                    move_piece = False

            if mouse_click_1:
                selected_piece = board[r_start, c_start]
                if selected_piece in config.PLAYER_1_PIECES or selected_piece in config.PLAYER_2_PIECES:
                    move_piece = True
                    mouse_click_1 = False
                    curr_piece_c = c_start
                    curr_piece_r = r_start
                    draw_board(board, move_piece, curr_piece_r, curr_piece_c, prev_move_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
                    pygame.display.update()
                else:
                    select_piece = True
                    mouse_click_1 = False

            if turn_counter == 0: # creating initial values for previous moved pieces to check for en passant
                prev_r_delta=0
                prev_c_end=np.nan
                prev_moved_piece=config.EMPTY

            if mouse_click_2:
                if player == config.PLAYER_1:
                    if selected_piece == config.W_PAWN:
                        piece_move = cp.Pawn(board, player, prev_r_delta, prev_c_end, prev_moved_piece)
                    elif selected_piece == config.W_KNIGHT:
                        piece_move = cp.Knight(board, player)
                    elif selected_piece == config.W_BISHOP:
                        piece_move = cp.Bishop(board, player)
                    elif selected_piece == config.W_KING_ROOK:
                        piece_move = cp.Rook(board, player, selected_piece)
                    elif selected_piece == config.W_QUEEN_ROOK:
                        piece_move = cp.Rook(board, player, selected_piece)
                    elif selected_piece == config.W_QUEEN:
                        piece_move = cp.Queen(board, player)
                    elif selected_piece == config.W_KING:
                        piece_move = cp.King(board, player, white_can_castle_queenside, white_can_castle_kingside)

                    if selected_piece in valid_pieces:
                        board, move_check = piece_move.move(r_start, c_start, r_end, c_end)
                        if move_check and selected_piece == config.W_QUEEN_ROOK:
                            white_can_castle_queenside = False
                        elif move_check and selected_piece == config.W_KING_ROOK:
                            white_can_castle_kingside = False

                    else:
                        move_check = False

                    if move_check and selected_piece == config.W_KING:
                        if (
                        r_start + 1 == r_end or
                        r_start - 1 == r_end or
                        c_start + 1 == c_end or
                        c_start - 1 == c_end
                        ):
                            white_can_castle_queenside = False
                            white_can_castle_kingside = False

                    else:
                        pass

                elif player == config.PLAYER_2:
                    if selected_piece == config.B_PAWN:
                        piece_move = cp.Pawn(board, player, prev_r_delta, prev_c_end, prev_moved_piece)
                    elif selected_piece == config.B_KNIGHT:
                        piece_move = cp.Knight(board, player)
                    elif selected_piece == config.B_BISHOP:
                        piece_move = cp.Bishop(board, player)
                    elif selected_piece == config.B_KING_ROOK:
                        piece_move = cp.Rook(board, player, selected_piece)
                    elif selected_piece == config.B_QUEEN_ROOK:
                        piece_move = cp.Rook(board, player, selected_piece)
                    elif selected_piece == config.B_QUEEN:
                        piece_move = cp.Queen(board, player)
                    elif selected_piece == config.B_KING:
                        piece_move = cp.King(board, player, black_can_castle_queenside, black_can_castle_kingside)

                    if selected_piece in valid_pieces:
                        board, move_check = piece_move.move(r_start, c_start, r_end, c_end)
                        if move_check and selected_piece == config.B_QUEEN_ROOK:
                            black_can_castle_queenside = False
                        elif move_check and selected_piece == config.B_KING_ROOK:
                            black_can_castle_kingside = False
                    else:
                        move_check = False

                    if move_check and selected_piece == config.B_KING:
                        if (
                        r_start + 1 == r_end or
                        r_start - 1 == r_end or
                        c_start + 1 == c_end or
                        c_start - 1 == c_end
                        ):
                            black_can_castle_queenside = False
                            black_can_castle_kingside = False

                    else:
                        pass

            if move_check and mouse_click_2: # if the move is valid then go to the next player
                prev_r_delta = abs(r_end - r_start)
                prev_c_end = c_end
                prev_moved_piece = selected_piece
                turn_counter += 1
                board_states.append(board)

                turn_start = True
                select_piece = True
                mouse_click_2 = False
                prev_move_piece = True

                curr_piece_r = np.nan
                curr_piece_c = np.nan
                prev_piece_r = r_end
                prev_piece_c = c_end
                prev_empty_r = curr_piece_r
                prev_empty_c = curr_piece_c
                draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_move_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
                pygame.display.update()

            elif not move_check and mouse_click_2: # if the move is not valid then ask for a move from the same player
                turn_start = False
                select_piece = True
                mouse_click_2 = False

                curr_piece_r = np.nan
                curr_piece_c = np.nan
                prev_piece_r = np.nan
                prev_piece_c = np.nan
                prev_empty_r = np.nan
                prev_empty_c = np.nan
                draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_move_piece, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
                pygame.display.update()


if __name__ == '__main__':
    main()

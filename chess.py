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
                if ele == 0 or ele == 7:
                    board[n_row, ele] = config.W_ROOK
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
                if ele == 0 or ele == 7:
                    board[n_row, ele] = config.B_ROOK
                elif ele == 1 or ele == 6:
                    board[n_row, ele] = config.B_KNIGHT
                elif ele == 2 or ele == 5:
                    board[n_row, ele] = config.B_BISHOP
                elif ele == 3:
                    board[n_row, ele] = config.B_QUEEN
                elif ele == 4:
                    board[n_row, ele] = config.B_KING

    return np.flip(board, 0)

def draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c):
    for r in range(config.RANKS):
        for c in range(config.FILES):
            if (c+r)%2 == 0:
                pygame.draw.rect(screen, LIGHT_SQUARES, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            elif (c+r)%2 != 0:
                pygame.draw.rect(screen, DARK_SQUARES, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

            if board[r, c] == config.W_PAWN:
                target_rect = w_pawn_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_pawn_image, target_rect)
            elif board[r, c] == config.W_KNIGHT:
                target_rect = w_knight_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_knight_image, target_rect)
            elif board[r, c] == config.W_BISHOP:
                target_rect = w_bishop_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(w_bishop_image, target_rect)
            elif board[r, c] == config.W_ROOK:
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
            elif board[r, c] == config.B_ROOK:
                target_rect = b_rook_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_rook_image, target_rect)
            elif board[r, c] == config.B_QUEEN:
                target_rect = b_queen_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_queen_image, target_rect)
            elif board[r, c] == config.B_KING:
                target_rect = b_king_image.get_rect(center=(SQUARESIZE*c+SQUARESIZE//2,SQUARESIZE*r+SQUARESIZE//2))
                screen.blit(b_king_image, target_rect)

    if valid_piece_selection:
        pygame.draw.rect(screen, SELECTED_COLOR, (curr_piece_c*SQUARESIZE, curr_piece_r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
    else:
        pass

    pygame.display.update()

### TODO:
### - CLEANOUT ALL PRINTS AND INPUTS WHEN PYGAME IS IMPLEMENTED
### - ADD SOME PRINT STATEMENTS FOR INVALID PIECE SELECTIONS
### - CLEANUP MAIN FILE ---> MAKE VARIABLES AND LOOPS MORE READABLE
### - DEFINE CHESS_BOARD.PY FUNCTION TO HANDLE PYGAME STUFF
### - GIVE A CONDITION TO PIECE_MOVEMENT.PY FOR CASTLING AND STALEMATE!!!
### - DONT FORGET KING/KING STALEMATE AND THREEFOLD REPITION

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
    temp_turn_counter = -1
    turn_start_loop = True
    clear_board_loop = False
    game_over = False
    mouse_click_1 = False
    mouse_click_2 = False
    move_loop = False

    while not game_over: # continue playing until checkmate is reached or the game is quit
        if not clear_board_loop:
            if temp_turn_counter < turn_counter:
                print(board)
                draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
                pygame.display.update()
                temp_turn_counter = turn_counter
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if turn_start_loop:
                turn_start_loop = False

                selection_loop = True
                mouse_click_1 = False
                mouse_click_2 = False

                valid_piece_selection = False

                valid_move_selection = False

                move_check = False

                clear_board_loop = False

                r_start = np.nan
                c_start = np.nan
                r_end = np.nan
                c_end = np.nan

                # setting our player based on turn
                if turn_counter % 2 == 0:
                    player = config.PLAYER_1
                elif turn_counter % 2 != 0:
                    player = config.PLAYER_2

                if check.is_check(player, board):
                    if check.is_game_over(player, board):
                        if player == config.PLAYER_1:
                            winning_player = config.PLAYER_2
                            game_over = True
                        elif player == config.PLAYER_2:
                            winning_player = config.PLAYER_1
                            game_over = True
                        print(f'{winning_player} wins!')

                elif not check.is_check(player, board):
                    if check.is_game_over(player, board):
                        game_over = True
                        print('stalemate')
                    else:
                        print(f'It is {player}\'s turn...')
                        break


            # while clear_board_loop:
            #     print('clear board?')
            #     valid_piece_selection = False
            #     clear_board_loop = False
            #     selection_loop = True
            #     curr_piece_r = np.nan
            #     curr_piece_c = np.nan
            #     prev_piece_r = np.nan
            #     prev_piece_c = np.nan
            #     prev_empty_r = np.nan
            #     prev_empty_c = np.nan
            #     draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
            #     pygame.display.update()
            #     break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if selection_loop:
                    if not valid_piece_selection:
                        print('clicking?')
                        print('mouse?')
                        x_pos = event.pos[0]
                        y_pos = event.pos[1]
                        c_start = int(x_pos//SQUARESIZE)
                        r_start = int(y_pos//SQUARESIZE)
                        mouse_click_1 = True

                if move_loop:
                    x_pos = event.pos[0]
                    y_pos = event.pos[1]
                    c_end = int(x_pos//SQUARESIZE)
                    r_end = int(y_pos//SQUARESIZE)
                    mouse_click_2 = True

            if mouse_click_1:
                print('click1?')
                selected_piece = board[r_start, c_start]
                if selected_piece in config.PLAYER_1_PIECES or selected_piece in config.PLAYER_2_PIECES:
                    valid_piece_selection = True
                    curr_piece_c = c_start
                    curr_piece_r = r_start
                    draw_board(board, valid_piece_selection, curr_piece_r, curr_piece_c, prev_piece_r, prev_piece_c, prev_empty_r, prev_empty_c)
                    pygame.display.update()

            if valid_piece_selection and player == config.PLAYER_1:
                valid_pieces = config.PLAYER_1_PIECES
            elif valid_piece_selection and player == config.PLAYER_2:
                valid_pieces = config.PLAYER_2_PIECES

            if valid_piece_selection:
                if selected_piece in valid_pieces:
                    print('selected')
                    move_loop = True
                    selection_loop = False
                    mouse_click_1 = False

                else:
                    print('else')
                    valid_piece_selection = False
                    move_loop = False
                    selection_loop = True
                    mouse_click_1 = False
                    # clear_board_loop = True

            if turn_counter == 0: # creating initial values for previous moved pieces to check for en passant
                prev_r_delta=0
                prev_c_end=np.nan
                prev_moved_piece=config.EMPTY

            if mouse_click_2:
                print('click2?')
                # instiatiating the class for the piece selected
                if board[r_start, c_start] == config.W_PAWN or board[r_start, c_start] == config.B_PAWN:
                    piece_move = cp.Pawn(board, player, prev_r_delta, prev_c_end, prev_moved_piece)
                elif board[r_start, c_start] == config.W_KNIGHT or board[r_start, c_start] == config.B_KNIGHT:
                    piece_move = cp.Knight(board, player)
                elif board[r_start, c_start] == config.W_BISHOP or board[r_start, c_start] == config.B_BISHOP:
                    piece_move = cp.Bishop(board, player)
                elif board[r_start, c_start] == config.W_ROOK or board[r_start, c_start] == config.B_ROOK:
                    piece_move = cp.Rook(board, player)
                elif board[r_start, c_start] == config.W_QUEEN or board[r_start, c_start] == config.B_QUEEN:
                    piece_move = cp.Queen(board, player)
                elif board[r_start, c_start] == config.W_KING or board[r_start, c_start] == config.B_KING:
                    piece_move = cp.King(board, player)

                board, move_check = piece_move.move(r_start, c_start, r_end, c_end)

            if move_check and mouse_click_2: # if the move is valid then go to the next player
                prev_r_delta = abs(r_end - r_start)
                prev_c_end = c_end
                prev_moved_piece = selected_piece
                turn_counter += 1
                mouse_click_2 = False
                turn_start_loop = True
                move_loop = False

            elif not move_check and mouse_click_2: # if the move is not valid then ask for a move from the same player
                clear_board_loop = True
                valid_piece_selection = False
                mouse_click_2 = False
                turn_start_loop = False
                move_loop = False


if __name__ == '__main__':
    main()

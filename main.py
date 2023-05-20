# # # # import pygame
# # # # import sys
# # # #
# # # # # Initialize Pygame
# # # # pygame.init()
# # # #
# # # # # Set screen size
# # # # screen = pygame.display.set_mode((600, 600))
# # # #
# # # # # Load sounds
# # # # bubble_sound = pygame.mixer.Sound('bubble.wav')
# # # # ding_sound = pygame.mixer.Sound('ding.wav')
# # # #
# # # # # Set colors
# # # # WHITE = (255, 255, 255)
# # # # BLACK = (0, 0, 0)
# # # # RED = (255, 0, 0)
# # # #
# # # # # Set font
# # # # font = pygame.font.Font(None, 72)
# # # #
# # # # # Initialize game state
# # # # board = [[' ' for _ in range(3)] for _ in range(3)]
# # # # player = 'X'
# # # #
# # # # def draw_board():
# # # #     # Draw board
# # # #     for i in range(1, 3):
# # # #         pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, 600), 5)
# # # #         pygame.draw.line(screen, BLACK, (0, i * 200), (600, i * 200), 5)
# # # #
# # # #     # Draw X and O
# # # #     for i in range(3):
# # # #         for j in range(3):
# # # #             if board[i][j] == 'X':
# # # #                 pygame.draw.line(screen, BLACK, (j * 200 + 25, i * 200 + 25), (j * 200 + 175, i * 200 + 175), 5)
# # # #                 pygame.draw.line(screen, BLACK, (j * 200 + 175, i * 200 + 25), (j * 200 + 25, i * 200 + 175), 5)
# # # #             elif board[i][j] == 'O':
# # # #                 pygame.draw.circle(screen, BLACK, (j * 200 + 100, i * 200 + 100), 75, 5)
# # # #
# # # # def check_winner():
# # # #     # Check rows
# # # #     for row in board:
# # # #         if row[0] == row[1] == row[2] and row[0] != ' ':
# # # #             return row[0]
# # # #
# # # #     # Check columns
# # # #     for col in range(3):
# # # #         if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
# # # #             return board[0][col]
# # # #
# # # #     # Check diagonals
# # # #     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
# # # #         return board[0][0]
# # # #     if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
# # # #         return board[0][2]
# # # #
# # # #     # Check if board is full
# # # #     if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
# # # #         return 'Tie'
# # # #
# # # #     # No winner yet
# # # #     return None
# # # #
# # # # while True:
# # # #     # Handle events
# # # #     for event in pygame.event.get():
# # # #         if event.type == pygame.QUIT:
# # # #             sys.exit()
# # # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # # #             x, y = event.pos
# # # #             row = y // 200
# # # #             col = x // 200
# # # #             if board[row][col] == ' ':
# # # #                 board[row][col] = player
# # # #                 if player == 'X':
# # # #                     bubble_sound.play()
# # # #                     player = 'O'
# # # #                 else:
# # # #                     ding_sound.play()
# # # #                     player = 'X'
# # # #
# # # #     # Clear screen
# # # #     screen.fill(WHITE)
# # # #
# # # #     # Draw game state
# # # #     draw_board()
# # # #
# # # #     # Check winner
# # # #     winner = check_winner()
# # # #     if winner is not None:
# # # #         if winner == 'Tie':
# # # #             text = font.render('Tie!', True, RED)
# # # #         else:
# # # #             text = font.render(winner + ' wins!', True, RED)
# # # #         screen.blit(text, (300 - text.get_width() // 2, 300 - text.get_height() //2))
# # # #
# # # #     # Update screen
# # # #     pygame.display.flip()
# # #
# # #
# # # import pygame
# # # import sys
# # #
# # # # Initialize Pygame
# # # pygame.init()
# # #
# # # # Set screen size
# # # screen_size = 600
# # # screen = pygame.display.set_mode((screen_size, screen_size))
# # #
# # # # Load sounds
# # # bubble_sound = pygame.mixer.Sound('bubble.wav')
# # # ding_sound = pygame.mixer.Sound('ding.wav')
# # #
# # # # Set colors
# # # BLACK = (0, 0, 0)
# # # RED = (255, 0, 0)
# # #
# # # # Set font
# # # font = pygame.font.Font(None, 36)
# # #
# # # # Initialize game state
# # # state = 'menu'
# # # board_size = 3
# # # cell_size = screen_size // board_size
# # # win_length = 3
# # # board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
# # # player = 'X'
# # # scores = {'X': 0, 'O': 0}
# # #
# # #
# # # def draw_board():
# # #     # Draw board
# # #     for i in range(1, board_size):
# # #         pygame.draw.line(screen, RED, (i * cell_size, 0), (i * cell_size, screen_size), 5)
# # #         pygame.draw.line(screen, RED, (0, i * cell_size), (screen_size, i * cell_size), 5)
# # #
# # #     # Draw X and O
# # #     for i in range(board_size):
# # #         for j in range(board_size):
# # #             if board[i][j] == 'X':
# # #                 pygame.draw.line(screen, RED, (j * cell_size + cell_size // 8, i * cell_size + cell_size // 8), (
# # #                 j * cell_size + cell_size - cell_size // 8, i * cell_size + cell_size - cell_size // 8), 5)
# # #                 pygame.draw.line(screen, RED,
# # #                                  (j * cell_size + cell_size - cell_size // 8, i * cell_size + cell_size // 8),
# # #                                  (j * cell_size + cell_size // 8, i * cell_size + cell_size - cell_size // 8), 5)
# # #             elif board[i][j] == 'O':
# # #                 pygame.draw.circle(screen, RED, (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2),
# # #                                    cell_size // 2 - cell_size // 8, 5)
# # #
# # #
# # # def check_winner():
# # #     # Check rows
# # #     for row in range(board_size):
# # #         for col in range(board_size - win_length + 1):
# # #             if all(board[row][col + i] == player for i in range(win_length)):
# # #                 return player
# # #
# # #     # Check columns
# # #     for col in range(board_ze):
# # #         for row in range(board_sizend(win_length + 1)):
# # #             if all(board[row + i][col] == player for i in range(win_length)):
# # #                 return player
# # #
# # #     # Check diagonals
# # #     for row in range(board_sizend(win_length + 1)):
# # #         for col in range(board_sizend(win_length + 1)):
# # #             if all(board[row + i][col + i] == player for i in range(win_length)):
# # #                 return player
# # #             if all(board[row + i][col + win_length - 1 - i] == player for i in range(win_length)):
# # #                 return player
# # #
# # #     # Check if board is full
# # #     if all(board[i][j] != ' ' for i in range(board_sizend) for j in range(board_sizend)):
# # #         return 'Tie'
# # #
# # #     # No winner yet
# # #     return None
# # #
# # #
# # # def draw_text(text):
# # #     text_surface = font.render(text, True, RED)
# # #     screen.blit(text_surface, (
# # #     screen.get_width() // 2 - text_surface.get_width() // 2, screen.get_height() // 2 - text_surface.get_height() // 2))
# # #
# # #
# # # def draw_menu():
# # #     draw_text('Choose board size:')
# # #     draw_text('3x3')
# # #     draw_text('9x9')
# # #     draw_text('16x16')
# # #
# # #
# # # def handle_menu(event):
# # #     global state
# # #     global board
# # #     global board_sizend
# # #     global win_length
# # #     global scores
# # #
# # #     if event.type == pygame.MOUSEBUTTONDOWN:
# # #         x, y = event.pos
# # #
# # #         if y > 100 and y < 150:
# # #             state = 'game'
# # #             board_sizend = 3
# # #             win_length = 3
# # #
# # #         elif y > 200 and y < 250:
# # #             state = 'game'
# # #             board_sizend = 9
# # #             win_length = 4
# # #
# # #         elif y > 300 and y < 350:
# # #             state = 'game'
# # #             board_sizend = 16
# # #             win_length = 5
# # #
# # #         else:
# # #             return
import sys

import pygame
from pygame.locals import *

# Set colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

def choose_symbols():
    global player_one_symbol
    global player_two_symbol
    global player_one_color
    global player_two_color

    # Set default symbols and colors
    player_one_symbol = 'X'
    player_two_symbol = 'O'
    player_one_color = RED
    player_two_color = RED

    # Set font
    font = pygame.font.Font(None, 36)

    # Set colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set symbol options
    symbol_options = ['X', 'O', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Set symbol option positions
    symbol_option_positions = [(50, 50), (150, 50), (250, 50), (350, 50), (450, 50),
                              (50, 150), (150, 150), (250, 150), (350, 150), (450, 150),
                              (50, 250), (150, 250)]

    # Set current player
    current_player = 'Player One'

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Check if a symbol option was clicked
                for i in range(len(symbol_options)):
                    symbol_option_position = symbol_option_positions[i]
                    symbol_option_rect = pygame.Rect(symbol_option_position[0],
                                                     symbol_option_position[1],
                                                     50,
                                                     50)
                    if symbol_option_rect.collidepoint(pos):
                        if current_player == 'Player One':
                            player_one_symbol = symbol_options[i]
                            current_player = 'Player Two'
                        else:
                            player_two_symbol = symbol_options[i]
                            return

        # Draw screen
        screen.fill(BLACK)

        # Draw title
        title_text = font.render(f'{current_player} Choose Your Symbol', True,
                                 WHITE)
        screen.blit(title_text, (50, 10))

        # Draw symbol options
        for i in range(len(symbol_options)):
            symbol_option_position = symbol_option_positions[i]
            pygame.draw.rect(screen,
                             WHITE,
                             (symbol_option_position[0],
                              symbol_option_position[1],
                              50,
                              50),
                             1)
            symbol_option_text = font.render(symbol_options[i], True,
                                             WHITE)
            screen.blit(symbol_option_text,
                        (symbol_option_position[0] +
                         (50 - symbol_option_text.get_width()) //2,
                         symbol_option_position[1] +
                         (50 - symbol_option_text.get_height()) //2))

        pygame.display.update()



# Initialize Pygame
pygame.init()

# Set background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

# Set screen size
screen = pygame.display.set_mode((600, 600))

# Allow players to choose symbols
choose_symbols()



# Set sounds
bubble_sound = pygame.mixer.Sound('bubble.wav')
ding_sound = pygame.mixer.Sound('ding.wav')

# Set font
font = pygame.font.Font(None, 36)

# Initialize game state
game_state = [[None, None, None], [None, None, None], [None, None, None]]
current_player = 'X'
player_one_wins = 0
player_two_wins = 0

def draw_game_state():
    # Draw background
    screen.fill(BLACK)

    # Draw scoreboard
    pygame.draw.rect(screen, WHITE, (0, 0, 600, 50))
    player_one_score_text = font.render(f'Player One: {player_one_wins}', True,
                                        BLACK)
    player_two_score_text = font.render(f'Player Two: {player_two_wins}', True,
                                        BLACK)
    screen.blit(player_one_score_text, (25, 10))
    screen.blit(player_two_score_text, (325, 10))

    # Draw grid lines
    pygame.draw.line(screen, WHITE, (200, 50), (200, 650), 5)
    pygame.draw.line(screen, WHITE, (400, 50), (400, 650), 5)
    pygame.draw.line(screen, WHITE, (0, 250), (600, 250), 5)
    pygame.draw.line(screen, WHITE, (0, 450), (600, 450), 5)

    # Draw game state
    for row in range(3):
        for col in range(3):
            if game_state[row][col] == 'X':
                symbol = player_one_symbol
                color = player_one_color
            elif game_state[row][col] == 'O':
                symbol = player_two_symbol
                color = player_two_color
            else:
                continue

            if symbol == 'X':
                pygame.draw.line(screen,
                                 color,
                                 (col * 200 + 25,
                                  row * 200 + 75),
                                 (col * 200 + 175,
                                  row * 200 + 225),
                                 5)
                pygame.draw.line(screen,
                                 color,
                                 (col * 200 + 175,
                                  row * 200 + 75),
                                 (col * 200 + 25,
                                  row * 200 + 225),
                                 5)
            elif symbol == 'O':
                pygame.draw.circle(screen,
                                   color,
                                   (col * 200 + 100,
                                    row * 200 + 150),
                                   75,
                                   5)
            elif symbol == 'Square':
                pygame.draw.rect(screen,
                                 color,
                                 (col * 200 + 25,
                                  row * 200 + 75,
                                  150,
                                  150),
                                 5)
            else:
                symbol_text = font.render(symbol, True, color)
                screen.blit(symbol_text,
                            (col * 200 +
                             (200 - symbol_text.get_width()) // 2,
                             row * 200 +
                             (200 - symbol_text.get_height()) // 2 +
                             50))

def handle_click(pos):
    global current_player
    global game_state
    global player_one_wins
    global player_two_wins

    # Determine row and column of click
    col = pos[0] // 200
    row = pos[1] // 200

    # Make move if valid
    if game_state[row][col] is None:
        game_state[row][col] = current_player

        # Play sound
        if current_player == 'X':
            bubble_sound.play()
        else:
            ding_sound.play()

        # Check for win
        winner = check_for_win()
        if winner == 'X':
            player_one_wins +=1
            # Reset game state
            game_state = [[None, None, None], [None, None, None], [None, None, None]]
        elif winner == 'O':
            player_two_wins +=1
            # Reset game state
            game_state = [[None, None, None], [None, None, None], [None, None, None]]
        elif winner == 'Draw':
            # Reset game state
            game_state = [[None, None, None], [None, None, None], [None, None, None]]

        # Switch current player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

def check_for_win():
    # Check rows
    for row in range(3):
        if game_state[row][0] is not None and game_state[row][0] == game_state[row][1] == game_state[row][2]:
            return game_state[row][0]

    # Check columns
    for col in range(3):
        if game_state[0][col] is not None and game_state[0][col] == game_state[1][col] == game_state[2][col]:
            return game_state[0][col]

    # Check diagonals
    if game_state[0][0] is not None and game_state[0][0] == game_state[1][1] == game_state[2][2]:
        return game_state[0][0]
    if game_state[2][0] is not None and game_state[2][0] == game_state[1][1] == game_state[0][2]:
        return game_state[2][0]

    # Check for draw
    for row in range(3):
        for col in range(3):
            if game_state[row][col] is None:
                return None

    return 'Draw'

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    # Draw screen
    draw_game_state()
    pygame.display.update()
#
#
# import pygame
# import os
#
# # initialize pygame
# pygame.init()
#
# # set screen size and create screen object
# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # set colors
# black = (0, 0, 0)
# red = (255, 0, 0)
# white = (255, 255, 255)
#
# # set sounds
# bubble_sound = pygame.mixer.Sound(os.path.join('', 'bubble.wav'))
# ding_sound = pygame.mixer.Sound(os.path.join('', 'ding.wav'))
#
# # set background music
# pygame.mixer.music.load(os.path.join('', 'background.mp3'))
# pygame.mixer.music.play(-1)
#
# # set font
# font = pygame.font.Font(None, 36)
#
# # game variables
# player_one_wins = 0
# player_two_wins = 0
# player_one_symbol = 'X'
# player_two_symbol = 'O'
# player_one_color = red
# player_two_color = red
#
# def draw_text(text, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, text_rect)
#
# def draw_scoreboard():
#     # draw white square at top of screen for scoreboard
#     pygame.draw.rect(screen, white, (0, 0, screen_width, 50))
#     # draw player one wins and symbol
#     draw_text(f'Player One: {player_one_wins} ({player_one_symbol})', player_one_color, screen_width/4, 25)
#     # draw player two wins and symbol
#     draw_text(f'Player Two: {player_two_wins} ({player_two_symbol})', player_two_color, screen_width*3/4, 25)
#
# def draw_grid():
#     # draw vertical lines
#     pygame.draw.line(screen, white, (200, 100), (200, 500), 5)
#     pygame.draw.line(screen, white, (400, 100), (400, 500), 5)
#     # draw horizontal lines
#     pygame.draw.line(screen, white, (100, 200), (500, 200), 5)
#     pygame.draw.line(screen, white, (100, 300), (500, 300), 5)
#     pygame.draw.line(screen, white, (100, 400), (500, 400), 5)
#
# def draw_symbol(x, y, symbol):
#     if symbol == player_one_symbol:
#         color = player_one_color
#         sound = bubble_sound
#     else:
#         color = player_two_color
#         sound = ding_sound
#     draw_text(symbol, color, x*200+150, y*100+150)
#     sound.play()
#
# def check_win(grid):
#     # check rows
#     for row in grid:
#         if row[0] == row[1] == row[2] and row[0] != '':
#             return row[0]
#     # check columns
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '':
#             return grid[0][col]
#     # check diagonals
#     if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
#         return grid[0][0]
#     if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '':
#         return grid[0][2]
#     # check for tie
#     tie = True
#     for row in grid:
#         for cell in row:
#             if cell == '':
#                 tie = False
#                 break
#         if not tie:
#             break
#     if tie:
#         return 'Tie'
#     return None
#
# def show_endgame_message(winner):
#     if winner == player_one_symbol:
#         draw_text('Player One Wins!', white, screen_width/2, screen_height/2)
#         global player_one_wins
#         player_one_wins += 1
#     elif winner == player_two_symbol:
#         draw_text('Player Two Wins!', white, screen_width/2, screen_height/2)
#         global player_two_wins
#         player_two_wins += 1
#     else:
#         draw_text('Tie!', white, screen_width/2, screen_height/2)
#     pygame.display.update()
#     pygame.time.wait(3000)
#
# def main():
#     global player_one_symbol
#     global player_two_symbol
#     global player_one_color
#     global player_two_color
#
#     # set game variables
#     grid = [['', '', ''], ['', '', ''], ['', '', '']]
#     turn = 0
#
#     # game loop
#     running = True
#     while running:
#         # handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 if y > 100:
#                     row = (y-100)//100
#                     col = x//200
#                     if grid[row][col] == '':
#                         if turn % 2 == 0:
#                             grid[row][col] = player_one_symbol
#                             draw_symbol(col, row, player_one_symbol)
#                         else:
#                             grid[row][col] = player_two_symbol
#                             draw_symbol(col, row, player_two_symbol)
#                         turn += 1
#
#         # check for win
#         winner = check_win(grid)
#         if winner is not None:
#             show_endgame_message(winner)
#             grid = [['', '', ''], ['', '', ''], ['', '', '']]
#             turn = 0
#
#         # draw screen
#         screen.fill(black)
#         draw_grid()
#         for row in range(3):
#             for col in range(3):
#                 symbol = grid[row][col]
#                 if symbol != '':
#                     draw_symbol(col, row, symbol)
#         draw_scoreboard()
#         pygame.display.update()
#
# if __name__ == '__main__':
#     main()


# import pygame
# import os
#
# # initialize pygame
# pygame.init()
#
# # set screen size and create screen object
# screen_width = 600
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
#
# # set colors
# black = (0, 0, 0)
# red = (255, 0, 0)
# white = (255, 255, 255)
#
# # set sounds
# bubble_sound = pygame.mixer.Sound(os.path.join('', 'bubble.wav'))
# ding_sound = pygame.mixer.Sound(os.path.join('', 'ding.wav'))
#
# # set background music
# pygame.mixer.music.load(os.path.join('', 'background.mp3'))
# pygame.mixer.music.play(-1)
#
# # set font
# font = pygame.font.Font(None, 72)
#
# # game variables
# player_one_wins = 0
# player_two_wins = 0
# player_one_symbol = 'X'
# player_two_symbol = 'O'
# player_one_color = red
# player_two_color = red
#
# def draw_text(text, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, text_rect)
#
# def draw_scoreboard():
#     # draw white square at top of screen for scoreboard
#     pygame.draw.rect(screen, white, (0, 0, screen_width, 50))
#     # draw player one wins and symbol
#     draw_text(f'Player One: {player_one_wins} ({player_one_symbol})', player_one_color, screen_width/4, 25)
#     # draw player two wins and symbol
#     draw_text(f'Player Two: {player_two_wins} ({player_two_symbol})', player_two_color, screen_width*3/4, 25)
#
# def draw_grid():
#     # draw vertical lines
#     pygame.draw.line(screen, white, (200, 150), (200, 450), 5)
#     pygame.draw.line(screen, white, (400, 150), (400, 450), 5)
#     # draw horizontal lines
#     pygame.draw.line(screen, white, (100, 250), (500, 250), 5)
#     pygame.draw.line(screen, white, (100, 350), (500, 350), 5)
#
# def draw_symbol(x, y, symbol):
#     if symbol == player_one_symbol:
#         color = player_one_color
#         sound = bubble_sound
#     else:
#         color = player_two_color
#         sound = ding_sound
#     draw_text(symbol, color, x*200+150, y*100+200)
#
# def check_win(grid):
#     # check rows
#     for row in grid:
#         if row[0] == row[1] == row[2] and row[0] != '':
#             return row[0]
#     # check columns
#     for col in range(3):
#         if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '':
#             return grid[0][col]
#     # check diagonals
#     if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
#         return grid[0][0]
#     if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '':
#         return grid[0][2]
#     # check for tie
#     tie = True
#     for row in grid:
#         for cell in row:
#             if cell == '':
#                 tie = False
#                 break
#         if not tie:
#             break
#     if tie:
#         return 'Tie'
#     return None
#
# def show_endgame_message(winner):
#     if winner == player_one_symbol:
#         draw_text('Player One Wins!', white, screen_width/2, screen_height/2)
#         global player_one_wins
#         player_one_wins += 1
#     elif winner == player_two_symbol:
#         draw_text('Player Two Wins!', white, screen_width/2, screen_height/2)
#         global player_two_wins
#         player_two_wins += 1
#     else:
#         draw_text('Tie!', white, screen_width/2, screen_height/2)
#     pygame.display.update()
#     pygame.time.wait(3000)
#
# def main():
#     global player_one_symbol
#     global player_two_symbol
#     global player_one_color
#     global player_two_color
#
#     # set game variables
#     grid = [['', '', ''], ['', '', ''], ['', '', '']]
#     turn = 0
#
#     # game loop
#     running = True
#     while running:
#         # handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 if y > 150:
#                     row = (y-150)//100
#                     col = x//200
#                     if grid[row][col] == '':
#                         if turn % 2 == 0:
#                             grid[row][col] = player_one_symbol
#                             draw_symbol(col, row, player_one_symbol)
#                             bubble_sound.play()
#                         else:
#                             grid[row][col] = player_two_symbol
#                             draw_symbol(col, row, player_two_symbol)
#                             ding_sound.play()
#                         turn += 1
#
#         # check for win
#         winner = check_win(grid)
#         if winner is not None:
#             show_endgame_message(winner)
#             grid = [['', '', ''], ['', '', ''], ['', '', '']]
#             turn = 0
#
#         # draw screen
#         screen.fill(black)
#         draw_grid()
#         for row in range(3):
#             for col in range(3):
#                 symbol = grid[row][col]
#                 if symbol != '':
#                     draw_symbol(col, row, symbol)
#         draw_scoreboard()
#         pygame.display.update()
#
# if __name__ == '__main__':
#     main()














# compiler phase two?
#
# class Parser:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.pos = 0
#
#     def parse(self):
#         return self.parse_program()
#
#     def parse_program(self):
#         return ('program', self.parse_declaration_list())
#
#     def parse_declaration_list(self):
#         declarations = []
#         while self.peek_type() in ['int', 'void']:
#             declarations.append(self.parse_declaration())
#         return ('declaration_list', declarations)
#
#     def parse_declaration(self):
#         decl_initial = self.parse_declaration_initial()
#         decl_prime = self.parse_declaration_prime()
#         return ('declaration', decl_initial, decl_prime)
#
#     def parse_declaration_initial(self):
#         type_specifier = self.consume()
#         id = self.consume()
#         return ('declaration_initial', type_specifier, id)
#
#     def parse_declaration_prime(self):
#         if self.peek() == '(':
#             return ('fun_declaration_prime', self.parse_fun_declaration_prime())
#         else:
#             return ('var_declaration_prime', self.parse_var_declaration_prime())
#
#     def parse_var_declaration_prime(self):
#         if self.peek() == ';':
#             self.consume(';')
#             return ('var_declaration_end',)
#         elif self.peek() == '[':
#             self.consume('[')
#             num = int(self.consume())
#             self.consume(']')
#             self.consume(';')
#             return ('var_declaration_array', num)
#
#     def parse_fun_declaration_prime(self):
#         self.consume('(')
#         params = self.parse_params()
#         self.consume(')')
#         compound_stmt = self.parse_compound_stmt()
#         return ('fun_declaration', params, compound_stmt)
#
#     def parse_params(self):
#         if self.peek() == 'int':
#             type_specifier = self.consume()
#             id = self.consume()
#             param_prime = self.parse_param_prime()
#             param_list = self.parse_param_list()
#             return ('params_int', type_specifier, id, param_prime, param_list)
#         elif self.peek() == 'void':
#             type_specifier = self.consume()
#             return ('params_void', type_specifier)
#
#     def parse_param_list(self):
#         params = []
#         while self.peek() == ',':
#             self.consume(',')
#             params.append(self.parse_param())
#         return ('param_list', params)
#
#     def parse_param(self):
#         decl_initial = self.parse_declaration_initial()
#         param_prime = self.parse_param_prime()
#         return ('param', decl_initial, param_prime)
#
#     def parse_param_prime(self):
#         if self.peek() == '[':
#             self.consume('[')
#             self.consume(']')
#             return ('param_array',)
#         else:
#             return ('param_end',)
#
#     def parse_compound_stmt(self):
#
#     # ...
#
#     # ...
#
#     def peek(self):
#         if self.pos < len(self.tokens):
#             return self.tokens[self.pos][1]
#         else:
#             return None
#
#     def peek_type(self):
#         if self.pos < len(self.tokens):
#             return self.tokens[self.pos][0]
#         else:
#             return None
#
#     def consume(self, expected=None):
#         token = self.peek()
#         if expected and token != expected:
#             raise Exception(f"Expected {expected}, got {token}")
#         self.pos += 1
#         return token
#
#
# # Load the tokenized input from the file
# with open('tokens.txt', 'r') as f:
#     tokens = [tuple(line.strip().split()) for line in f]
#
# # Create a new parser object
# parser = Parser(tokens)
#
# # Parse the tokenized input
# ast = parser.parse()
#
# # Print the AST
# print(ast)
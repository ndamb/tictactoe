import pygame
from pygame.locals import QUIT
from tkinter import Tk
from tkinter.simpledialog import askstring
from winning_patterns import winning_patterns
from drawing_stuff import draw_main_menu
from drawing_stuff import draw_options
from drawing_stuff import draw_game_field

options = False
first_run = True
HEIGHT = 300
WIDTH = 300
SCREEN_CLR = (75, 75, 75)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

player_sign_list = ["X", "O"]
game_matrix = ["_", "_", "_",
               "_", "_", "_",
               "_", "_", "_"]
curr_player = 0


def main(curr_player, first_run, options):
    running = True
    root = Tk()
    root.wm_withdraw()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    draw_main_menu(screen)
    pygame.display.set_caption("Tic-Tac-Toe")
    while running:
        pygame.display.update()
        if winning_patterns(game_matrix) is False:
            print("Spiel wird beendet.")
            running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_pos = pos[0]
                y_pos = pos[1]
                if options:
                    if x_pos > 250 and x_pos < 290 and y_pos > 250 and y_pos < 290:
                        draw_main_menu(screen)
                        options = False
                elif first_run:
                    if x_pos > 30 and x_pos < 110 and y_pos > 250 and y_pos < 290:
                        first_run = False
                        draw_game_field(screen, first_run)
                    if x_pos > 150 and x_pos < 230 and y_pos > 250 and y_pos <290:
                        draw_options(screen)
                        options = True
                else:
                    if x_pos > 0 and x_pos < 100 and y_pos > 0 and y_pos < 100:
                        if game_matrix[0] == "_":
                            if curr_player == 0:
                                game_matrix[0] = "X"
                                pygame.draw.line(screen, RED, (0, 0), (100, 100), 5)
                                pygame.draw.line(screen, RED, (100, 0), (0, 100), 5)
                            if curr_player == 1:
                                game_matrix[0] = "O"
                                pygame.draw.circle(screen, BLUE, (50, 50), 45, 3)
                            curr_player += 1
                            if curr_player == 2: curr_player = 0
                        else:
                            continue
                    if x_pos >= 100 and x_pos < 200 and y_pos > 0 and y_pos < 100:
                        if game_matrix[1] == "_":
                            if curr_player == 0:
                                game_matrix[1] = "X"
                                pygame.draw.line(screen, RED, (100, 0), (200, 100), 5)
                                pygame.draw.line(screen, RED, (200, 0), (100, 100), 5)
                            if curr_player == 1:
                                game_matrix[1] = "O"
                                pygame.draw.circle(screen, BLUE, (150, 50), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos >= 200 and x_pos < 300 and y_pos > 0 and y_pos < 100:
                        if game_matrix[2] == "_":
                            if curr_player == 0:
                                game_matrix[2] = "X"
                                pygame.draw.line(screen, RED, (200, 0), (300, 100), 5)
                                pygame.draw.line(screen, RED, (300, 0), (200, 100), 5)
                            if curr_player == 1:
                                game_matrix[2] = "O"
                                pygame.draw.circle(screen, BLUE, (250, 50), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos > 0 and x_pos < 100 and y_pos > 100 and y_pos < 200:
                        if game_matrix[3] == "_":
                            if curr_player == 0:
                                game_matrix[3] = "X"
                                pygame.draw.line(screen, RED, (0, 100), (100, 200), 5)
                                pygame.draw.line(screen, RED, (100, 100), (0, 200), 5)
                            if curr_player == 1:
                                game_matrix[3] = "O"
                                pygame.draw.circle(screen, BLUE, (50, 150), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos > 100 and x_pos < 200 and y_pos > 100 and y_pos < 200:
                        if game_matrix[4] == "_":
                            if curr_player == 0:
                                game_matrix[4] = "X"
                                pygame.draw.line(screen, RED, (100, 100), (200, 200), 5)
                                pygame.draw.line(screen, RED, (200, 100), (100, 200), 5)
                            if curr_player == 1:
                                game_matrix[4] = "O"
                                pygame.draw.circle(screen, BLUE, (150, 150), 50, 5)
                            curr_player += 1
                            if curr_player == 2: curr_player = 0
                        else:
                            continue
                    if x_pos > 200 and x_pos < 300 and y_pos > 100 and y_pos < 200:
                        if game_matrix[5] == "_":
                            if curr_player == 0:
                                game_matrix[5] = "X"
                                pygame.draw.line(screen, RED, (200, 100), (300, 200), 5)
                                pygame.draw.line(screen, RED, (300, 100), (200, 200), 5)
                            if curr_player == 1:
                                game_matrix[5] = "O"
                                pygame.draw.circle(screen, BLUE, (250, 150), 50, 5)
                            curr_player += 1

                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos > 0 and x_pos < 100 and y_pos > 200 and y_pos < 300:
                        if game_matrix[6] == "_":
                            if curr_player == 0:
                                game_matrix[6] = "X"
                                pygame.draw.line(screen, RED, (0, 200), (100, 300), 5)
                                pygame.draw.line(screen, RED, (100, 200), (0, 300), 5)
                            if curr_player == 1:
                                game_matrix[6] = "O"
                                pygame.draw.circle(screen, BLUE, (50, 250), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos > 100 and x_pos < 200 and y_pos > 200 and y_pos < 300:
                        if game_matrix[7] == "_":
                            if curr_player == 0:
                                game_matrix[7] = "X"
                                pygame.draw.line(screen, RED, (100, 200), (200, 300), 5)
                                pygame.draw.line(screen, RED, (200, 200), (100, 300), 5)
                            if curr_player == 1:
                                game_matrix[7] = "O"
                                pygame.draw.circle(screen, BLUE, (150, 250), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue
                    if x_pos > 200 and x_pos < 300 and y_pos > 200 and y_pos < 300:
                        if game_matrix[8] == "_":
                            if curr_player == 0:
                                game_matrix[8] = "X"
                                pygame.draw.line(screen, RED, (200, 200), (300, 300), 5)
                                pygame.draw.line(screen, RED, (300, 200), (200, 300), 5)
                            if curr_player == 1:
                                game_matrix[8] = "O"
                                pygame.draw.circle(screen, BLUE, (250, 250), 50, 5)
                            curr_player += 1
                            if curr_player == 2:curr_player = 0
                        else:
                            continue


while True:
    main(curr_player, first_run, options)
    user_choice = askstring("Weiterspielen", "Weiterspielen?(Ja/Nein)")
    if user_choice == "Ja":
        curr_player = 0
        game_matrix = ["_", "_", "_",
                       "_", "_", "_",
                       "_", "_", "_"]
    else:
        break

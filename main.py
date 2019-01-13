import pygame
from pygame.locals import QUIT
from tkinter import Tk
from tkinter.simpledialog import askstring
from winning_patterns import winning_patterns
from drawing_stuff import draw_main_menu
from drawing_stuff import draw_options
from drawing_stuff import draw_game_field
from drawing_stuff import draw_ki
from random import randint
from mouse_positions import mouse_positions

options = False
first_run = True
ki = False
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


def main(curr_player, first_run, options, ki):
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
                    if x_pos > 20 and x_pos < 100 and y_pos > 30 and y_pos < 70:
                        print("Selected KI")
                        ki = True
                elif first_run:
                    if x_pos > 30 and x_pos < 110 and y_pos > 250 and y_pos < 290:
                        first_run = False
                        draw_game_field(screen)
                    if x_pos > 150 and x_pos < 230 and y_pos > 250 and y_pos <290:
                        draw_options(screen)
                        options = True
                else:
                    print("ki is", ki)
                    print("curr player is", curr_player)
                    if ki and curr_player is 1:
                        print("KI is choosing a field...")
                        ki_choice = randint(0, 8)
                        print("KI chose field number ", ki_choice)
                        print("checking if field is avaible")
                        if game_matrix[ki_choice] in player_sign_list:
                            print("ERROR: field as already a sign.")
                            continue
                        else:
                            print("Sucess: continuing to place the sign")
                            draw_ki(screen, ki_choice)

                    elif mouse_positions(game_matrix, screen, x_pos, y_pos, RED, BLUE, curr_player) is False:
                        print("continue 1338")
                        continue
                    else:
                        curr_player += 1
                        if curr_player is 2:
                            curr_player = 0


while True:
    main(curr_player, first_run, options, ki)
    user_choice = askstring("Weiterspielen", "Weiterspielen?(Ja/Nein)")
    if user_choice == "Ja":
        curr_player = 0
        game_matrix = ["_", "_", "_",
                       "_", "_", "_",
                       "_", "_", "_"]
    else:
        break

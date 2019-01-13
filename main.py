import pygame
from pygame.locals import QUIT
from tkinter import Tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from winning_patterns import winning_patterns
import time

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

def draw_main_menu(screen):
    screen.fill(WHITE)
    pygame.font.init()
    title_font = pygame.font.SysFont("Comic Sans MS", 30)
    textsurface = title_font.render("Tic-Tac-Toe", False, (0, 0, 0))
    screen.blit(textsurface, (70, 100))
    button_font = pygame.font.SysFont("Comic Sans MS", 15)
    buttonsurface = button_font.render("Start", False, (0, 0, 0))
    pygame.draw.rect(screen, SCREEN_CLR, (30, 250, 80, 40), 0)
    screen.blit(buttonsurface, (50, 260))
    pygame.draw.rect(screen, SCREEN_CLR, (150, 250, 80, 40), 0)
    buttonsurface2 = button_font.render("Optionen", False, (0, 0, 0))
    screen.blit(buttonsurface2, (160, 260))
    first_run = False

def draw_options(screen):
    screen.fill(WHITE)
    pygame.draw.rect(screen, SCREEN_CLR, (250, 250, 40, 40))
    button_font = pygame.font.SysFont("Comic Sans MS", 30)
    button_surface = button_font.render("<-", False, (0, 0, 0))
    screen.blit(button_surface, (260, 247))
    options = True
    return options
def draw_game_field(screen, first_run):
    """if first_run:
        print(" i am here")
        screen.fill(WHITE)
        pygame.font.init()
        title_font = pygame.font.SysFont("Comic Sans MS", 30)
        textsurface = title_font.render("Tic-Tac-Toe", False, (0, 0, 0))
        screen.blit(textsurface, (70, 100))
        button_font = pygame.font.SysFont("Comic Sans MS", 15)
        buttonsurface = button_font.render("Start", False, (0, 0, 0))
        pygame.draw.rect(screen, SCREEN_CLR, (30, 250, 80, 40), 0)
        screen.blit(buttonsurface, (50, 260))
        pygame.draw.rect(screen, SCREEN_CLR, (150, 250, 80, 40), 0)
        buttonsurface2 = button_font.render("Optionen", False, (0, 0, 0))
        screen.blit(buttonsurface2, (160, 260))
        first_run = False
        return first_run"""
    #if first_run is False:
    screen.fill(SCREEN_CLR)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)


def main(curr_player, first_run, options):
    running = True
    root = Tk()
    root.wm_withdraw()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    print("click lcick")
    draw_main_menu(screen)
    #draw_game_field(screen, first_run)
    pygame.display.set_caption("Tic-Tac-Toe")
    messagebox.showinfo("Information", "Bitte bestaetigen und Spielernamen eingeben!")
    player_1 = askstring("Spielernamen", "Name: ")
    player_2 = askstring("Spielernamen", "Name: ")
    if player_1 == "" or player_1 is None: player_1 = "Spieler 1"
    if player_2 == "" or player_2 is None: player_2 = "Spieler 2"
    player_list = [player_1, player_2]
    print(player_list)
    print("ft is", first_run)
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
                print("Current game matrix is: ", game_matrix)
                x_pos = pos[0]
                y_pos = pos[1]
                print("X position is: ", x_pos)
                print("Y position is: ", y_pos)
                print("ft is", first_run)
                if options:
                    print("meddl")
                    if x_pos > 250 and x_pos < 290 and y_pos > 250 and y_pos < 290:
                        print("OPPPTIONSSS")
                        draw_main_menu(screen)
                        options = False
                elif first_run:
                    print("xdddddd")
                    if x_pos > 30 and x_pos < 110 and y_pos > 250 and y_pos < 290:
                        first_run = False
                        draw_game_field(screen, first_run)
                    if x_pos > 150 and x_pos < 230 and y_pos > 250 and y_pos <290:
                        draw_options(screen)
                        options = True
                else:
                    if x_pos > 0 and x_pos < 100 and y_pos > 0 and y_pos < 100:
                        print("Selected first field!")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected second field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected third field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Select fourth field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected fifth field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected sixth field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected seventh field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected eigth field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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
                        print("Selected ninth field")
                        print("Derzeitger Spieler ist: ", player_list[curr_player])
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

import pygame
from pygame.locals import QUIT
from tkinter import Tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from winning_patterns import winning_patterns

HEIGHT = 300
WIDTH = 300
SCREEN_CLR = (75, 75, 75)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player_sign_list = ["X", "O"]
game_matrix = ["_", "_", "_",
               "_", "_", "_",
               "_", "_", "_"]
curr_player = 0


def draw_game_field(screen):
    screen.fill(SCREEN_CLR)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)


def main():
    running = True
    root = Tk()
    root.wm_withdraw()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    draw_game_field(screen)
    messagebox.showinfo("Information", "Bitte bestaetigen und Spielernamen eingeben!")
    player_1 = askstring("Spielernamen", "Name: ")
    player_2 = askstring("Spielernamen", "Name: ")
    if player_1 == "" or player_1 is None: player_1 = "Spieler 1"
    if player_2 == "" or player_2 is None: player_2 = "Spieler 2"
    player_list = [player_1, player_2]
    print(player_list)
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


while True:
    main()
    user_choice = askstring("Weiterspielen", "Weiterspielen?(Ja/Nein)")
    if user_choice == "Ja":
        curr_player = 0
        game_matrix = ["_", "_", "_",
                       "_", "_", "_",
                       "_", "_", "_"]
    else:
        break

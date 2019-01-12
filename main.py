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


def main(curr_player):
    running = True
    root = Tk()
    root.wm_withdraw()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(SCREEN_CLR)
    pygame.display.set_caption("Tic-Tac-Toe")
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
    messagebox.showinfo("Information", "Bitte bestaetigen und Spielernamen eingeben!")
    player_1 = askstring("Spielernamen", "Name: ")
    player_2 = askstring("Spielernamen", "Name: ")
    if player_1 == "" or player_1 == None: player_1 = "Spieler 1"
    if player_2 == "" or player_2 == None: player_2 = "Spieler 2"
    player_list = [player_1, player_2]
    print(player_list)
    while running:
        pygame.display.update()
        if winning_patterns(game_matrix) == False:
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
    main(curr_player)
    user_choice = askstring("Weiterspielen", "Weiterspielen?(Ja/Nein)")
    if user_choice == "Ja":
        curr_player = 0
        game_matrix = ["_", "_", "_",
                       "_", "_", "_",
                       "_", "_", "_"]
    else:
        break

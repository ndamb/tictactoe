import pygame


def mouse_positions(game_matrix, screen, x_pos, y_pos, RED, BLUE, curr_player):
    print("Inside mouse pos!")
    print("values are: ", game_matrix, x_pos, y_pos, curr_player)
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
            if curr_player == 2:curr_player = 0
            return True, curr_player
        else:
            print("check 1")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 2")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 1 2 3")
            return False
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
            if curr_player == 2: curr_player = 0
        else:
            print("check 1 2 4")
            return False
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
            return True, curr_player
        else:
            print("check 1 2 5")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 1 2 6")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 1 2 7")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 1 2 8")
            return False
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
            if curr_player == 2: curr_player = 0
            return True, curr_player
        else:
            print("check 1 2 9")
            return False

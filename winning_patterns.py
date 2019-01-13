def winning_patterns(game_matrix):
    if game_matrix[0] == game_matrix[1] == game_matrix[2] == "X":
        running = False
        return running
    elif game_matrix[3] == game_matrix[4] == game_matrix[5] == "X":
        running = False
        return running
    elif game_matrix[6] == game_matrix[7] == game_matrix[8] == "X":
        running = False
        return running
    elif game_matrix[0] == game_matrix[3] == game_matrix[6] == "X":
        running = False
        return running
    elif game_matrix[1] == game_matrix[4] == game_matrix[7] == "X":
        running = False
        return running
    elif game_matrix[2] == game_matrix[5] == game_matrix[8] == "X":
        running = False
        return running
    elif game_matrix[0] == game_matrix[4] == game_matrix[8] == "X":
        running = False
        return running
    elif game_matrix[2] == game_matrix[4] == game_matrix[6] == "X":
        running = False
        return running
    elif game_matrix[0] == game_matrix[1] == game_matrix[2] == "O":
        running = False
        return running
    elif game_matrix[3] == game_matrix[4] == game_matrix[5] == "O":
        running = False
        return running
    elif game_matrix[6] == game_matrix[7] == game_matrix[8] == "O":
        running = False
        return running
    elif game_matrix[1] == game_matrix[3] == game_matrix[6] == "O":
        running = False
        return running
    elif game_matrix[1] == game_matrix[4] == game_matrix[7] == "O":
        running = False
        return running
    elif game_matrix[2] == game_matrix[5] == game_matrix[8] == "O":
        running = False
        return running
    elif game_matrix[0] == game_matrix[4] == game_matrix[8] == "O":
        running = False
        return running
    elif game_matrix[2] == game_matrix[4] == game_matrix[6] == "O":
        running = False
        return running
    else:
        empty_fields = 0
        for x in game_matrix:
            if x == "_":
                empty_fields += 1
        if empty_fields == 0:
            running = False
            return running
        else:
            #print("GAME STILL RUNNING")
            pass

def winning_patterns(game_matrix):
    if game_matrix[0] == game_matrix[1] == game_matrix[2] == "X":
        print("WIN WIN1")
        running = False
        return running
    elif game_matrix[3] == game_matrix[4] == game_matrix[5] == "X":
        print("WIN WIN2")
        running = False
        return running
    elif game_matrix[6] == game_matrix[7] == game_matrix[8] == "X":
        print("WIN WIN3")
        running = False
        return running
    elif game_matrix[0] == game_matrix[3] == game_matrix[6] == "X":
        print("WIN WIN4")
        running = False
        return running
    elif game_matrix[1] == game_matrix[4] == game_matrix[7] == "X":
        print("WIN WIN5")
        running = False
        return running
    elif game_matrix[2] == game_matrix[5] == game_matrix[8] == "X":
        print("WIN WIN6")
        running = False
        return running
    elif game_matrix[0] == game_matrix[4] == game_matrix[8] == "X":
        print("WIN WIN7")
        running = False
        return running
    elif game_matrix[2] == game_matrix[4] == game_matrix[6] == "X":
        print("WIN WIN8")
        running = False
        return running
    elif game_matrix[0] == game_matrix[1] == game_matrix[2] == "O":
        print("WIN WIN9")
        running = False
        return running
    elif game_matrix[3] == game_matrix[4] == game_matrix[5] == "O":
        print("WIN WIN11")
        running = False
        return running
    elif game_matrix[6] == game_matrix[7] == game_matrix[8] == "O":
        print("WIN WIN22")
        running = False
        return running
    elif game_matrix[1] == game_matrix[3] == game_matrix[6] == "O":
        print("WIN WIN33")
        running = False
        return running
    elif game_matrix[1] == game_matrix[4] == game_matrix[7] == "O":
        print("WIN WIN44")
        running = False
        return running
    elif game_matrix[2] == game_matrix[5] == game_matrix[8] == "O":
        print("WIN WIN55")
        running = False
        return running
    elif game_matrix[0] == game_matrix[4] == game_matrix[8] == "O":
        print("WIN WIN66")
        running = False
        return running
    elif game_matrix[2] == game_matrix[4] == game_matrix[6] == "O":
        print("WIN WIN77")
        running = False
        return running
    else:
        empty_fields = 0
        for x in game_matrix:
            if x == "_":
                empty_fields += 1
        if empty_fields == 0:
            print("GAME FINISHED")
            running = False
            return running
        else:
            print("GAME STILL RUNNING")


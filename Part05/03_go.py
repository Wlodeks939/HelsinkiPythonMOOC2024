def who_won(game_board: list):

    count1 = 0
    count2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                count1 +=1
            elif game_board[i][j] == 2:  
                count2 +=1 

    if count1 > count2:
        return 1
    elif count2 > count1:
        return 2
    else:
        return 0            
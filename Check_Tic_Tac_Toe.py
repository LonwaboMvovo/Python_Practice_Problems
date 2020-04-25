# https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
def tic_tac_toe_winner(game):
    # Horizontal Posibilities:
    for rowi in range(3):
        game_set = []
        for coli in range(3):
            game_set.append(game[rowi][coli])
        if len(set(game_set)) == 1 and game_set[0] != 0:
            return f'The winner is player {game_set[0]} and they won with a Horizontal line'

    # Vertical Posibilities:
    for colj in range(3):
        game_set = []
        for rowj in range(3):
            game_set.append(game[rowj][colj])
        if len(set(game_set)) == 1 and game_set[0] != 0:
            return f'The winner is player {game_set[0]} and they won with a Vertical line'
    
    # Diagonal Posibilities:
    for dig in range(0,3,2):
        game_set = []
        game_set.append(game[0][dig])
        game_set.append(game[1][1])
        if dig == 0:
            game_set.append(game[2][2])
        else:
            game_set.append(game[2][0])
        if len(set(game_set)) == 1 and game_set[0] != 0:
            return f'The winner is player {game_set[0]} and they won with a Diagonal line'
    
    #Draw:
    return 'Draw'


game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]
print(tic_tac_toe_winner(game))

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]
print(tic_tac_toe_winner(winner_is_2))

winner_is_1 = [[1, 2, 0],
              [2, 1, 0],
              [2, 1, 1]]
print(tic_tac_toe_winner(winner_is_1))

winner_is_also_1 = [[0, 1, 0],
                   [2, 1, 0],
                   [2, 1, 1]]
print(tic_tac_toe_winner(winner_is_also_1))

no_winner = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 2]]
print(tic_tac_toe_winner(no_winner))

also_no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 0]]
print(tic_tac_toe_winner(also_no_winner))
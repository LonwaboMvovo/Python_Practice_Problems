# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
def draw_board():
    return f'''
    1   2   3
   --- --- --- 
1 | {board[0][0] if board[0][0] != 0 else ' '} | {board[0][1] if board[0][1] != 0 else ' '} | {board[0][2] if board[0][2] != 0 else ' '} |
   --- --- --- 
2 | {board[1][0] if board[1][0] != 0 else ' '} | {board[1][1] if board[1][1] != 0 else ' '} | {board[1][2] if board[1][2] != 0 else ' '} |
   --- --- --- 
3 | {board[2][0] if board[2][0] != 0 else ' '} | {board[2][1] if board[2][1] != 0 else ' '} | {board[2][2] if board[2][2] != 0 else ' '} |
   --- --- --- '''


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
    
    # When Game isn't over yet:
    for mrkx in range(3):
        for mrky in range(3):
            if game[mrkx][mrky] == 0: return False

    #Draw:
    return 'Draw'


playing_game = True
whos_turn = 1
board = [[0, 0, 0],
	     [0, 0, 0],
	     [0, 0, 0]]

print('\nTic-Tac-Toe!!!')

while playing_game:
    mark = 'X' if whos_turn % 2 != 0 else 'O'

    while True:
        try:
            coords = [int(num) for num in input(f'\nCoordinates of your move Player-{mark}: ').split(',')]
            assert coords[0] <= 3 and coords[0] >= 1 and coords[1] <= 3 and coords[1] >= 1 and board[coords[0]-1][coords[1]-1] == 0
            break
        except:
            print('\nInvalid entry. Enter a comma separated coordinate (row, col) for an open space on the board.\nFor example "1,3" will make this mark:')
            print('''
    1   2   3
   --- --- --- 
1 |   |   | X |
   --- --- --- 
2 |   |   |   |
   --- --- --- 
3 |   |   |   |
   --- --- --- ''')

    board[coords[0]-1][coords[1]-1] = mark
    print(draw_board())
    if not tic_tac_toe_winner(board): pass
    else: 
        print('\n'+tic_tac_toe_winner(board))
        playing_game = False
    whos_turn += 1

print('\nGame Over!!!')
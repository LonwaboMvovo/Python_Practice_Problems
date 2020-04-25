# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
def create_board(size):
    row = ['---' for _ in range(size)]
    col = ['   ' for _ in range(size)]

    for _ in range(size):
        print(f' {" ".join(row)} ')
        print(f'|{"|".join(col)}|')

    print(f' {" ".join(row)} ')


while True:
    try:
        length_of_board = int(input('What size game board would you like: '))
        create_board(length_of_board)
        break
    except ValueError:
        print('\nInvalid entry. You must enter an integer.')
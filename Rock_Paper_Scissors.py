# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
class Player:
    def __init__(self, response, valid, points):
        self.response = response
        self.valid = valid
        self.points = points


def who_wins(p1, p2):
    if p1 == 'r':
        if p2 == 'r':
            return 'Draw!'
        elif p2 == 'p':
            player2.points += 1
            return 'Paper beats Rock, Player 2 wins!'
        else:
            player1.points += 1
            return 'Rock beats Scissors, Player 1 wins!'
    elif p1 == 'p':
        if p2 == 'r':
            player1.points += 1
            return 'Paper beats Rock, Player 1 wins!'
        elif p2 == 'p':
            return 'Draw!'
        else:
            player2.points += 1
            return 'Scissors beats Paper, Player 2 wins!'
    else:
        if p2 == 'r':
            player2.points += 1
            return 'Rock beats Scissors, Player 2 wins!'
        elif p2 == 'p':
            player1.points += 1
            return 'Scissors beats Paper, Player 1 wins!'
        else:
            return 'Draw!'


player1 = Player('', False, 0)
player2 = Player('', False, 0)

print('\n(R)ock! (P)aper! (S)cissors!')

while True:
    while not player1.valid:
        player1.response = input('\nPlayer1=> ').lower()
        if player1.response == 'r' or player1.response == 'p' or player1.response == 's':
            player1.valid = True
            while not player2.valid:
                player2.response = input('\nPlayer2=> ').lower()
                if player2.response == 'r' or player2.response == 'p' or player2.response == 's':
                    player2.valid = True
                else:
                    print('Invalid answer Player 2. (R) for rock, (P) for paper and (S) for scissors')
        else: print('Invalid answer Player 1. (R) for rock, (P) for paper and (S) for scissors')
    print('\n' + who_wins(player1.response, player2.response))
    option = input('\nEnter any key to play again otherwise enter "QUIT" to end game: ').lower()
    if option == 'quit': break     
    player1.valid = False
    player2.valid = False

print('\nPlayer1 pts:', player1.points)
print('Player2 pts:', player2.points, '\n')

if player1.points > player2.points: print('Player 1 wins the game!!!')
elif player1.points < player2.points: print('Player 2 wins the game!!!')
else: print('The game ends in a draw!!!')

print('\nGAME OVER!!!')
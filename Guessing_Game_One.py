# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
from random import randint as randi
total_guesses = 0
correct_guesses = 0
user_guess = ''

while True:
    number_to_guess = randi(1, 9)
    while user_guess == '':
        try:
            user_guess = int(input('I have chosen a random number from 1 to 9.\nGuess it correctly and you win >> '))
        except ValueError:
            print('\nYou entered an invalid guess. Your guess must be an integer.\n')
    if user_guess > number_to_guess: print('\nToo high!', f'\nThe correct number was {number_to_guess}')
    elif user_guess < number_to_guess: print('\nToo low!', f'\nThe correct number was {number_to_guess}')
    else:
        correct_guesses += 1
        print('Correct!')
    total_guesses += 1
    if input('Press anything to continue otherwise if you would like to exit the game, enter "EXIT" >> ').upper() == 'EXIT': break
    user_guess = ''

if total_guesses == 1: print(f'\nYou guessed correctly {correct_guesses} out of {total_guesses} time')
else: print(f'\nYou guessed correctly {correct_guesses} out of {total_guesses} times')
print(f'\nTherefore your success rate was {round(correct_guesses/total_guesses*100, 2)}%')
print('\nGame Over!')
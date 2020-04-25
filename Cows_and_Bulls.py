# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
# The excercise says that a correct number in the correct position is a cow and just a correct number is a bull, but wikipedia says the opposite so imma go with wikipedia
from random import randint as randi

secret_number = ''
for _ in range(4): secret_number += str(randi(0,9))
guesses = 0

print('\nWelcome to the Cows and Bulls Game!')

while True:
    bulls = 0
    cows = 0
    guesses += 1

    while True:
        try:
            user_guess = input("\nEnter a number\n>>> ")
            assert len(user_guess) == 4 and int(user_guess) >= 0
            break
        except:
            print('\nInvalid input. Your guess must be a four digit number\nFor ex: "1234"')

    if user_guess == secret_number: break
    else:
        for i in range(4):
            if user_guess[i] == secret_number[i]: bulls +=1
            elif user_guess[i] in secret_number: cows += 1
    print(f'{cows} cows, {bulls} bulls')

if guesses == 1: print(f'\nWell done you guessed my secret number {secret_number} and it took you {guesses} try')
else: print(f'\nWell done you guessed my secret number {secret_number} and it took you {guesses} tries')

print('\nGame Over!')
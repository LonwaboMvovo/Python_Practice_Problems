# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
from Hangman_Game import game

while True:
    game()
    while True:
        try:
            play_again = input('\nDo you want to play again? ').lower()
            assert play_again == 'y' or play_again == 'n'
            break
        except: print("\nI don't understand that. Enter (Y) for yes if you would like to play again or (N) for no if you would like to stop playing.")  
    if play_again == 'n': break

print('\nGame Over!!!')
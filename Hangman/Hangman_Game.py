import random

def hanged_body(errs):
    hang_boi = ['   ____'
                ,'  |    |'
                ,'  |'
                ,'  |'
                ,'  |'
                ,'  |'
                ,' _|_'
                ,'|   |______'
                ,'|          |'
                ,'|__________|\n']
    if errs >= 1: hang_boi[2] = '  |    o'
    if errs >= 2: hang_boi[3] = '  |   /'
    if errs >= 3: hang_boi[3] = '  |   / \\'
    if errs >= 4:
        hang_boi[3] = '  |   /|\\'
        hang_boi[4] = '  |    |'
    if errs >= 5: hang_boi[5] = '  |   /'
    if errs == 6: hang_boi[5] = '  |   / \\'
    return hang_boi


def choose_word():
    with open('sowpods.txt', 'r') as wordsf:
        all_words = [word.strip() for word in wordsf]
    return random.choice(all_words)

    
def game():
    clue_word = choose_word()

    word_progress = ['_' for _ in range(len(clue_word))]
    word_progress_displayed = ''.join(word_progress)
    letters_guessed = []

    print('\n>>> Welcome to Hangman!')
    for hang_part in hanged_body(0): print(hang_part)
    print(' '.join(word_progress))
    times_wrong = 0
    while True:
        try:
            guess = input(f'\nUsed letters: {letters_guessed}\n>>> Guess your letter: ').upper()
            assert guess.isalpha() and len(guess) == 1
            if guess in letters_guessed: print(f'\nYou have already guessed the letter {guess}')
            elif guess not in clue_word:
                times_wrong += 1
                print('\nThat letter is not in the word')
                for hang_part in hanged_body(times_wrong): print(hang_part)
            else:
                for i in range(len(clue_word)):
                    if guess == clue_word[i]:
                        word_progress[i] = guess
            if guess not in letters_guessed: letters_guessed.append(guess)
        except: print('\nInvalid entry. Please enter a letter in the English alphabet')
        word_progress_displayed = ''.join(word_progress)
        print(' '.join(word_progress))
        if times_wrong == 6: 
            print(f"\nYup he's dead. Which means the game is over. The correct word was actually {clue_word}")
            break
        elif word_progress_displayed == clue_word:
            print(f'\nCongratulations you got the word: {clue_word}')
            break
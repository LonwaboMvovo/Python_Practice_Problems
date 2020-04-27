# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
clue_word = 'EVAPORATE'
word_progress = ['_ ' for _ in range(len(clue_word))]
word_progress_displayed = ''.join(word_progress)
letters_guessed = []

print('\n>>> Welcome to Hangman!')
print(word_progress_displayed)

while True:
    try:
        guess = input('\n>>> Guess your letter: ').upper()
        assert guess.isalpha() and len(guess) == 1
        if guess in letters_guessed: print(f'\nYou have already guessed the letter {guess}')
        elif guess not in clue_word and guess not in letters_guessed: print('\nThat letter is not in my word')
        else:
            letters_guessed.append(guess)
            for i in range(len(clue_word)):
                if guess == clue_word[i]:
                    word_progress[i] = guess
    except: print('Invalid entry. Please enter a letter in the English alphabet')
    word_progress_displayed = ''.join(word_progress)
    print(' '.join(word_progress))
    if word_progress_displayed == clue_word: break

print(f'\nCongratulations you got my word: {clue_word}')
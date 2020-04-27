# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
import random

with open('sowpods.txt', 'r') as wordsf:
    all_words = [word.strip() for word in wordsf]

print(random.choice(all_words))
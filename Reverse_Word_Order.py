# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
def sentence_reverser(sentence):
    return ' '.join(sentence.split()[::-1])


print(sentence_reverser(input('Long String: ')))
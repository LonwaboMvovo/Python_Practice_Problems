# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
from random import randint as randi

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_overlap_comprehensions = [i for i in set(a) if i in b]

print(list_overlap_comprehensions)

def rand_list():
    return [randi(0,100) for x in range(randi(10, 15))]

rand_a = rand_list()
rand_b = rand_list()

print(rand_a)
print(rand_b)

rand_list_overlap_comprehensions = [j for j in set(rand_a) if j in rand_b]
print(rand_list_overlap_comprehensions)
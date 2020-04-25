# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
from random import randint as randi

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_overlap = []

for number in a: list_overlap.append(number) if number in b and number not in list_overlap else None
print(list_overlap)

rand_a = []
rand_b = []
rand_list_overlap = []

for num_a in range(randi(10, 15)): rand_a.append(randi(0,100))
print(rand_a)

for num_b in range(randi(10, 15)): rand_b.append(randi(0,100))
print(rand_b)

for num in rand_a: rand_list_overlap.append(num) if num in rand_b and num not in rand_list_overlap else None
print(rand_list_overlap)
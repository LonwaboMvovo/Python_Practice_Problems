# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
from random import randint as randi

def no_duplicates_loop(givin_list):
    no_duplicates_loop_list = []
    for num in givin_list: no_duplicates_loop_list.append(num) if num not in no_duplicates_loop_list else None
    return no_duplicates_loop_list


def no_duplicates_set(givin_list):
    return [num for num in set(givin_list)]


my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(no_duplicates_loop(my_list))
print(no_duplicates_set(my_list))

def overlap_loop(list_a, list_b):
    overlap_loop_list = []
    for num in list_a: overlap_loop_list.append(num) if num in list_b and num not in overlap_loop_list else None
    return overlap_loop_list


def overlap_set(list_a, list_b):
    return [num for num in set(list_a) if num in list_b]


rand_a = []
rand_b = []

for _ in range(randi(10, 15)): rand_a.append(randi(0, 100))
for _ in range(randi(10, 15)): rand_b.append(randi(0, 100))

print(overlap_loop(rand_a, rand_b))
print(overlap_set(rand_a, rand_b))
# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
def first_and_last(array):
    return [array[0], array[-1]]


a = [5, 10, 15, 20, 25]
print(first_and_last(a))
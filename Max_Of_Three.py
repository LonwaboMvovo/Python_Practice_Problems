# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
def max_of_three(num1, num2, num3):
    max_num = num1
    
    if num2 > max_num: max_num = num2
    if num3 > max_num: max_num = num3
    
    return f'\nMax: {max_num}'


how_many_numbers = 3
numbers = []

print('\nMax of Three!')

for i in range(how_many_numbers):
    while True:
        try:
            numbers.append(float(input(f'\nNumber {i+1}: ')))
            break
        except ValueError: print(f'\nInvalid input! Number {i+1} is not a number')

print(max_of_three(numbers[0],numbers[2],numbers[2]))
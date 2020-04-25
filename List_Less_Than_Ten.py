# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_less_than_number = []

while True:
    try:
        check_number = int(input('Check number: '))
        break
    except ValueError:
        print('Please enter a valid number')

for number in list_a: list_less_than_number.append(number) if number < check_number else None
        
print(list_less_than_number)
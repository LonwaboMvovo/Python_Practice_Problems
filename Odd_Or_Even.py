# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
while True:
    try:
        num = int(input('Number: '))
        check = int(input('Check Number: '))
        break
    except ValueError:
        print('Please enter a valid number')

if num % check == 0:
    print(f'{num} is divisible by {check}')
else:
    print(f'{num} is not divisible by {check}')

if num % 2 == 0:
    print(f'and {num} is even')
else:
    print(f'and {num} is odd')
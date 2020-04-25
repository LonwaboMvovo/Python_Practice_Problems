# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
while True:
    try:
        number = int(input('Number: '))
        break
    except ValueError:
        print('Please enter a valid number')
divisors = []

for possible_divisor in range(1, number + 1):
    if number % possible_divisor == 0:
        divisors.append(possible_divisor)

print(divisors)
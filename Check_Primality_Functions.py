# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
def devisor_check(num):
    divisors = []
    for possible_divisor in range(1, num + 1):
        if num % possible_divisor == 0: divisors.append(possible_divisor)
    return divisors


while True:
    try:
        number_to_check = int(input('Number: '))
        break
    except ValueError:
        print('You have not entered a valid integer.\n')

if len(devisor_check(number_to_check)) < 3: print(f'\n{number_to_check} is a prime number')
else: print(f"\n{number_to_check} is not a prime number\nit's divisors are {devisor_check(number_to_check)}")
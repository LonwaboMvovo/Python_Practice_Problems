# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
def fibonacci_numbers(nums):
    fibonacci_list = []
    for _ in range(nums):
        if len(fibonacci_list) < 2: fibonacci_list.append(1)
        else: fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list


while True:
    try:
        list_length = int(input('\nHow many Fibonnaci numbers: '))
        print(fibonacci_numbers(list_length))
        break
    except ValueError:
        print('Invalid. Entry must be an integer')
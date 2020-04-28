# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

print('\nChoose a number between 0 and 100 and I will try guess it!!')

possible_guesses = list(range(101))
lies = '\n♫♫ ~ Why the f**k you lying?\nWhy you always lying\nHmmm oh my God\nStop f**king lying ~ ♫♫'
low = 0
upp = 100
counter = 1

while low < upp:
    mid = (low + upp) // 2
    my_guess = possible_guesses[mid]
    
    while True:
        response = input(f'\nIs your number {my_guess}? ').lower()
        if response == 'y' or response == 'n': break
        else: print("\nI don't understand. (Y) for yes and (N) for no")
    
    if response == 'y': break
    else:
        while True:
            h_or_l = input(f'\nIs your number (H)igher of (L)ower? ').lower()
            if h_or_l == 'h' or h_or_l == 'l':
                break
            else: print("\nI don't understand. (H) for higher and (L) for lower")
        if h_or_l == 'h':
            if my_guess == possible_guesses[upp]: print(lies)
            else:
                low = mid + 1
                counter += 1
        else:
            if my_guess == possible_guesses[low]: print(lies)
            else:
                upp = mid - 1
                counter += 1

if low == upp: counter -= 1
if counter == 1: print(f'\nYess!! and it only took me {counter} try')
else: print(f'\nYess!! and it only took me {counter} tries')

print('\nGame Over!!!')
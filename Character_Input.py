# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
name = input('Name: ')

while True:
    try:
        age = int(input('Age: '))
        break
    except ValueError:
        print('Please enter valid age')
while True:
    birthday_passed = input('Has your birthday already passed? (Y) Yes (N) No ').upper()
    if birthday_passed == 'Y' or birthday_passed == 'N':
        break
    else:
        print('Please enter valid answer')
if (birthday_passed == 'Y'):
    when_turn100 = 2020 + 100 - age
else:
    when_turn100 = 2020 + 99 - age
while True:
    try:
        number_of_messages = int(input('Number of messages: '))
        break
    except ValueError:
        print('Please enter valid number')

print(f'Hey {name} you will turn 100 years old in the year {when_turn100}\n' * number_of_messages)
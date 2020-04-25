# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
string = input('String: ')
string_list = []

for letter in string:
    string_list.append(letter)

string_list.reverse()

if ''.join(string_list) == string:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')


# Solution using string reversal:
string = input('String: ')
reversed_string = string[::-1]

if reversed_string == string:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')
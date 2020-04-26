# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random
import string
import time

def password_generator(length,uppercase,lowercase,digits,special,brackets):
    time_to_generate = time.time()
    characters = ''

    if uppercase == 'y': characters += string.ascii_uppercase
    if lowercase == 'y': characters += string.ascii_lowercase
    if digits == 'y': characters += string.digits
    if special == 'y': characters += string.punctuation
    if brackets == 'y': characters += '(){}<>[]'
    
    return ''.join(random.sample(characters, length)), str(time.time() - time_to_generate)


password_options = {}

print('\nPassword Generator')

while True:
    try:
        password_options['length'] = int(input('\nLength: '))
        assert password_options['length'] > 0
        break
    except: print('Invalid entry. You have not entered a positive integer.')

while True:
    password_options['uppercase'] = input('\nUppercase(A,B,C...)?\n(Y)es or (N)o: ').lower()
    if password_options['uppercase'] == 'y' or password_options['uppercase'] == 'n':
        break
    else: print('Invalid entry. You must enter "Y" for yes and "N" for no.\n')
        
while True:
    password_options['lowercase'] = input('\nLowercase(a,b,c...)?\n(Y)es or (N)o: ').lower()
    if password_options['lowercase'] == 'y' or password_options['lowercase'] == 'n':
        break
    else: print('Invalid entry. You must enter "Y" for yes and "N" for no.\n')

while True:
    password_options['digits'] = input('\nDigits(1,2,3...)?\n(Y)es or (N)o: ').lower()
    if password_options['digits'] == 'y' or password_options['digits'] == 'n':
        break
    else: print('Invalid entry. You must enter "Y" for yes and "N" for no.\n')

while True:
    password_options['special'] = input('\nSpecial(!,",#...)?\n(Y)es or (N)o: ').lower()
    if password_options['special'] == 'y' or password_options['special'] == 'n':
        break
    else: print('Invalid entry. You must enter "Y" for yes and "N" for no.\n')

while True:
    password_options['brackets'] = input('\nBrackets((),{},<>...)?\n(Y)es or (N)o: ').lower()
    if password_options['brackets'] == 'y' or password_options['brackets'] == 'n':
        break
    else: print('Invalid entry. You must enter "Y" for yes and "N" for no.\n')

passwrd, time_for_passwrd = password_generator(password_options['length'],password_options['uppercase'],
password_options['lowercase'],password_options['digits'],password_options['special'],
password_options['brackets'])

print('\nYour generated password:\n' + passwrd)

print('\nTime taken:\n' + time_for_passwrd)
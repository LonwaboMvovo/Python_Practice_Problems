# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
birthdays = {
    'DUA LIPA': '22/08/1995',
    'JOE ROGAN': '11/08/1967',
    'A-REECE': '27/03/1997',
    'WALTER O-BRIAN': '24/02/1977',
    'FELIKS ZEMDEGS': '20/12/1995'
}

print('\n>>> Welcome to the birthday dictionary. I know the birthdays of:\n')

for name in birthdays: print(name)

try:
    whos_bday = input("\n>>> Who's birthday do you want to look up?\n").upper()
    print(f"\n{whos_bday}'s birthday is {birthdays[whos_bday]}.")
except KeyError:
    print('\nI do not know the birthday of that person. I only know the birthdays of these people:\n')
    for name in birthdays: print(name)
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
def file_to_list(file_name):
    file_list = []
    with open(file_name, 'r') as f:
        for i in f:
            i = i.strip()
            file_list.append(i)
    return file_list


prime_numbers = file_to_list('primenumbers.txt')
happy_numbers = file_to_list('happynumbers.txt')

prime_and_happy_numbers = [num for num in prime_numbers if num in happy_numbers]

print(prime_and_happy_numbers)
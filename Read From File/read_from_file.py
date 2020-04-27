# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
names = {}

with open('nameslist.txt', 'r') as namesf:
    for line in namesf:
        line = line.strip()
        if line in names: names[line] += 1
        else: names[line] = 1

print(names)

pics = {}

with open('Training_01.txt', 'r') as picsf:
    for pic_line in picsf:
        pic_line = pic_line.strip().split('/')[1:]
        if pic_line[1] in pics:
            pics[pic_line[1]] += 1
        else:
            pics[pic_line[1]] = 1
print(pics)
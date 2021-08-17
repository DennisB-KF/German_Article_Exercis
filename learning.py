import random

Substantive = []

with open('woerter.csv') as file:
    line = file.readline()
    for line in file:
        line = line.strip('\n')
        (w,a) = line.split(',')
        Substantive.append((w,a))

random.shuffle(Substantive)

for i in Substantive:
    print(i[0])
    a = input('Enter Article: ')
    if a == i[1]:
        print('correct!\n******')
    else:
        Falsche.append((f'{i[0]},{i[1]}'))
        print(f'Wrong, the correct article is: {i[1]}')

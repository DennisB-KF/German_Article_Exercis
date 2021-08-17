import random

Subs = []

with open('woerter.csv') as file:
    line = file.readline()
    for line in file:
        line = line.strip('\n')
        (w,a) = line.split(',')
        Subs.append((w,a))

random.shuffle(Subs)

for i in Subs:
    print(i[0])
    a = input('Enter the article: ')
    if a == i[1]:
        print('Correct!\n******')
    else:
        print(f'Wrong, the correct article is: {i[1]}')

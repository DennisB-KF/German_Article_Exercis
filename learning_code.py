import random

Subs = []
count = 0

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
        count += 1
    else:
        print(f'Wrong, the correct article is: {i[1]}')

print(f"That is it! You've answered {int(count/len(Subs)*100)} percent correct.")

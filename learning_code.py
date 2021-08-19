import random

subs = []
wrongs = []
count = 0

with open('woerter.csv') as file:
    line = file.readline()
    for line in file:
        line = line.strip('\n')
        (w,a) = line.split(',')
        subs.append((w,a))

random.shuffle(subs)

for i in subs:
    print(i[0])
    a = input('Enter the article: ')
    if a == i[1]:
        print('Correct!\n******\n')
        count += 1
    else:
        wrongs.append(i)
        print(f'Wrong, the correct article is: {i[1]}\n')

print(f"That is it! Out of {len(subs)} you've answered {int(count/len(subs)*100)} percent correct.\n")
print('The wrong answers were:\n')
for i in wrongs:
    print(f'{i[1]}' + ' ' + f'{i[0]}\n')

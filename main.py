from random import randrange, choice
from string import ascii_lowercase

with open('text.txt', 'w', encoding='utf-8') as file:
    for _ in range(10):
        for _ in range(10):
            t = chr(ord('a') + randrange(26))
            file.write(t)
        file.write('\n')
print('file written successfully')

print()

with open('text.txt', 'r', encoding='utf-8') as file:
    print(file.read())

print()

with open('text.txt', 'r', encoding='utf-8') as file:
    t = file.read().replace(' ', '')
# l = input('write forbiden simbols\n').split()
l = []  # 'a b c d e f g h i j k'.split()
print(f'l: {l}')

for i in l:
    t = t.replace(i, ' ')

print(t)


def generate():
    global l, l2
    l = [list(line) for line in t.splitlines()]
    l2 = [[10 ** 9 for _ in range(len(l[0]))] for _ in range(len(l))]


generate()

print(*l2, sep='\n')


def f(x, y, value):
    global l2
    if l2[x][y] > value and l[x][y] == ' ':
        l2[x][y] = value
        if x > 0:
            f(x - 1, y, value + 1)
        if x < len(l2) - 1:
            f(x + 1, y, value + 1)
        if y > 0:
            f(x, y - 1, value + 1)
        if y < len(l2[0]) - 1:
            f(x, y + 1, value + 1)


def solve():  # solving l2
    global l2
    for i in range(len(l2)):
        for j in range(len(l2[0])):
            l2[i][j] = 10 ** 9

    for i in range(len(l[0])):
        if l[0][i] == ' ':
            f(0, i, value=0)
    if any([i != 10 ** 9 for i in l2[-1]]):
        return True
    return False


def show():
    print()
    for i in l2:
        for j in i:
            print(str(j).rjust(11), end=' ')
        print()


while not solve():
    c = choice(ascii_lowercase)
    t = t.replace(c, ' ')
    generate()
show()

print('-' * (len(l[0]) + 2))
for i in l:
    print(*(['|'] + i + ['|']), sep='', end='\n')
print('-' * (len(l[0]) + 2))


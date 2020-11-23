from random import randrange

d = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
n = 15
l = 1
u = 16

for i in d:
    while len(d[i]) != 5:
        t = randrange(l, u)
        if t not in d[i]:
            d[i].append(t)
    l += n
    u += n
    if i == 'N':
        d[i][2] = 'X'

print(' B I N G O')
for i in range(5):
    for j in 'BINGO':
        print('%2d ' % (d[j][i]), end='')
    print()



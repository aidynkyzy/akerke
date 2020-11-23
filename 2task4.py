from random import randrange

def simulate():
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    return dice1 + dice2

expected = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
simulated = {
    2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
    8: 0, 9: 0, 10: 0, 11: 0, 12: 0
}

for i in range(1000):
    s = simulate()
    simulated[s] += 1

for i in simulated.keys():
    print('%2d %.2f %.2f' % (i, simulated[i] / 1000 * 100, expected[i] * 100))



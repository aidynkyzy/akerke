d = {
    '1': ['.', ',', '?', '!', ';'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}
s = input().upper()
for i in s:
    for k, v in d.items():
        if i in v:
            for j in range(v.index(i) + 1):
                print(k, end='')
print()


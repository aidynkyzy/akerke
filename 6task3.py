s = input()

for char in s:
    lowerletters = 0
    upperletters = 0

    if "a" >= char >= "z":

        upperletters = upperletters + 1

    else:

        lowerletters = lowerletters + 1

if lowerletters >= upperletters:

    print(s.lower())
else:
    print(s.upper())
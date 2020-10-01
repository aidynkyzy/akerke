n, k = [int(i) for i in input().split()]
lst = []
pins = ["I"]*n
for i in range(k):
    c = [int(i) for i in input().split()]
    lst.append(c)
for j in range(0, k):
    for i in range(0, n):
        if i in range(lst[j][0]-1, lst[j][1]):
            pins[i] = "."

for elements in pins:
    print(elements, end="")  
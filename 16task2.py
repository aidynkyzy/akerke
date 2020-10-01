lst = []
sum = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        lst.append(n)

for i in range(1, len(lst) - 1):
    if (lst[i] > lst[i-1]) and (lst[i] > lst[i+1]):
        sum += 1

print(sum)
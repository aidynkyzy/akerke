n = int(input())

a = [0]*(n+1)

for i in range(1, n+1):
    a[i] = int(input())

a[0] = a[-1]
a.pop()
for i in a:
    print(i, end=' ')
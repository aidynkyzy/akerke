maxi = 0
sum = 0
lst = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if n > maxi:
            maxi = n
        lst.append(n)
for i in lst:
    if i == maxi:
        sum += 1
print(sum)
sum = 0
run = True
while run:
    n = int(input())
    if n == 0:
        run = False
    else:
        sum += n
print(sum)
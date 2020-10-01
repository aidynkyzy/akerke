def fibonacci(n):
    if n == 0:
        return 0
    # Second Fibonacci number is 1
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


a = int(input())
ind = -1
result = False
for i in range(2, a):
    b = fibonacci(i)
    if b == a:
        result = True
        ind = i
        break
    if b > a:
        result = False
        break
if result is True:
    print(ind)
else:
    print(ind)
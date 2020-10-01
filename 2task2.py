x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
difference_x = abs(x1 - x2)
difference_y = abs(y1 - y2)
if difference_x == 1 | difference_y == 1:
    print("YES")
else: print("NO")  
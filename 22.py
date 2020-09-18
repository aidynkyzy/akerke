import math
print("The lengths of the sides of a triangle:")
a , b , c = input().split()
a = int(a)
b = int(b)
c = int(c)
p = (a + b + c)/2
area = math.sqrt(p*((p - a)(p - b)(p - c)))
print("The area is %f" %area)
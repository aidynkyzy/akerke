print("The length of the base of the triangle:")
base = int(input())
print("The height of the triangle:")
height = int(input())
area = 0.5  * height * base
ans = "The area of the triangle is {} with the base length {} and height {}"
print(ans.format(area, base, height))
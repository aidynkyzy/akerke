print("The radius:")
radius = int(input())
print("The height:")
height = int(input())
volume = 3.14 * radius * radius * height
volume = round(volume, 1)
ans = "The volume is {}"
print(ans.format(volume))
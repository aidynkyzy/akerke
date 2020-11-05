s = str(input()) 

firststr = "aAeEiIuUyYoO"
secondstr = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ"

for i in s:
    if i in firststr:
        s = s.replace(i, ".")
for i in s:
    if i in secondstr:
        s = s.lower()
print(s)
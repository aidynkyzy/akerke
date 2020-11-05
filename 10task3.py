s = str(input())
s1 = ""
s2 = list(s.lower())

s2[0] = s2[0].upper()

for i in range(len(s)):
    s1 = s1[i]+s2[i]

print(s1)
s = input() 

s1 = " "
index = 0

for i in s:
    if i != s1[index]:
        s1 += i
        index += 1
        
s = s1.strip()

if len(s) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
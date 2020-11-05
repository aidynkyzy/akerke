s = input() 
strng = " " 
for i in s:
    s = s[::-1]
    if i in strng:
        s = s.replace(" ", "+")
print(s) 
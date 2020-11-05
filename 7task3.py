s = input()

lst = "abcdefghijklmnopqrstuvwxyz"
lst2="ABCDEFGHIJKLMNOPRSTUVWXYZ"

for i in lst:

    if i in s.lower():
        print("yes")
        
        
    else if i in s.upper():
        print("no")


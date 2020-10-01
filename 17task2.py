n=int(input())
cnt=0
lst=[]
for x in range(n):
    a=int(input())
    lst.append(a)

for i in range (len(lst)-1):    
    if lst[i-1]!=lst[i] :
        cnt+=1

print(cnt)
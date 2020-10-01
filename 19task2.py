n=int(input())
lst=[]

for i in range (n):
    a=int(input())
    lst.append(a)

def Pairs(lst, n):
    cnt = 0
    for i in range(0, n):
        for j in range(i+1, n) :   
            if lst[i] - lst[j] ==0  | lst[j] - lst[i] == 0:
                cnt += 1
    return cnt
 
n = len(lst)
print ( Pairs(lst, n))
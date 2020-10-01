N=int(input())
cnt=0
sqr=0
while cnt < N and sqr < N:
    cnt+=1
    sqr = cnt * cnt
    if sqr <= N:
        print(sqr)
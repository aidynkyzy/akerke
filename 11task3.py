n = int(input())
s = str(input())
cnt = 0
ans = 0

for i in range(n):
    if(s[i] == "x"):
        cnt+=1
        if(cnt > 2):
            ans+=1
    else: cnt=0

print(ans)
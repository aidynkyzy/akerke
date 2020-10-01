N=int(input())
M=int(input())
X=int(input())
Y=int(input())
size=N*M
if size > X and size > Y:
    print(min(X,Y))
else:
    print ("NO")
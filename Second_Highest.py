N = int(input())

for i in range(N):
    x,y,z=map(int,input().split())
    Second_Max = max(min(x,y),min(y,z),min(z,x))
    print(Second_Max)

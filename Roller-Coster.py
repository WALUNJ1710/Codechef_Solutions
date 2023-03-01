T = int(input())

for i in range(T):
    X,H = map(int,input().split())
    if X < H:
        print("No")
    else:
        print("Yes")
    

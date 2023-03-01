T = int(input())

for i in range(T):
    X,Y = map(int,input().split())
    if Y > X :
        print("No")
    else:
        print("Yes")

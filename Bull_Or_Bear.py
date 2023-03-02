t = int(input())

for i in range(t):
    x,y = map(int,input().split())
    if x > y:
        print("Loss")
    elif x == y:
        print("Neutral")
    else:
        print("Profit")

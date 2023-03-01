t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    price1 = 100-a
    price2 = 200-b
    if price1 < price2:
        print("FIRST")
    elif price2 < price1:
        print("SECOND")
    else:
        print("BOTH")

t = int(input())

for i in range(t):
    x,y = map(int,input().split())
    invest = max(0,x-y)
    print(invest)

t = int(input())

for i in range(t):
    x,y = map(int,input().split())
    Chair_req = x-y
    if Chair_req >= 0:
        print(Chair_req)
    else:
        print("0")
    

def can_divide_chocolates(n):
    if n % 2 == 0:
        return "Yes" 
    else:
        return "No"

t = int(input())

for i in range(t):
    n = int(input())
    
    print(can_divide_chocolates(n))

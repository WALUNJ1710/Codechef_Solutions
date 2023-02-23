def is_good_turn(x, y):
    sum = x + y
    if sum > 6:
        return "YES"
    else:
        return "NO"

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(is_good_turn(x, y))

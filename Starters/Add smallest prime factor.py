# cook your dish here
import math
 
# function to check if a number is prime
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True
 
# function to find the smallest prime factor of a number
def smallest_prime_factor(n):
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            return i
 
# main function to solve the problem
def solve(x, y):
    t = 0
    while x < y:
        x += smallest_prime_factor(x)
        t += 1
    return t
 
# main loop to read input and output answers
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(solve(x, y))

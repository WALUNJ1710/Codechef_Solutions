t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())
    perm = [i+1 for i in range(n)]  # start with the sorted permutation
    for i in range(0, n//2, 2):
        perm[i], perm[n-i-1] = perm[n-i-1], perm[i]  # swap pairs of elements
    for i in range(1, n, 2):
        perm[i], perm[i-1] = perm[i-1], perm[i]  # swap adjacent elements
    print(*perm)  # print the permutation separated by spaces

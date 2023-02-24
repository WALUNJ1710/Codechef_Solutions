# number of test cases
T = int(input())

for i in range(T):
    # total points and number of test cases passed
    X, N = map(int, input().split())

    # points per test case
    points_per_test_case = X // 10

    # Chef's score
    score = points_per_test_case * N

    # output the score
    print(score)

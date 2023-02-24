# Read the number of test cases
T = int(input())

# Loop over the test cases
for i in range(T):
    # Read the value of X and Y
    X, Y = map(int, input().split())

    # Calculate the target score
    A = X - 1

    # Calculate how many more runs Team B needs to score
    runs_needed = X - Y

    # Print the result
    print(runs_needed)

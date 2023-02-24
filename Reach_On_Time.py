# Read the number of test cases
T = int(input())

# Loop over the test cases
for i in range(T):
    # Read the value of X
    X = int(input())

    # Check if Chef will reach on time
    if X >= 30:
        print("YES")
    else:
        print("NO")

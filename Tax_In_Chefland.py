# Taking input for the number of test cases
T = int(input())

# Iterating over each test case
for i in range(T):
    # Taking input for the total income
    X = int(input())
    
    # Checking if the total income is greater than 100
    if X > 100:
        # Deducting the tax of 10 rupees and printing the remaining amount
        print(X - 10)
    else:
        # Printing the total income as it is
        print(X)

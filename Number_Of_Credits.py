# Function to calculate the total number of credits for a test case
def calculateCredits(X, Y, Z):
    totalCredits = 4*X + 2*Y  # Calculate the total number of credits
    return totalCredits

# Main function
if __name__ == '__main__':
    T = int(input())   # Read the number of test cases
    
    # Repeat for each test case
    for i in range(T):
        X, Y, Z = map(int, input().split())  # Read the number of RTP, Audit and Non-RTP courses
        totalCredits = calculateCredits(X, Y, Z)  # Calculate the total number of credits
        print(totalCredits)  # Print the total number of credits

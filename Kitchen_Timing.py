# Read the number of test cases
T = int(input())

# Loop through T test cases
for i in range(T):
    # Read the starting and ending time of working hours
    X, Y = map(int, input().split())
    
    # Calculate the difference between the ending and starting time
    hours_worked = Y - X
    
    # Print the difference as the number of hours Chef works
    print(hours_worked)

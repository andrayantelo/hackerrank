# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array A[] of n
# integers each separated by a space.

# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100

# Output format
# Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # remove all instances of the max and then find max again
    
    arr = filter( lambda a: a != max(arr), arr)
    
    runner_up = max(arr)
    
    print(runner_up)

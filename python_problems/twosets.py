# You are given two sets, a and b.
# Your job is to find whether set a is a subset of set b.

# If set a is a subset of set b, print True.
# If set a is not a subset of set b, print False.

# Input Format
# The first line will contain the number of test cases, t.
# The first line of each test case contains the number of elements in set a.
# The second line of each test case contains the space separated elements of set a.
# The third line of each test case contains the number of elements in set b.
# The fourth line of each test case contains the space separated elements of set b.

# Constraints
# 0 < t < 21
# 0 < Number of elements in each set < 1001

# Output Format
# Output True or False for each test case on separate lines.

if __name__ == "__main__":
    t = int(input())
    
    for test in range(t):
        a_len = int(input())
        a = set([int(i) for i in input().split()])
        b_len = int(input())
        b = set([int(i) for i in input().split()])
        
        print(a.issubset(b))

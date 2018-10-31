# Task
# You are given a set a and n number of other sets. These n number of sets
# have to perform some specific mutation operations on set a.

# Your task is to execute those operations and print the sum of elements from set a.

# Input Format
# The first line contains the number of elements in set a.
# The second line contains the space separated list of elements in set a.
# The third line contains integer n, the number of other sets.
# The next 2*n lines are divided into n parts containing two lines each.
# The first line of each part contains the space separated entries of
# the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.
# 0 < len(set(a)) < 1000
# 0 < len(otherSets) < 100
# 0 < n < 100

# Output Format
# Output the sum of elements in set A

if __name__ == "__main__":
    a_size = int(input())
    a = set(map(int, input().split()))
    parts = int(input())
    
    for part in range(parts):
        command = input().rsplit(None, 1)
        n = set(map(int, input().split()))
        getattr(a, command[0])(n)
    
    print(sum(a))
 

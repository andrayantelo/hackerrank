# You are given a set a and n other sets. 
# Your job is to find whether set a is a strict superset of each of the n sets.

# Print True, if a is a strict superset of each of the n sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Input Format
# The first line contains the space separated elements of set a. 
# The second line contains integer n, the number of other sets. 
# The next n lines contains the space separated elements of the other sets.

# Constraints 
# 0 < len(set(a)) < 501
# 0 < n < 21
# 0 < len(otherSets) < 101

# Output Format
# Print True if set a is a strict superset of all other n sets. Otherwise, print False.

if __name__ == "__main__":
    a = set([int(i) for i in input().split()])
    num_other_sets = int(input())
    sum_bool = True
    
    
    for n in range(num_other_sets):
        n = set([int(i) for i in input().split()])
        if not a.issuperset(n):
            sum_bool = False
        
    print(sum_bool)

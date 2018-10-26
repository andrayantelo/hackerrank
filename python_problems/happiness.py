# There is an array of n integers. There are also 2 disjoint sets, a and b
# each contains m integers. You like all the integers in set a and dislike
# all the integers in set b. Your initial happiness is 0. For each i
# integer in the array, if i is an element of A, you add 1 to your 
# happiness. If i is an element of B, you add -1 to your happiness.
# Otherwise, your happiness does not change. Output your final happiness
# at the end.

# Note: Since a and b are sets, they have no repeated elements. However,
# the array might contain duplicate elements.

# Constraints
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# 1 <= Any integer in the input <= 10^9

# Input Format
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, a and b, respectively.

# Output Format
# Output a single integer, your total happiness.

if __name__ == '__main__':
    sizes = input().split()
    n, m = sizes[0], sizes[1]
    
    line = map(int, input().split())
    
    a, b = set(map(int, input().split())), set(map(int, input().split()))
    
    #happiness = 0
    
    #for i in line:
    #    if i in a:
    #        happiness += 1
    #    elif i in b:
    #        happiness -= 1
    #print(happiness)
    
    
    #Better solution found online:
    happiness = sum([(i in a) - (i in b) for i in line])
    print(happiness)

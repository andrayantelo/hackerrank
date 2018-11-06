# Consider the following:

# A string, s, of length n where s = c0c1...c(n-1).
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, ti, consists of a
# contiguous block of k characters in s. Then, use each ti to create string ui such that:

# The characters in ui are a subsequence of the characters in ti.
# Any repeat occurrence of a character is removed from the string such that
# each character in ui occurs exactly once. In other words, if the character
# at some index j in ti occurs at a previous index < j in ti, then do not include
# the character in string ui.
# Given s and k, print n/k lines where each line i denotes string ui.

# Input Format
# The first line contains a single string denoting s.
# The second line contains an integer, k, denoting the length of each subsegment

# Constraints
# 1 <= n <= 10^4, where n is the length of s
# 1 <= k <= n
# It is guaranteed that n is a multiple of k

# Output Format
# Print n/k lines where each line i contains string ui.

def merge_the_tools(string, k):
     n = len(string)










if __name__ == '__main__':
    a = input()
    k = int(input())
    
    print(a)
    print(k)

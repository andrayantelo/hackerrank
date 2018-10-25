# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d .

# Input Format

# The first line contains an integer n , the number of operations. 
# The next n lines contains the space separated names of methods and their values.

# Constraints
# 0 <= n <= 100

# Output Format

# Print the space separated elements of deque d.

from collections import deque
import sys

n = input()

f = open('input.txt' ,'r')

d = deque()

for line in f:
    instruction = line.rsplit(None, 1)
    if len(instruction) > 1:
        dfunc = instruction[0]
        value = int(instruction[1])
        getattr(d, dfunc)(value)
    else:
        dfunc = instruction[0]
        getattr(d, dfunc)()
	
for e in d:
	print(e, end=" ")
	
	

from collections import namedtuple
import sys

#ID, MARKS, CLASS and NAME

n = int(input())
cols = input()
Student = namedtuple('Student', cols)
# example: s = Student('Student', 'ID MARKS CLASS NAME')

for line in sys.stdin:
  value_list = line.split()
  print(value_list)
  #value_list is an array like so: ['ana', '15', '1', '98']
  

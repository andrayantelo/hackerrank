from collections import namedtuple
import sys

#ID, MARKS, CLASS and NAME

n, Student, sum_marks = int(input()), namedtuple('Student', input()), 0
#n = 5
#Student = namedtuple('Student', 'MARKS CLASS NAME ID')
#sum_marks = 0
#i = 0

#inf = open("input.txt", "r")
#Student._make(line.split())
#doc = inf.readlines()


print(sum([int(Student._make(line.split()).MARKS) for line in sys.stdin])/n)

#print(sum([int(Student._make(line.split()).MARKS) for line in doc)\n)



#for line in sys.stdin:
#  s = Student._make(line.split())
#  sum_marks += int(s.MARKS)	
  
  
#  i+= 1
#  if i == 5:
#	  break

#print(sum_marks/n)
  

#You are the manager of a supermarket. 
#You have a list of  items together with their prices that consumers bought on a particular day. 
#Your task is to print each item_name and net_price in order of its first occurrence.

#item_name = Name of the item. 
#net_price = Quantity of the item sold multiplied by the price of each item.

#Input Format

#The first line contains the number of items, N . 
#The next N lines contains the item's name and price, separated by a space.

#Constraints
#0< N <= 100

#Output Format

#Print the item_name and net_price in order of its first occurrence.

from collections import OrderedDict
import re

n = input()
groceries = OrderedDict()

f = open('input.txt', 'r')

for line in f:
	#setdefault dict method to set default value to 0 so that we can do += price TODO TODO
    item = line.split()
    price = int(item.pop())
    groceries[" ".join(item)] = price
    #print(list)
    #print(price)
print(groceries)   
    #price = int(line.split().pop())
    #print(line)
    #print(price)
	#groceries[s[0]] = int(s[1])

#print groceries

# you'll have something like this: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
# OrderedDict([('banana fries', 12), ('potato chips', 30), ('apple juice', 10), ('candy', 5)])

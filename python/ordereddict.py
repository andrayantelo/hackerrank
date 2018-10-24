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

n = input()
groceries = OrderedDict()

f = open('input.txt', 'r')

for line in f:
	item = line.rsplit(None, 1)
	unit = item[0]
	price = int(item[1])
	
	if unit in groceries:
	  groceries[unit] += price 
	else:
	  groceries[unit] = price
	
	 
for key in groceries:
	print(key, end=" ")
	print(groceries[key])		
	  

#def parse_input(string):
#	"""returns tuple of item name and data"""
#	item = string.split()
#	price = int(item.pop())
#	item = " ".join(item)
#	return (item, price)
	
#def make_odict(text_file):
#	f = open(text_file, 'r')
#	groceries = OrderedDict()
#	for line in f:
#	    item, price = parse_input(line)
#	    groceries.setdefault(item, 0)
#	    groceries[item] += price
    
#def print_groceries(groc_dict):	
#	for key in groceries:
#		print(key, end=" ")
#		print(groceries[key])
   
   

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#all me, again!
from itertools import dropwhile, count
import time

def has_same_digits(start_num, max_multiplier):
	digits = str(start_num)
	for x in range(2, max_multiplier+1):
		temp = str(start_num*x)
		for d in digits:
			temp = temp.replace(d, '', 1)
		if temp != "":
			return False
	return True
			
#print(has_same_digits(125874, 2))			
start_time = time.time()

print(next(dropwhile(lambda x: not has_same_digits(x, 6), count(100))))

end_time = time.time()

print("Completed in %s seconds" % (end_time - start_time))
#142857
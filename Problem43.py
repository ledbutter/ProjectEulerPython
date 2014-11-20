# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

def is_divisible(divisor, dividend):
	if divisor % dividend == 0:
		return True
	else:
		return False

def has_specialproperties(x):
	digits = str(x)
	if is_divisible(int(digits[1:4]), 2) and is_divisible(int(digits[2:5]), 3) and \
		is_divisible(int(digits[3:6]), 5) and is_divisible(int(digits[4:7]), 7) and \
		is_divisible(int(digits[5:8]), 11) and is_divisible(int(digits[6:9]), 13) and \
		is_divisible(int(digits[7:10]), 17):
		return True
	else:
		return False
	
#stolen and modified from problem 41 	
def gen_pandigitals():
	#grab all the ten-digit pandigitals
	perms = permutations(range(9, -1, -1), 10)
	for p in perms:
		yield int(''.join(str(d) for d in p))
	
#my own, more pythonic version of this (pretty impressive, huh?)
print(sum(filter(lambda x: has_specialproperties(x), gen_pandigitals())))
#16695334890	
	
# total = 0		
		
# for x in gen_pandigitals():
	# if has_specialproperties(x):		
		# total += x
			
# print(total)
#16695334890
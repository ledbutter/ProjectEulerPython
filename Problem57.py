# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

 # 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

from itertools import starmap
from math import log10

def expansions(n):
	num, den = 2, 1						# r = 2
	for _ in range(n):
		yield num + den, num			# 1 + 1/r
		num, den = 2 * num + den, num	# r = 2 + 1/r

def ndig(n):
	return int(log10(n)+1)
	
print(sum(starmap(lambda num, den: ndig(num) > ndig(den), expansions(1000))))	

	
## my way, dog slow
# from fractions import Fraction

# def CalculateOther(iteration):
	# # need to start from inside and move out
	# # to do that we need to ....
	# if iteration == 1:
		# return Fraction(1, 2)
	# else:
		# start = Fraction(2) + Fraction(1, 2)
		# result = Fraction(1, start)
		# for i in range(iteration-2):
			# result = Fraction(1, 2 + result)
		# return result
	
	# # this violates python's limits for recursion	
	# # if iteration == 1:
		# # return Fraction(1, 2)
	# # else:
		# # return Fraction(1, Fraction(2, 1) + CalculateOther(iteration-1))
	
# def fraction_sum(iteration):
	# start = Fraction(1,1)
	# other = CalculateOther(iteration)
	# res = start + other
	# return res
	
# def num_greater_denom(f):
	# if len(str(f.numerator)) > len(str(f.denominator)):
		# return True
	# else:
		# return False
				
# fractions = map(fraction_sum, range(1,1001))

# print(len(list(filter(num_greater_denom, fractions))))	
# #153
		
	
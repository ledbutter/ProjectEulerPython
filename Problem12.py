# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

 # 1: 1
 # 3: 1,3
 # 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
# 76576500

# my method
from Utils import triangle_numbers, factorCount

factor_count = 0
target = 0
max_count = 0

for x in triangle_numbers(15000):
	factor_count = factorCount(x)
	
	if factor_count > max_count:
		max_count = factor_count
	if factor_count > 500:
		target = x
		break
		
print(target)
print(max_count)

# adopted from C++ solution
# from math import sqrt

# divisors = 0
# n = 0
# triangle = 0
# limit = 0

# while True:
	# divisors = 0
	# n = n+1
	# triangle = (n*(n+1))//2
	
	# limit = int(sqrt(triangle))
	
	# for x in range(1, limit):
		# if triangle % x == 0:
			# divisors += 1
	# # multiply by two to account for those divisors above the square root
	# divisors *= 2
	
	# if divisors > 500:
		# break
		
# print(triangle)

## another euler solution
# from math import sqrt
# def tri(n):
	# return ((n+1)*(n)/2)
	
# for i in range(7, 1000000):
	# l = []
	# l.append(1)
	# l.append(tri(i))
	# for j in range(2, int(sqrt(tri(i)))+1):
		# if (not tri(i)%j):
			# l.append(j)
			# l.append(tri(i)/j)
	# if len(l) > 500:
		# print(i)
		# print(tri(i))
		# break
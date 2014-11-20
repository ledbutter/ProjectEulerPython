# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.

# Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

Limit = 1000000
factors=[0]*Limit # number of prime factors
count = 0
number_count = 4

for i in range(2, Limit):
	if factors[i] == 0:
		# i is prime (hasn't been visited before)
		count = 0
		val = i
		while val < Limit:
			#increment all multiples of i
			factors[val] += 1
			val += i
	elif factors[i] == number_count:
		#we've found a number that has the desired number of prime factors...
		count += 1
		#...is it the fourth such number in a row???
		if count == number_count:
			print(i-(number_count-1)) # print the first number in the sequence
			break
	else:
		count = 0
		
# from Utils import prime_factor_list, is_prime
# from itertools import dropwhile

# def is_not_magic(first_num, num_count):
	# for offset in range(0, num_count):
		# if len(prime_factor_list(first_num+offset)) != num_count:
			# return True
	# return False
	
# print("Answer: ", next(dropwhile(lambda x: is_not_magic(x, 4), range(2*3*5*7,1000000))))
#134043
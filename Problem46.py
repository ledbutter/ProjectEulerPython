# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2x1^2
# 15 = 7 + 2x2^2
# 21 = 3 + 2x3^2
# 25 = 7 + 2x3^2
# 27 = 19 + 2x2^2
# 33 = 31 + 2x1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#here's a more pythony way of doing things
from itertools import count, dropwhile
from Utils import is_prime

def twice_squares(limit):
	for i in range(limit):
		yield 2*(i**2)

def not_right(num):
	for n in twice_squares(num):
		prime = num - n
		if is_prime(prime):
			return True
	return False

composite_odds = filter(lambda x: not is_prime(x), count(35, 2))
print(next(dropwhile(not_right, composite_odds)))
#5777

#mine: works fairly fast
# from itertools import count, takewhile
# from Utils import is_prime, primes_sieve

# #first come up with iterator to generate all odd composite numbers
# composite_odds = filter(lambda x: not is_prime(x), count(35, 2))

# # i = 0
# # for c in composite_odds:
	# # print(c)
	# # i += 1
	# # if i == 10:
		# # break
	
# #generate the twice squared values
# # def twice_squares(limit):
	# # for i in range(limit):
		# # yield 2*(i**2)
		
# twice_squares = list(2*(n**2) for n in range(1, 100))
# primes = list(primes_sieve(10000))
		
# def find_answer():
	# for c in composite_odds:
		# found_combo = False
		# #find all primes smaller than c
		# for p in primes:#primes_sieve(c):
			# for t in twice_squares:#twice_squares((c-p)//2):
				# if p + t == c:
					# #print("Composite odd %i can be expressed as %i and %i" % (c, p, t))
					# found_combo = True
				# if found_combo == True:
					# break
			# if found_combo == True:
				# break
		# if found_combo == False:
			# return c

# print(find_answer())
#5777




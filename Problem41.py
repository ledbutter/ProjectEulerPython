# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations, dropwhile
from Utils import is_prime
from functools import reduce

def gen_pandigitals():
	#start with nine digits and work our way down
	for x in range(9,2,-1):
		perms = permutations(range(x, 0, -1), x)
		for p in perms:
			yield int(''.join(str(d) for d in p))
			
			#my original long-winded way
			# temp = ""
			# for d in p:
				# temp += str(d)
			# yield int(temp)
		
	
prime_check = lambda i: not is_prime(i)	

print(list(dropwhile(lambda x: prime_check(x), gen_pandigitals()))[0])		
		
# for n in gen_pandigitals():
	# if n % 2 != 0:
		# if is_prime(n):
			# print(n)
			# break
		
#7652413
	
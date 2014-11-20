# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from Utils import primes_sieve, is_prime

upper_range = 1000000

circular_count = 0

#use set for much better performance
primes_seen = set()

for p in primes_sieve(upper_range):
	if p not in primes_seen:
		primes_seen.add(p)
	p_digits = str(p)
	if len(p_digits) > 1:
		is_circular = True
		for i in range(1, len(p_digits)):
			possible = int(p_digits[i:]+p_digits[:i])
			if possible in primes_seen:
				continue
			elif not is_prime(possible):
				is_circular = False
				break
			else:
				primes_seen.add(possible)
		if is_circular:
			#print(p)
			circular_count += 1
	else:
		#print(p)
		circular_count += 1
	
print(circular_count)
#55
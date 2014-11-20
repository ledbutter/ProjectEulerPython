# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove 
# 	digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work 
#	from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from Utils import primes_sieve, is_prime

candidates = filter(lambda x: x > 7, primes_sieve(1000000))

prime_set = set()

count = total = 0

for n in candidates:
	if n not in prime_set:
		prime_set.add(n)
		
	digits = str(n)
	i = 1
	while i < len(digits):
		if not is_prime(int(digits[i:])):
			break
		i += 1
			
	if i == len(digits):
		i = len(digits) - 1
		while i > 0:
			if not is_prime(int(digits[0:i])):
				break
			i -= 1
		
	if i == 0:
		#print(n)
		count += 1
		total += n
	
	if count == 11:
		break

print(total)
#748317
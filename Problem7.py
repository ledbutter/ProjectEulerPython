#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#104743

import Primes

i = 0
target = 0

for x in Primes.primes_sieve(1000000):
	i += 1
	if i == 10001:
		target = x
		break
		
print(target)
	

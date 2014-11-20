# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

#this works, but i had to do a lot of guess work on the limit
from Utils import primes_sieve, is_prime

limit = 3967

primes = list(primes_sieve(limit))

index = 1
max_prime = 0
max_index = 0

max = len(primes)-1

#print(max)

for i in range(max):
	index = 1
	sum = primes[i]
	while index + i < max:
		#print("i is %i and index is %i" % (i, index))
		sum += primes[i + index]
		if is_prime(sum):
			if max_index < index:
				max_index = index
				max_prime = sum
		index += 1
		
print("Max value %i with sequence length of %i" % (max_prime, max_index+1))
#997651

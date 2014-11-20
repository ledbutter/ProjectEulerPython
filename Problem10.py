# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from Utils import primes_sieve

print(sum(primes_sieve(2000000)))

#142913828922
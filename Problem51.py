# By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, 
# are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven 
# primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.

#all me, got lucky that the max same_digit_count produced the correct result, should really return a list of all
#digits that occur at least once
from Utils import is_prime, primes_sieve
from itertools import dropwhile
import string

def same_digit_count(n):
	digits = str(n)
	result = (0,0)
	count = 0
	
	for d in string.digits:
		count = digits.count(d)
		if count > result[1]:
			result = int(d), count
	return result
	
def prime_family(n, replace_digit):
	result = [n]
	str_digit = str(replace_digit)
	str_n = str(n)
	other_digits = string.digits.replace(str_digit,'')
	for d in other_digits:
		temp = int(str_n.replace(str_digit, d))
		if len(str(temp)) == len(str_n):
			if is_prime(temp):
				result.append(temp)
	result.sort()
	return result

#only deal with primes greater than the last one in the example sequence
primes = dropwhile(lambda x: x < 56993, primes_sieve(1000000))

for p in primes:
	digit, same_count = same_digit_count(p)
	if same_count > 0:
		res = prime_family(p, digit) 
		if len(res) == 8:
			print(res[0])
			break
#121313
	

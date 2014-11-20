from math import sqrt, ceil, fabs
import random


def is_pandigital(digits, lower=1, length=9):
	to_remove = list(range(lower,10))
	if len(digits) == length and digits.isdigit():
		for d in digits:
			val = int(d)
			if val in to_remove:
				to_remove.remove(val)
			else:
				return False
		if len(to_remove) == 0:
			return True
		else:
			return False
	else:
		return False

def fibonacciSequence():
	firstVal = 0
	secondVal = 1
	currentVal = 0
	
	while True:
		currentVal = firstVal + secondVal
		firstVal = secondVal
		secondVal = currentVal
		yield currentVal
	
def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(sqrt(n))
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

def primes_sieve(limit):
	'''Produces the prime numbers up to limit represented by limit'''
	a = [True] * (limit)
	a[0] = a[1] = False
	
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, limit, i):
				a[n] = False
	
def trial_division(n, bound=None):
	if n == 1:
		return 1
	for p in [2, 3, 5]:
		if n%p == 0:
			return p
	if bound == None:
		bound = n
	diff = [6, 4, 2, 4, 2, 4, 6, 2]
	m = 7
	i = 1
	while m <= bound and m*m <= n:
		if n%m == 0:
			return m
		m += diff[i%8]
		i += 1
	return n
	
def prime_factor_list(n):
	'''retrieves prime factors of a number'''
	if n in [-1, 0, 1]: return []
	if n < 0: 
		n = -n
	F = []
	while n != 1:
		p = trial_division(n)
		e = 1
		n //= p
		while n%p == 0:
			e += 1; n //= p
		F.append((p,e))
	F.sort()
	return F

def factors(n):
	'''Produces all of the factors of n'''
	yield 1
	i = 2
	limit = n**0.5
	while i <= limit:
		if n % i == 0:
			yield i
			n = n//i
			limit = n**0.5
		else:
			i += 1
	if n > 1:
		yield n
	
	# limit = ceil(sqrt(n))
	# for i in range(1, limit):
		# if n % i == 0:
			# yield i
	# # include the number itself
	# yield n
	
def factor_Pairs(n):
	limit = ceil(sqrt(n))
	for i in range(1, limit):
		if n % i == 0:
			yield (i, n//i)
	
def factorCount(n):
	'''Returns the number of factors of n, including n itself in that count'''
	limit = ceil(sqrt(n))
	num = 1 # 1 for n itself
	for i in range(1, limit):
		if n % i == 0:
			num += 1
	#need to multiply by 2 to account for those divisors greater than sqrt of n
	return num*2
	
def sumFactors(n):
	sum = 1
	t = sqrt(n)
	for i in range(2, int(t)+1):
		if n % i == 0:
			sum += i + n//i
	if t == int(t):
		sum -= t
	return sum
	
def triangle_numbers(limit):
	'''Produces the first X triangle_numbers with X being represented by limit'''
	triangle = 0
	n = 1
	while n < limit:
		triangle = int((n*(n+1))//2)
		yield triangle
		n += 1
	# yield 1
	# sum = 1
	# i = 2
	# while i < limit:
		# sum += i
		# i += 1
		# yield sum
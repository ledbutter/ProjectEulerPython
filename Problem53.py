# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# nCr =	
# n!
# r!(nr)!
# ,where r  n, n! = n(n1)...321, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
from math import factorial

min_val = 1000000
combos = lambda n, r: factorial(n)//(factorial(r)*factorial(n-r))
		
num = 0
for n in range(23, 101):
	for r in range(0, n+1):
		if combos(n, r) > min_val:
			num += 1

print(num)
#4075


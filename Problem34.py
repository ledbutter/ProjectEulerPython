# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
from math import factorial

tot = 0

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

upper_range = factorial(9) * 7

for n in range(3, upper_range):
	if n == sum(f[int(d)] for d in str(n)):
		print(n)
		tot += n

print(tot)
#40730
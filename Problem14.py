# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
# 837799

def sequenceLength(n):
	
	seqLength = 1
	while n > 1:
		seqLength += 1
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1
	return seqLength
	
#print(max((sequenceLength(n), n) for n in range(999999, 100000, -2)))

#or...
maxLength = seqLength = maxVal = 1
for x in range(999999, 3, -2):
	seqLength = 1
	n = x
	while n > 1:
		seqLength += 1
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n + 1
	if maxLength < seqLength:
		maxLength = seqLength
		maxVal = x
	
print(maxLength, maxVal)
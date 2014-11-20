# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
#	(i) each of the three terms are prime, and, 
#	(ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from Utils import is_prime

def number_perms(src_num):
	perms = []
	str_num = str(src_num)
	
	if len(str_num) == 1:
		perms = [int(str_num)]
	else:
		for i, c in enumerate(str_num):
			for perm in number_perms(int(str_num[:i] + str_num[i+1:])):
				perms.append(int(c + str(perm)))
		
	return perms

#start with the next odd number than the one listed in the example
n = 1489

while n < 9999:
	b = n + 3330
	c = n + 6660
	
	if is_prime(n) and is_prime(b) and is_prime(c):
		#now check for the permutations
		perms = number_perms(n)
		
		if b in perms and c in perms:
			print("%i %i %i" % (n, b,c))
			break
	n += 2
#2969 6299 9629
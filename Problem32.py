# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# 	for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and 
# 	product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# 	pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from Utils import factor_Pairs, is_pandigital

#this ugly code is actually mine and it works!

# i know this range is way too big, but it should work
total = []

#print(vals)

for i in range(100, 10000):
	sum = str(i)
	pairs = factor_Pairs(i)
	for p in pairs:
		unique = 0
		all_digits = str(p[0]) + str(p[1]) + sum
		if is_pandigital(all_digits):
			total.append((i,p[0], p[1]))
			break
				
#print(total)
sum = 0
for pd in total:
	sum += pd[0]
print(sum)

# http://blog.dreamshire.com/2009/04/22/project-euler-problem-32-solution/
# def is_pandigital2(n, s=9): 
	# n=str(n)
	# return len(n)==s and not '1234567890'[:s].strip(n)
	
# p = set()
# for i in range(2,100):
	# start = 1234
	# if i>9:
		# start = 123
	# for j in range(start, 10000//i+1):
		# if is_pandigital2(str(i)+str(j)+str(i*j)):
			# #print(i,j,i*j)
			# p.add(i*j)
		
#print(sum(p))
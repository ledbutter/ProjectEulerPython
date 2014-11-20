# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#from itertools import filterfalse, takewhile
from Utils import sumFactors

def is_abundant(n):
	factorSum = sumFactors(n)
	if factorSum > n:
		return True
	else:
		return False

limit = 28123
	
abundants = set(filter(lambda x: is_abundant(x), range(11, limit)))

non_append_sums = 0

for n in range(1, limit):
	if not any((n-a in abundants) for a in abundants):
		non_append_sums += n

print(non_append_sums)
#4179871


#not 1,973,502 or 395,465,626

# abundants = list(filter(lambda x: is_abundant(x), range(1, limit)))

# possible_sums = []
# for i in range(len(abundants)):
	# for j in range(i, len(abundants)):
		# possible_sums.append(abundants[i]+abundants[j])

		
# possible_sums.sort()
# current = possible_sums[0]
# final_sums = []
# i = 0
# while current < limit:
	# final_sums.append(current)
	# i += 1
	# current = possible_sums[i]
# #final_sums = takewhile(lambda x: x < limit, possible_sums)		

# non_append_sums = 0	
# for i in range(1, limit):
	# if i not in final_sums:
		# non_append_sums += i
		
# print(non_append_sums)

# # current = 0

# for i in range(len(abundants)):
	# for j in range(i, len(abundants)):
		# possible_sums.append(abundants[i]+abundants[j])
		
# final_sums = takewhile(lambda x: x < 28135, possible_sums)
		
# # now have all possible sums
# nums = list(filterfalse(lambda x: x in final_sums, range(1, limit)))

# non_append_sums = 0
# for i in nums:
	# non_append_sums += i

# print(non_append_sums)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#solution from stackoverflow:
# def d(n):
	# sum = 1
	# t = sqrt(n)
	# for i in range(2, int(t)+1):
		# if n % i == 0:
			# sum += i + n//i
	# if t == int(t):
		# sum -= t
	# return sum
	
# limit = 20162
# sum = 0

# abn = set()
# for n in range(1, limit):
	# if is_abundant(n):#if d(n) > n:
		# abn.add(n)
	# if not any((n-a in abn) for a in abn):
		# sum += n
		
# print(sum)
#4179871
	
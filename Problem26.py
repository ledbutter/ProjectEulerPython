# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from itertools import count

def recur_len(n):
	# digits for unit fraction 1/n
	r = 10 # initial remainder (10/n)/10
	seen = {}
	for i in count(0):
		#print("i = %i and r = %r" % (i, r))
		if r == 0:
			return 0 #divides evenly
		elif r in seen:
			return i-seen[r] # curpos - firstpos
		seen[r] = i
		r = 10*(r % n)
		
#recur_len(7)
	
len, i = max((recur_len(i),i) for i in range(2,1000))
print(i)

# my slow way:
# from decimal import *

# d = max = temp = length = 1
# stringTemp = ""

# divisor = Decimal(1)
# getcontext().prec = 10000

# while d < 1000:
	# temp = divisor/Decimal(d)
	# # take only the remainder
	# stringTemp = str(temp)[2:]
	# strLen = len(stringTemp)
	# if strLen > 6:
		# #if stringTemp[0] != stringTemp[1] and stringTemp[1] != stringTemp[2]:
		# i = 2
		# while stringTemp[:i] != stringTemp[i:i+i]:
			# #print(stringTemp[:i], stringTemp[i:i+i])
			# i += 1
			# if i == strLen:
				# break
		# if stringTemp[:i] == stringTemp[i:i+i]:
			# #print("%d has this sequence: %s" % (d, stringTemp[:i]))
			# if i > length:
				# length = i
				# max = d
			# #print("%i has length %i" % (d, len(stringTemp)))
			
	# d += 1
# print(max, length)
#983
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the 
#	concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 
#	918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an
#	integer with (1,2, ... , n) where n > 1?

from Utils import is_pandigital


#this uncommented implementation comes from the discussion forum
from itertools import count

def gen_pandigital(seed):
   digits = str(seed)
   for i in count(2):
      ndig = len(digits)
      if ndig < 9: digits += str(seed * i)
      elif ndig == 9 and set(digits) == set('123456789'):
         return int(digits)
      else: return False

print(max(map(gen_pandigital, range(1,10000))))

# max_range = 2
# max_pan = 0
# max_r = range(1,2)
# max_n = 0

# while max_range < 10:
	# r = range(1,max_range)
	# for i in range(1, 10000):
		# products = []
		# for m in r:
			# products.append(i*m)
		# concat = ""
		# for p in products:
			# concat += str(p)
		# if is_pandigital(concat):
			# temp = int(concat)
			# if temp > max_pan:
				# #print(temp)
				# max_r = r
				# max_n = i
				# max_pan = temp
	# max_range += 1
# print(max_pan, max_r, max_n)
#932718654 range(1, 3) 9327
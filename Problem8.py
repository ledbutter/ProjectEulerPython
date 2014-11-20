# Find the greatest product of five consecutive digits in the 1000-digit number.
# 40824

from string import whitespace
from operator import mul
from functools import reduce
#from itertools import product, islice

txt = open("Problem8Input.txt")

inputs = [int(c) for line in txt for c in line if c not in whitespace]
print(max([reduce(mul, inputs[i:i+5]) for i in range(len(inputs) -5)]))

# inputString = txt.read()

# txt.close()

# inputs = []

# for s in inputString:
	# inputs.append(int(s))

# index = maxVal = 0

# temp = 1

# for i in inputs:
	# if index + 4 > len(inputs):
		# break
	# current = islice(inputs, index, index+5)
	# for c in current:
		# temp *= c
	# if temp > maxVal:
		# maxVal = temp
	# temp = 1
	# index += 1

# print(maxVal)


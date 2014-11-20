# The nth term of the sequence of triangle numbers is given by, tn = .5n(n+1); so the first ten triangle 
# numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these
# values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word 
# value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand 
# common English words, how many are triangle words?

import string
from itertools import count, islice

f = open("words.txt")

words = f.readline().split(",")

f.close()

#old school way that works very well:
def triangle_numbers(limit):
	nums = set()
	for i in range(1, limit):
		nums.add(int(.5*i*(i+1)))
	return nums

#get the values for each letter
vals = islice(count(1), 26)

#get the letters
letters = string.ascii_uppercase

#create a dictionary that combines the two
letterVals = dict(zip(letters, vals))

triangles = triangle_numbers(20)
	
total = 0
for w in words:
	temp = 0
	for c in w:
		temp += letterVals[c]
	if temp in triangles:
		total += 1
		
print(total)
#162
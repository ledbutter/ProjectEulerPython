# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.
# What is the total of all the name scores in the file?

from itertools import count, islice
import string



f = open('names.txt')

input = f.read()

f.close()

names = input.split(",")

names.sort()

#could just do a range(1, 26), but this is more fun
vals = islice(count(1), 26)

letters = string.ascii_uppercase

letterVals = dict(zip(letters, vals))

def nameValue(name, index):
	nameSum = 0
	for n in name:
		nameSum += letterVals[n]
	return nameSum * index
		
i = 1
total = 0
for name in names:
	total += nameValue(name, i)
	i += 1

print(total)
	

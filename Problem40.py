# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1  d10  d100  d1000  d10000  d100000  d1000000

from itertools import count
# from operator import mul
# from functools import reduce

product = 1

irr_fraction = count(1)

whole_deal = ""

for x in irr_fraction:
	whole_deal += str(x)
	if len(whole_deal) >= 1000000:
		break
		
product = int(whole_deal[0]) * int(whole_deal[9]) * int(whole_deal[99]) * int(whole_deal[999]) * int(whole_deal[9999]) * int(whole_deal[99999]) * int(whole_deal[999999])
	
print(product)
#210

# s = ''.join([str(x) for x in range(0,1000000)])
# print(reduce(mul,[int(s[10**i]) for i in range(7)]))


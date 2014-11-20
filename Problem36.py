# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

#retrieve the binary representation without the leading 0b prefix
getBin = lambda x: x >= 0 and str(bin(x))[2:]

#shorter, yet more inefficient version
print(sum([i for i in range(1, 1000000, 2) if getBin(i)==getBin(i)[::-1] and str(i) == str(i)[::-1]]))
#872187

# pal_sum = 0

# #can skip evens as they will never be palindromic in base 2
# for n in range(1, 1000000, 2):
	# dec = str(n)
	# #if string is same forwards and backwards
	# if dec == dec[::-1]:
		# binDigits = getBin(n)
		# if binDigits == binDigits[::-1]:
			# pal_sum += n
			
# print(pal_sum)
#872187
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
#numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#906609

match = True
odd = True

stack = []
start = end = 0

largest = 0

for firstNum in range(999,99,-1):
	for num in range(firstNum, 99, -1):
		product = num * firstNum
		if product < largest:
			continue
		stack = []
		for s in str(product):
			stack.append(s)

		match = True
		start = 0
		end = len(stack)-1
		while match and start < end:
			if stack[start] != stack[end]:
				match = False
			else:
				start, end = start + 1, end -1
		if match == True and product > largest:
			largest = product

print(largest)	



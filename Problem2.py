def FibonacciSequence(maxVal):
	firstVal = 0
	secondVal = 1
	currentVal = 0
	
	while firstVal + secondVal <= maxVal:
		currentVal = firstVal + secondVal
		firstVal = secondVal
		secondVal = currentVal
		yield currentVal
		

#vals = FibonacciSequence(4000000)

#sum = 0

#for val in vals:
#	if val % 2 == 0:
#		sum += val
		
#print(sum)

# or from the discussion board....
#This may be a small improvement.  The Fibonacci series is:
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
#Now, replacing an odd number with O and an even with E, we get:
#O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...
#And so each third number is even.  We don't need to calculate the odd numbers.  Starting from any two odd terms x, y, the series is:
#x, y, x + y, x + 2y, 2x + 3y, 3x + 5y

# 1, 1, 1 + 1 = 2, 1 + 2(1) = 3,  2(1) + 3(1) = 5, 3(1) + 5(1) = 8
def SumEvenFib(maxVal):
	x = y = 1
	sum = 0
	while sum < maxVal:
		sum += (x + y)
		x, y = x + 2*y, 2*x + 3*y
	return sum
	
#print(SumEvenFib(4000000))

# just for fun, try summing odds
#  starting from one odd and one even
#  O  O   E    O       0        E
#  x, y, x+y, x+2y, 2x + 3y, 3x + 5y
def SumOddFib(maxVal):
	x = 1
	y = 2
	sum = 0
	
	while sum < maxVal:
		print("X: %i Y: %i" % (x, y))
		print("Fib %i" % (x + y))

		sum += (x + y)

		if y % 2 == 0:
			x, y = y, x + y
		else:
			x, y = x + y, x + 2*y
			
	#return sum

SumOddFib(22)



#x = 1, y = 1
#1+1+3+5+13+21 = 43
#2x + y, 4x + 3y
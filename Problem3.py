#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#	6857

# from math import sqrt

# primes = set([2])
# value = 3
# number = 600851475143
# sq = sqrt(number)
# while value < sq:
	# isPrime = True
	# for k in primes:
		# if value % k == 0:
			# isPrime = False
			# value += 2 # why not + 1 ????
	# if isPrime:
		# primes.add(value)
		# if number % value == 0:
			# print(value)
			# number /= value
# print(number)


number = 600851475143
n = 1

while number > 1:
	n += 1
	if number%n == 0:
		number /= n
		
print(n)
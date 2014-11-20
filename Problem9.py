# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 31875000

# find numbers for which a**2 + b**2 == c**2

# product = 0

# for a in range(997):
	# for b in range(a, 998):
		# for c in range(b, 999):
			# if a + b + c == 1000 and a**2 + b**2 == c**2:
				# product = a*b*c
				# break
		# if product != 0:
			# break
	# if product != 0:
			# break
			
# print(product)

n = 1000

sq = list(map(lambda x: x*x, range(0, n//2+1)))
j,t = divmod(n,2)
t = 0
for i in range(1,n//4):
	while True:
		t += 1
		c = ((sq[i] + sq[j])**0.5)
		d = i+j+c
		if d > n:
			j -= 1
		elif d == n:
			print(i*j*c)
			break
		else:
			break
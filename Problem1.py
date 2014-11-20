
total = 0

for i in range(1, 1000):
	#print(i)
	if i % 3 == 0 or i % 5 == 0:
		total += i

print(total)


print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))
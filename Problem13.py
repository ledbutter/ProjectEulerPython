#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# 5537376230
from functools import reduce

grid = [[int(val) for val in line.split(' ')] for line in open("Problem13Input.txt")]

colCount = 50
rowCount = 100

#sum up the digits of the last column, add remainder to next column, etc. etc

results = []

sum = remainder = temp = 0

for column in range(colCount-1, -1, -1):
	sum = remainder
	for row in range(rowCount):
		#cast to string as the grid just has one huge number per row
		rowStr = str(grid[row]).replace("[", "").replace("]", "")
		sum += int(rowStr[column])
		#sum += grid[row][column]
		
	(temp, remainder) = divmod(sum, 10)
	if column > 0:
		results.append(remainder)
		remainder = temp
	else:
		results.append(sum)
	

final = ""
for i in list(reversed(results))[0:10]:
	final += str(i)
	
print("Result: %s" % final)
# 553737623039 with the 39 being extra (due to the final column adding up to triple digits (i.e. it is 553))
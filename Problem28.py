# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
from math import floor
		
grid = []

row_count = column_count = 1001

start_row = current_row = int(floor(row_count / 2))
start_column = current_column = int(floor(column_count / 2))

grid = []

for row in range(row_count):
	r = []
	for col in range(column_count):
		r.append(0)
	grid.append(r)

#print(grid)

val = 1

# grid[current_row][current_column] = val++#1
# grid[current_row][++current_column] = val++#2  1 2
# grid[++current_row][current_column] = val++#3  1
# grid[current_row][--current_column] = val++#4  2 4
# grid[current_row][--current_column] = val++#5  2
# grid[--current_row][current_column] = val++#6  2
# grid[--current_row][current_column] = val++#7  2
# grid[current_row][++current_column] = val++#8  3 6
# grid[current_row][++current_column] = val++#9  3
# grid[current_row][++current_column] = val++#10 3
# grid[++current_row][current_column] = val++#11 3
# grid[++current_row][current_column] = val++#12 3
# grid[++current_row][current_column] = val++#13 3
# grid[current_row][--current_column] = val++#14 4 12
# grid[current_row][--current_column] = val++#15 4
# grid[current_row][--current_column] = val++#16 4
# grid[current_row][--current_column] = val++#17 4
# grid[--current_row][current_column] = val++#18 4
# grid[--current_row][current_column] = val++#19 4
# grid[--current_row][current_column] = val++#20 4
# grid[--current_row][current_column] = val++#21 4
# grid[current_row][++current_column] = val++#22 4
# grid[current_row][++current_column] = val++#23 4
# grid[current_row][++current_column] = val++#24 4
# grid[current_row][++current_column] = val++#25 4

max_val = row_count * column_count

grid[start_row][start_column] = val
val += 1

loop_num = 1

while val <= max_val:
	#right, down, left, left, up, up, right, right
	#right, down, down, down, left, left, left, left, up, up, up, up, right, right, right, right
	
	current_column += 1
	grid[current_row][current_column] = val
	val += 1
	for i in range(loop_num*2-1):
		current_row += 1
		grid[current_row][current_column] = val
		val += 1
	for i in range(loop_num*2):
		current_column -= 1
		grid[current_row][current_column] = val
		val += 1
	for i in range(loop_num*2):
		current_row -= 1
		grid[current_row][current_column] = val
		val += 1
	for i in range(loop_num*2):
		current_column += 1
		grid[current_row][current_column] = val
		val += 1
	loop_num += 1

sum = 0
for i in range(row_count):
	#print(grid[i][i], grid[i][column_count-i-1])
	sum += grid[i][i] 
	if i != column_count-i-1:
		sum += grid[i][column_count-i-1]
	
print(sum)
#669171001

# for g in grid:
	# print(g)
#print(grid)
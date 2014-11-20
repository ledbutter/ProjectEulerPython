# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8
# out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this 
# process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first
# falls below 10%?

# i finally took the time to try to figure out if there was a pattern here, and there is
#first row of diagonals with value and offset from start in parentheses: 3(2), 5(4), 7(6), 9(8)
#second row: 13(10), 17(12), 21(14), 25(16)
#third row: 31(18), 37(20), 43(22), 49(24)
#fourth row: 57(26), 65(28), 73(30), 81(32)

#so we just need to keep track of our diagonal values, and screw keeping track of the whole grid

from Utils import is_prime
from math import sqrt

def add_diagonal_set(diagonals):
	if len(diagonals) != 0:
		# grab the last value we added...
		last_val = max(diagonals)
		# ...and take advantage of the fact that that will be a square root, and know that our next value will be based
		# on that square root plus 1
		next_val = int(sqrt(last_val)) + 1
		diagonals.add(last_val + next_val)
		diagonals.add(last_val + next_val*2)
		diagonals.add(last_val + next_val*3)
		diagonals.add(last_val + next_val*4)
	else:
		diagonals.add(1)
		diagonals.add(3)
		diagonals.add(5)
		diagonals.add(7)
		diagonals.add(9)
	#print(diagonals)
	return diagonals
	
def update_primes(prime_diagonals, diagonals):
	try:
		biggest_prime = max(prime_diagonals)
	except ValueError:
		print("Empty prime diagonals, using 0 as biggest prime")
		biggest_prime = 0
	candidates = filter(lambda d: d > biggest_prime, diagonals)
	for c in candidates:
		if is_prime(c):
			prime_diagonals.add(c)
	return prime_diagonals

def calculate_percentage(prime_diagonals, diagonals):
	return len(prime_diagonals)/len(diagonals)

diagonals = set()
prime_diagonals = set()
percentage = 0.999
side_length = 1
#fake_counter = 0
while percentage > .10:
	diagonals = add_diagonal_set(diagonals)
	prime_diagonals = update_primes(prime_diagonals, diagonals)
	percentage = calculate_percentage(prime_diagonals, diagonals)
	side_length += 2
	#print("Grid of length %i has %s percentage" % (side_length, percentage))
	# fake_counter += 1
	# if fake_counter == 3:
		# break
print(len(diagonals))
#my looping logic was never quite right but i got the right answer by printing out the value for each iteration and found
#it there
#26241



# this would eventually reach the answer, but would take a long, long time
# from math import floor
# from Utils import is_prime
		
# def generate_new_grid(side_length):
	# grid = []
	# row_count = column_count = side_length
	# start_row = current_row = int(floor(row_count / 2))
	# start_column = current_column = int(floor(column_count / 2))

	# for row in range(row_count):
		# r = []
		# for col in range(column_count):
			# r.append(0)
		# grid.append(r)
		
	# val = 1
	
	# max_val = row_count * column_count

	# grid[start_row][start_column] = val
	# val += 1

	# loop_num = 1

	# while val <= max_val:
		# current_column += 1
		# grid[current_row][current_column] = val
		# val += 1
		# for i in range(loop_num*2-1):
			# current_row -= 1
			# grid[current_row][current_column] = val
			# val += 1
		# for i in range(loop_num*2):
			# current_column -= 1
			# grid[current_row][current_column] = val
			# val += 1
		# for i in range(loop_num*2):
			# current_row += 1
			# grid[current_row][current_column] = val
			# val += 1
		# for i in range(loop_num*2):
			# current_column += 1
			# grid[current_row][current_column] = val
			# val += 1
		# loop_num += 1
		
	# #print(grid)	
	# return grid
	
# def update_grid(grid, side_length):
	# #this is where i need to start
	
	# current_length = len(grid)
	# length_diff = side_length - current_length
	# if length_diff != 2:
		# raise Exception("Invalid new side length, needs to be two")
	
	# # grab the last value used
	# last_val = grid[current_length - 1][current_length - 1]
	
	# # add a row at top and bottom
	# r = []
	# for c in range(side_length):
		# r.append(0)
	# grid.insert(0, r)
	# grid.append(r)
	
	# # now update each row to add a 0 at start and end
	# for i in range(1, current_length+1):
		# grid[i].insert(0, 0)
		# grid[i].append(0)
		
	# # for row in grid:
		# # print(row)
	
	# # now turn those 0's into the right values
	# current_row = current_length 
	# current_column = side_length - 1
	# val = last_val + 1
	# new_rows = []
	# for r in range(side_length):
		# c = []
		# for col in range(side_length):
			# c.append(grid[r][col])
		# new_rows.append(c)
	
	# for i in range((side_length - 1)*4):
		# new_rows[current_row][current_column] = val
		# #grid[current_row][current_column] = val
		# #print("Val at row %i and column %i is %i" % (current_row, current_column, val))
		
		# if current_row > 0 and current_column == (side_length - 1):
			# # we are going up the right side
			# current_row -= 1
		# elif current_row == 0 and current_column > 0:
			# # we are going across the top
			# current_column -= 1
		# elif current_column == 0 and current_row < (side_length - 1):
			# # we are going down the left side
			# current_row += 1
		# else:
			# # we are going across the bottom
			# current_column += 1
		# val += 1
	
	# # for row in new_rows:
		# # print(row)
	# #for row in grid:
	# #	print(row)
	# return new_rows
		
# def generate_grid(side_length, grid=None):
	# row_count = column_count = side_length
	
	# if grid == None:
		# grid = generate_new_grid(side_length)
	# else:
		# grid = update_grid(grid, side_length)
	# return grid
	
# def diagonal_prime_percentage(grid, side_length):
	# diagonals = set()
	# prime_count = 0
	# for i in range(side_length):
		# # upper left to lower right
		# diagonals.add(grid[i][i])
		# # lower left to upper right
		# diagonals.add(grid[side_length-i-1][i])
	# for d in diagonals:
		# if is_prime(d):
			# prime_count += 1
			
	# return prime_count/len(diagonals)
		
# side_length = 7	
# grid = generate_grid(side_length)	
# #print(grid)
# percentage = diagonal_prime_percentage(grid, side_length)

# # fake_counter = 0

# while percentage > 0.099999:
	# side_length += 2
	# grid = generate_grid(side_length, grid)
	# percentage = diagonal_prime_percentage(grid, side_length)
	# #percentage = diagonal_prime_percentage(generate_grid(side_length, grid), side_length)
	# print("Side length of %i has %s percent" % (side_length, percentage))
	# #fake_counter += 1
	# # if fake_counter == 2:
		# # break
	# #break

# print(len(grid))	
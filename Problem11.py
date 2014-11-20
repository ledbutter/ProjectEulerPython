# In the 2020 grid below, four numbers along a diagonal line have been marked in red.
#The product of these numbers is 26  63  78  14 = 1788696.
#What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?
#70600674

from numpy import *


grid = [[int(val) for val in line.split(' ')] for line in open("Problem11Input.txt")]

# temp = 1
# max = index = 0

# a,b,c,d = 0,0,0,0

# length = len(grid)

# for x in range(0, length):
	# for y in range(0, length):
		# if y + 4 < length:
			# #left to right
			# temp = grid[x][y] * grid[x][y+1] * grid[x][y+2] * grid[x][y+3]
			# if temp > max:
				# a,b,c,d = grid[x][y], grid[x][y+1], grid[x][y+2], grid[x][y+3]
				# max = temp
		# if x + 4 < length:
			# #top to bottom
			# temp = grid[x][y] * grid[x+1][y] * grid[x+2][y] * grid[x+3][y]
			# if temp > max:
				# a,b,c,d = grid[x][y], grid[x+1][y], grid[x+2][y], grid[x+3][y]
				# max = temp
		# if x + 4 < length and y + 4 < length:
			# #upper left to bottom right
			# temp = grid[x][y] * grid[x+1][y+1] * grid[x+2][y+2] * grid[x+3][y+3]
			# if temp > max:
				# a,b,c,d = grid[x][y], grid[x+1][y+1], grid[x+2][y+2], grid[x+3][y+3]
				# max = temp
		# if x - 4 > 0 and y - 4 > 0:
			# #upper right to bottom left
			# temp = grid[x][y] * grid[x-1][y-1] * grid[x-2][y-2] * grid[x-3][y-3]
			# if temp > max:
				# a,b,c,d = grid[x][y], grid[x-1][y-1], grid[x-2][y-2], grid[x-3][y-3]
				# max = temp
		# if x - 4 > 0 and y + 4 < length:
			# #lower left to upper right
			# temp = grid[x][y] * grid[x-1][y+1] * grid[x-2][y+2] * grid[x-3][y+3]
			# if temp > max:
				# a,b,c,d = grid[x][y], grid[x-1][y+1], grid[x-2][y+2], grid[x-3][y+3]
				# max = temp
	
# print("%i %i %i %i" %(a,b,c,d))
# print(max)

grid = array(grid)

horiz = max(prod(grid[i, j:j+4]) for i in range(20) for j in range(17))
vert = max(prod(grid[i:i+4,j]) for i in range(17) for j in range(20))
d1 = max(prod(diag(grid[i:i+4,j:j+4])) for i in range(17) for j in range(17))
d2 = max(prod(diag(grid[i:i+4,j+4:j:-1])) for i in range(17) for j in range(17))
print(max(horiz, vert, d1, d2))


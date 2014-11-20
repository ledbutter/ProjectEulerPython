#Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#How many routes are there through a 20x20 grid?
# factorial(2*20)/(factorial(20)*factorial(20))
# = 137846528820
#http://joaoff.com/2008/01/20/a-square-grid-path-problem/

# My solution uses a top down approach. For example for 1x1 grid, we can reach the corner from its neighboring nodes in 1 way.
# 2----1
# |    |
# 1----0

# So to reach it from the top left corner we have 2 ways.
# now suppose a 2x1 grid
# 3----1
# |    |
# 2----1
# |    |
# 1----0

# We can reach the bottom right corner, from the top left corner, by either taking the "down" route which has 2 ways, or the "right" way which has 1 way. 
# So for any NxM grid construct a N+1 x M+1 matrix. Mark

# matrix[N]=1
# matrix[M]=1

# Assuming indexing starts from 0.
# The values for the rest of the cells can be evaluated by:
# matrix[j]=matrix[i+1][j] + matrix[j+1]
# where i=N-1 to 0 and j=M-1 to 0.

l = []
#create 21x21 grid and set each value to 0
for i in range(21):
	l.append([])
	for j in range(21):
		l[i].append(0)		

#set the value for each cell that can only go one way to the end as 1
for i in range(21):
	l[20][i]= 1
	l[i][20] = 1
	
#calculate the rest by adding the values for the cell directly to the right and directly below together
for i in range(19, -1, -1):
	for j in range(19, -1, -1):
		l[i][j]=l[i+1][j]+l[i][j+1]
		
print(l[0][0])
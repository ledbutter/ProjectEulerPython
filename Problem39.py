# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p  1000, is the number of solutions maximised?

# p = 120

# sols = 0

# for a in range(1, p//2):
	# for b in range(a+1, p-a):
		# for c in range(b+1, p-a-b+1):
			# if a**2 + b**2 == c**2 and a+b+c==p:
				# print(a,b,c)
				# sols += 1

# print(sols)

#def possible_perimters(p):

#http://blog.dreamshire.com/2009/04/22/project-euler-problem-39-solution/
# t_max = 0
# p_limit = 1000
 
# for p in range(p_limit//2, p_limit+1, 2):
  # t = 0;
  # for a in range(2, p//4+1):
    # if  p*(p - 2*a) % (2*(p-a)) == 0: t += 1
    # if t > t_max: (t_max, p_max) = (t, p)
		
# print(p_max)
#840

#my original code would have worked but it was incredibly slow,
#this is an optimized version of that code based on the message board
from math import sqrt
	
max_p = max_solutions = current_solutions = 0

for p in range(500, 1001, 2):
	#print(p)
	current_solutions = 0
	
	for a in range(1, p//4):
		for b in range(a+1, (p-a)//2):
			c = sqrt(a**2+b**2)
			if a+b+c==p:
				#print(a,b,c)
				current_solutions += 1
		
	
	if current_solutions > max_solutions:
		max_p = p
		max_solutions = current_solutions
		
print(max_p, max_solutions)
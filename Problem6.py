# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# 25164150

from itertools import repeat
from functools import reduce

squares = map(pow, range(1, 101), repeat(2, 100))

sumOfSquares = reduce(lambda x, y: x+y, squares)

sumNaturals = sum(range(1, 101))

naturalsSquared = sumNaturals**2

print(naturalsSquared - sumOfSquares)
# 25164150
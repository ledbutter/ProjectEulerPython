#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 232792560

#need to check if divisible by all primes smaller than 20, so:
# 2, 3, 5, 7, 11, 13, 17, 19

from itertools import count

#find first element that is divisible by all nums up to 20
#naive method, very slow
# for i in count(20000, 20):
	# if i % 20 == 0:
		# if i % 19 == 0:
			# if i % 18 == 0:
				# if i % 17 == 0:
					# if i % 16 == 0:
						# if i % 15 == 0:
							# if i % 14 == 0:
								# if i % 13 == 0:
									# if i % 12 == 0:
										# if i % 11 == 0:
											# if i % 10 == 0:
												# if i % 9 == 0:
													# if i % 8 == 0:
														# if i % 7 == 0:
															# if i % 6 == 0:
																# if i % 5 == 0:
																	# if i % 4 == 0:
																		# if i % 3 == 0:
																			# if i % 2 == 0:
																				# num = i
																				# break
									
# print(num)

i = 1
#find smallest number that is divisible by each of 1-20
for k in (range(1,21)):
	if i % k > 0:
		for j in range(1, 21):
			# if i is not divisible by k, then multiply it by each number until it is divisible
			if (i*j) % k == 0:
				# set i to that value and go to next value
				i *= j
				break
				
print(i)
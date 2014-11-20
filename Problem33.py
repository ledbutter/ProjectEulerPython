# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.



fractions = []
for divisor in range(10,100):
	for dividend in range(divisor+1,100):
		if divisor % 10 != 0 and dividend % 10 != 0:
			#try dividing the divisors and dividends by 10...
			#...grabbing the result of the divisor...
			dropped_divisor, temp_div = divmod(divisor,10)
			#...and the mod of the dividend
			temp_end, dropped_dividend = divmod(dividend,10)
			#are they equal?
			if (temp_div == temp_end and divisor/dividend) == (dropped_divisor/dropped_dividend):
				print("Adding %i/%i= %.2f" % (divisor, dividend,(divisor/dividend)))
				fractions.append(divisor/dividend)
	
#((16/64)*(19/95)*(26/65)*(49/98)
#print(fractions)
#387296/38729600 = 100
	
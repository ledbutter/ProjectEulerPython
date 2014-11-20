#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numberMap = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
			10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
			20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
	
sum = 0	
hundo = len("hundred")
andLen = len("and")

# wrong: 11622, 11595, 21125

def calculate_div_mod(i, divisor):
	return divmod(i, divisor)

for i in range(1, 1001):
	#print(i)
	if i < 21:
		print(numberMap[i])
		sum += len(numberMap[i])
	elif i < 100:
		(div, remainder) = calculate_div_mod(i, 10)
		sum += len(numberMap[div*10])
		if remainder in numberMap:
			sum += len(numberMap[remainder])
			print("%s %s" %(numberMap[div*10], numberMap[remainder]))
		else:
			print("%s" % numberMap[div*10])
	elif i < 1000:
		(div, remainder) = calculate_div_mod(i, 100)
		# x + "hundred"
		sum += len(numberMap[div]) + hundo
		if remainder < 21 and remainder > 0:
			#+ "and" + y
			sum += andLen + len(numberMap[remainder])
			print("%s hundred and %s" % (numberMap[div], numberMap[remainder]))
		elif remainder > 20:
			#+ "and" + y
			temp = numberMap[div]
			(div, remainder) = calculate_div_mod(remainder, 10)
			sum += andLen + len(numberMap[div*10])
			if remainder in numberMap:
				print("%s hundred and %s %s" % (temp, numberMap[div*10], numberMap[remainder]))
				sum += len(numberMap[remainder])
			else:
				print("%s hundred and %s" % (temp, numberMap[div*10]))
		else:
			print("%s hundred" % numberMap[div])
	else:
		print("one thousand")
		sum += len("onethousand")
	
print(sum)
#21124
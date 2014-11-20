# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#1/1/1901 was a Tuesday

#python has date support, so this could be as simple as this:
	#import datetime
	#count = 0
	#for y in range(1901,2001):
		#for m in range(1,13):
			#if datetime.datetime(y,m,1).weekday() == 6:
				#count += 1
	#print count
#but i didn't think to look for that and rolled my own


from itertools import cycle, compress

months = []
january = march = may = july = august = october = december = range(1,32)
april = june = september = november = range(1,31)
february = range(1,29)

months.append(january)
months.append(february)
months.append(march)
months.append(april)
months.append(may)
months.append(june)
months.append(july)
months.append(august)
months.append(september)
months.append(october)
months.append(november)
months.append(december)

def find_sundays(days_of_week, month, year):
	if len(month) != 28 or year % 4 > 0:
		return list((s for s in compress(month, days_of_week)))
	else:
		leap_february = []
		for i in month:
			leap_february.append(i)
		leap_february.append(29)
		return list((s for s in compress(leap_february, days_of_week)))
	

def calculate_offset(sundays, month, year):
	last_sunday = sundays[-1]
	last_day_of_month = month[len(month)-1]
	if len(month) == 28 and year % 4 == 0:
		last_day_of_month += 1
	return 7 - (last_day_of_month - last_sunday)
	
	
first_sundays = 0
offset = [0,0,0,0,0,1,0]
day_offset = 0
d_o_w = cycle(offset)

for year in range(1901, 2001):
	for month in months:
		sundays = find_sundays(d_o_w, month, year)
		if 1 in sundays:
			first_sundays += 1
		day_offset = calculate_offset(sundays, month, year)
		offset = []
		for d in range(7):
			if d == day_offset-1:
				offset.append(1)
			else:
				offset.append(0)
		d_o_w = cycle(offset)

print(first_sundays)
#171!!!!

# suns = find_sundays(d_o_w, january, 1901)
# for s in suns:
	# print(s)
# day_offset = calculate_offset(suns, january, 1901)
# #print(day_offset)
# offset = []
# for d in range(7):
	# if d == day_offset-1:
		# offset.append(1)
	# else:
		# offset.append(0)
# #print(offset)
# d_o_w = cycle(offset)

# #print(d_o_w)

# print("\n")

# suns = find_sundays(d_o_w, february, 1901)
# for s in suns:
	# print(s)
# day_offset = calculate_offset(suns, february, 1901)

# print(day_offset)

# for month in months:
	# sundays = find_sundays(d_o_w, month, 1901)
	# for s in sundays:
		# print(s)
	
	# day_offset = calculate_offset(sundays, month, 1901)
	# #print("Day Offset: %i\n" % day_offset)
	# offset = []
	# for d in range(7):
		# if d == day_offset-1:
			# offset.append(1)
		# else:
			# offset.append(0)
	# d_o_w = cycle(offset)
	# #print(offset)
	# print("\n")
	
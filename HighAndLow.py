def high_and_low(numbers):
	data = numbers.split()
	low = int(data[0])
	high = low


	for item in data:
		number = int(item)
		if number > high:
			high = number
		if number < low:
			low = number
	
	return '' + str(high) + ' ' + str(low)

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
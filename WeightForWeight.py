import math

def sum_digits(input):
	total = 0
	while input > 0:
		total += (input % 10)
		input = math.floor(input / 10)
	return total

def order_weight(string):
	strItems = string.split()
	items = []
	for item in strItems:
		items.append(int(item))

	items.sort(key=sum_digits)
	print(''.join(items))
#	return returnString

order_weight('103 123 4444 99 2000')
# assert sum_digits(1) == 1
# assert sum_digits(12) == 3
# assert sum_digits(123) == 6
# assert order_weight('103 123 4444 99 2000') == '2000 103 123 4444 99'

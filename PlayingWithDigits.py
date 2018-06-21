import math

def dig_pow(n, p):
	n2 = n
	digits = []
	while n2 > 1:
		digits.append(n2%10)
		n2 = math.floor(n2 / 10)
	
	total = 0
	while len(digits) > 0:
		digit = digits.pop()
		total += digit**p
		p += 1

	k = 1
	while k <= total/n:
		if n*k == total:
			break
		k += 1

	if k > total/n:
		k = -1
		
	return k

print(dig_pow(92, 1))
print(dig_pow(89, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
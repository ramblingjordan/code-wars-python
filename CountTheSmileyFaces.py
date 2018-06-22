import re

def count_smileys(arr):
	smileCount =0
	for item in arr:
		if re.match('^[:;][-~]?[)D]$', item):
			smileCount += 1
	return smileCount

print(count_smileys([':)', ';D', ':(']))

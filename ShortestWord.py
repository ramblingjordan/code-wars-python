def find_short(s):
	data = s.split()
	shortLength = len(data[0])
	for item in data:
		if len(item) < shortLength:
			shortLength = len(item)
	
	return shortLength

print(find_short("one two three four"))
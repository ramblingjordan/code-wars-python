def disemvowel(string):
	output = ''
	for letter in string:
		if letter.lower() not in 'aeiou':
			output += letter
	return output

print(disemvowel('This website is for losers LOL!'))
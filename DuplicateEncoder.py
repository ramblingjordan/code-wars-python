def duplicate_encode(word):
	encodedWord = ''
	inputWord = str(word).lower()
	for letter in inputWord:
		if inputWord.count(letter) > 1:
			encodedWord += ')'
		else:
			encodedWord += '('
	return encodedWord

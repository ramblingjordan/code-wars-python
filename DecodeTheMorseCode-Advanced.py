import unittest

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
MORSE_CODE = {value:key for key,value in CODE.items()}


def decodeMorse(morse_code):
	words = str(morse_code).split('   ')
	message = ''

	for w in words:
		letters = w.split()
		for l in letters:
			message += MORSE_CODE[l]
		message += ' '	
	return message.strip()

## ===================
## String -> String
## produce a string without leading or trailing
## zeros '0' from given string
def stripZeros(bits):
	if len(bits) == 0:
		return bits
	elif bits[0] == '0':
		return stripZeros(bits[1:])
	elif bits[-1] == '0' and len(bits) != 1:
		return stripZeros(bits[:-1])
	return bits

## ===================
## String -> Integer
## produce transmission rate from given bit stream
def transmissionRate(bits):
	if len(bits) <= 2:
		return len(bits)
	if bits == '101':
		return 1

	for i in range(1,len(bits)-2):
		check_code = '1' + i*'0' + '1'
		if bits.find(check_code) > -1:
			return i
	return 1


def normalizeBitStream(bits, transRate):
	if len(bits) <= transRate:
		return bits[0]
	else:
		return bits[0] + normalizeBitStream(bits[transRate:], transRate)

def getWords(bits):
	return bits.split('0'*7)

def convertBitWordToMorseWord(word):
	if len(word) == 0:
		return ''
	elif word == '1':
		return '.'
	#elif word == '111':
	#	return '-'
	elif word[:3] == '000':
		return ' ' + convertBitWordToMorseWord(word[3:])
	elif word[0] == '0':
		return '' + convertBitWordToMorseWord(word[1:])
	elif word[:3] == '111':
		return '-' + convertBitWordToMorseWord(word[3:])
	else:
		return '.' + convertBitWordToMorseWord(word[1:])
	
def convertBitPhraseToMorsePhrase(words):
	if len(words) == 0:
		return []
	return [convertBitWordToMorseWord(words[0])] + convertBitPhraseToMorsePhrase(words[1:])
	

## ===================
## String -> String
## produce morse code '-' '.' and ' ' from given bit stream
def decodeBits(bits):
	bits = stripZeros(bits)
	transRate = transmissionRate(bits)
	bits = normalizeBitStream(bits, transRate)
	words = getWords(bits)
	phrase = '   '.join(convertBitPhraseToMorsePhrase(words))
	return phrase
	

class TestUM(unittest.TestCase):
	def test_decodeBits(self):
		self.assertEqual(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'),
		'.... . -.--   .--- ..- -.. .')

	def test_convertBitPhraseToMorsePhrase(self):
		self.assertEqual(convertBitPhraseToMorsePhrase(['10101', '10111', '111', '1', '11101011101']), 
						['...', '.-', '-', '.', '-.-.'])

	def test_convertBitWordToMorseWord(self):
		self.assertEqual(convertBitWordToMorseWord('10101'), '...')
		self.assertEqual(convertBitWordToMorseWord('10111'), '.-')
		self.assertEqual(convertBitWordToMorseWord('111'), '-')
		self.assertEqual(convertBitWordToMorseWord('1'), '.')
		self.assertEqual(convertBitWordToMorseWord('11101011101'), '-.-.')

	def test_normalizeBitStream(self):
		self.assertEqual(normalizeBitStream('110011', 2), '101')
		self.assertEqual(normalizeBitStream('111000111000000000111000111', 3), '101000101')

	def test_getWords(self):
		self.assertEqual(getWords('100000001'), ['1', '1'])
		self.assertEqual(getWords('1000000010110010000000101'), ['1', '1011001', '101'])

	def test_transmissionRate(self):
		self.assertEqual(transmissionRate('1'), 1)
		self.assertEqual(transmissionRate('1100110011'), 2)
		self.assertEqual(transmissionRate('1100101001'), 1)

	def test_stripZeros(self):
		self.assertEqual(stripZeros('00100'), '1')
		self.assertEqual(stripZeros('10001'), '10001')
		self.assertEqual(stripZeros('0'), '')
		self.assertEqual(stripZeros('1'), '1')


	def test_answer_1(self):
		self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 
						'HEY JUDE')

	
if __name__ == '__main__':
    unittest.main()
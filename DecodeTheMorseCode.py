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


class TestUM(unittest.TestCase):

	def test_answer_1(self):
		self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

	
if __name__ == '__main__':
    unittest.main()
import unittest



def countDuplicates(text):
	count = 0
	text = text.lower()

	while(len(text) > 0):
		if (text.count(text[0]) > 1):
			count += 1
		text = text.replace(text[0], '')
	
	return count



class TestUM(unittest.TestCase):

	def test_answer_1(self):
		self.assertEqual(countDuplicates('abcde'), 0)

	def test_answer_2(self):		
		self.assertEqual(countDuplicates('abcdea'), 1)

	def test_answer_3(self):
		self.assertEqual(countDuplicates('indivisibility'), 1)

	def test_answer_4(self):
		self.assertEqual(countDuplicates('aabbcc'), 3)

if __name__ == '__main__':
    unittest.main()
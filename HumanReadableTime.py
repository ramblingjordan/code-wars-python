import unittest

# minute = 60
# hour   = 3600

def make_readable(seconds):
	
	hour = str(seconds // 3600)
	seconds = seconds % 3600
	minute = str(seconds // 60)
	seconds = str(seconds % 60)
	
	return hour.zfill(2) + ":" + minute.zfill(2) + ":" + seconds.zfill(2)



class TestUM(unittest.TestCase):

	def test_answer_1(self):
		self.assertEqual(make_readable(0), "00:00:00")

	def test_answer_2(self):		
		self.assertEqual(make_readable(5), "00:00:05")

	def test_answer_3(self):
		self.assertEqual(make_readable(60), "00:01:00")

	def test_answer_4(self):
		self.assertEqual(make_readable(86399), "23:59:59")

	def test_answer_5(self):
		self.assertEqual(make_readable(359999), "99:59:59")	

if __name__ == '__main__':
    unittest.main()
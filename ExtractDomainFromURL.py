import unittest



def domain_name(url):
	if url[:7] == 'http://':
		return domain_name(url[7:])
	elif url[:8] == 'https://':
		return domain_name(url[8:])
	elif url[:4] == 'www.':
		return domain_name(url[4:])
	elif url.find('.') > -1:
		return domain_name(url[:url.find('.')])
	return url



class TestUM(unittest.TestCase):

	def test_answer_1(self):
		self.assertEqual(domain_name("http://github.com/carbonfive/raygun"), "github")

	def test_answer_2(self):		
		self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")

	def test_answer_3(self):
		self.assertEqual(domain_name("https://www.cnet.com"), "cnet")

if __name__ == '__main__':
    unittest.main()
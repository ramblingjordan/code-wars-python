import unittest

def staysStill(dir1, dir2):
	if (dir1 == 'NORTH') and (dir2 == 'SOUTH'):
		return True
	elif (dir1 == 'SOUTH') and (dir2 == 'NORTH'):
		return True
	elif (dir1 == 'EAST') and (dir2 == 'WEST'):
		return True
	elif (dir1 == 'WEST') and (dir2 == 'EAST'):
		return True
	return False

def dirReduc(arr):

	if len(arr) <= 1:
		return arr 

	for i in range(len(arr)-1):
		if staysStill(arr[i], arr[i+1]):
			return dirReduc(arr[:i] + arr[i+2:])
	
	return arr


class TestUM(unittest.TestCase):

	def test_answer_1(self):
		a = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
		self.assertEqual(dirReduc(a), ['WEST'])

	def test_answer_2(self):		
		u = ['NORTH', 'WEST', 'SOUTH', 'EAST']
		self.assertEqual(dirReduc(u), ['NORTH', 'WEST', 'SOUTH', 'EAST'])

if __name__ == '__main__':
    unittest.main()
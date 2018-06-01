import unittest
from rootCodingTest import *
from objectHelperFunctions import *
from timestringFunctions import *

class testHelperFunctions(unittest.TestCase):
	"""
	Class to test the helper functions.
	"""
	def test_splitTimeString(self):
		print("Testing splitTimeString:")
		self.assertEqual((12, 23), splitTimeString('12:23'))
		self.assertEqual(None, splitTimeString('12:23:23'))
		return
	def test_findTimeDifference(self):
		print("Testing findTimeDifference:")
		self.assertEqual(1.5, findTimeDifference('22:15', '23:45'))
		self.assertEqual(0, findTimeDifference('04:23', '04:23'))
		self.assertEqual(None, findTimeDifference('05:23', '04:23'))
		return
	def test_addValuesFromTuples(self):
		print("Testing addValuesFromTuples:")
		self.assertEqual((2, 3), addValuesFromTuples((1, 2), (1, 1)))
		self.assertEqual(None, addValuesFromTuples((1, 2), (1, 2, 3)))
		self.assertEqual(None, addValuesFromTuples((1), 2))
		return

class testFileOperations(unittest.TestCase):
	"""
	Class to test all the functions dealing with file operations (read/write)
	"""
	def test_readFile(self):
		print("Testing readFile:")
		self.assertEqual({}, readFile('jnuouae'))
		self.assertEqual({}, readFile('testInputs/testBlankInput'))
		self.assertEqual({'Bob': (0,0)}, readFile('testInputs/testSampleInput'))
	def test_writeToFile(self):
		print("Testing writeToFile:")
		self.assertTrue(writeToFile({}))
		self.assertFalse(writeToFile({'a': (1, 2), 'b': (), 'c': ()}))
		self.assertTrue(writeToFile({'a': (1, 2)}))


class testPrimaryFunctions(unittest.TestCase):
	"""
	Class to test all the functions working on the actual problem statement. 
	"""
	def test_checkTripSpeed(self):
		print("Testing checkTripSpeed:")
		self.assertFalse(checkTripSpeed(9, 3, 5))
		self.assertFalse(checkTripSpeed(100, 2, 5, 40))
		self.assertFalse(checkTripSpeed(5, 0))
		self.assertTrue(checkTripSpeed(100, 2, 5, 50))
	def test_updateDriversMap(self):
		print("Testing updateDriversMap:")
		self.assertEqual({'rob': (0, 0)}, updateDriversMap({}, 'rob', (0, 0)))
		self.assertEqual({'rob': (2, 3)}, updateDriversMap({'rob': (0, 0)}, 'rob', (2, 3)))
		self.assertEqual(None, updateDriversMap({}, 'rob', (2, 3)))

if __name__ == '__main__':
	unittest.main()
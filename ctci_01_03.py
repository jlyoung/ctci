"""

Cracking the Coding Interview
Chapter 1:	1.3
Design an algorithm and write code to remove the duplicate characters in a 
string without using any additional buffer. 
NOTE: One or two additional variables are fine. 
An extra copy of the array is not.

Write the test cases for this method

"""
import sys
import unittest

class TestCitcChapter1Question3(unittest.TestCase):
	def setUp(self):
		self.string_with_dupes = "aaababbcbccadeef"
		self.string_no_dupes = "abcdef"

	def test_remove_duplicates(self):
		self.assertEqual(remove_duplicates(self.string_with_dupes),self.string_no_dupes)

def remove_duplicates(string):
	# Convert string to a list because strings are immutable in Python
	string_array = list(string)
	outer = 0
	while outer < len(string_array):
		inner = outer
		while inner < len(string_array):
			if inner == outer:
				inner += 1
				continue
			if string_array[inner] == string_array[outer]:
				string_array.pop(inner)
			else:
				inner += 1
		outer += 1
	# Convert list back into a string
	return ''.join(string_array)

def main():
	while(True):
		try:
			cmd_line = raw_input('(CTRL+C to exit) Enter a string to remove its duplicates:  ')
			print "String without duplicates: %s" % remove_duplicates(cmd_line)
		except (EOFError, KeyboardInterrupt):
			print "\n"
			sys.exit(0)

if __name__ == '__main__':
	main()
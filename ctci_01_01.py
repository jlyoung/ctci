"""

Cracking the Coding Interview
Chapter 1:	1.1
Implement an algorithm to determine if a string has all unique characters.

"""
import sys
import unittest

class TestCitcChapter1Question1(unittest.TestCase):
	def setUp(self):
		self.duplicate_string = "has duplicate char a"
		self.unique_string = "no dupes"

	def test_duplicates(self):
		self.assertFalse(contains_all_unique_chars(self.duplicate_string),'Expected value = {0}, actual value = {1}.'.format(False, True))

	def test_unique(self):
		self.assertTrue(contains_all_unique_chars(self.unique_string),'Expected value = {0}, actual value = {1}.'.format(True, False))

def contains_all_unique_chars(string):
	seen = []
	for char in list(string):
		if char in seen:
			return False
		seen.append(char)
	return True

def main():
	while(True):
		try:
			cmd_line = raw_input('Enter a string... (CTRL+C to exit):  ')
			if contains_all_unique_chars(cmd_line):
				print 'String "%s" contains all unique characters.' % (cmd_line)
			else:
				print 'String "%s" contains duplicate characters.' % (cmd_line)
		except (EOFError, KeyboardInterrupt):
			print "\n"
			sys.exit(0)

if __name__ == '__main__':
	main()
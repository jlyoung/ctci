"""

Cracking the Coding Interview
Chapter 1:	1.4
Write a method to decide if two strings are anagrams or not

"""
import sys
import unittest

class TestCitcChapter1Question4(unittest.TestCase):
	def setUp(self):
		self.anagram_string1 = "williamshakespeare"
		self.anagram_string2 = "iamaweakishspeller"
		self.not_anagram_string1 = "anagram"
		self.not_anagram_string2 = "nagarom"

	def test_anagram_true(self):
		self.assertTrue(are_anagrams(self.anagram_string1, self.anagram_string2))

	def test_anagram_false(self):
		self.assertFalse(are_anagrams(self.not_anagram_string1, self.not_anagram_string2))

def char_dict(string):
	stringset = set(string)
	chardict = dict()
	for char in stringset:
		chardict[char] = string.count(char)
	return chardict

def are_anagrams(string1, string2):
	if len(string1) != len(string2):
		return False
	return char_dict(string1) == char_dict(string2)

def main():
	print "Anagram Tester (CTRL+C to Exit)"
	while(True):
		try:
			string1 = raw_input('Enter string #1: ')
			string2 = raw_input('Enter string #2: ')
			if are_anagrams(string1, string2):
				print "Strings 1 and 2 ARE anagrams."
			else:
				print "Strings 1 and 2 ARE NOT anagrams."
		except (EOFError, KeyboardInterrupt):
			print "\n"
			sys.exit(0)

if __name__ == '__main__':
	main()
"""

Cracking the Coding Interview
Chapter 1:	1.2
Write code to reverse a C style string.
C string means that abcd is represented as five characters,
including the null character.

"""
import sys
import unittest

class TestCitcChapter1Question2(unittest.TestCase):
	def setUp(self):
		self.c_string = "abcd\0"
		self.reversed_c_string = "\0dcba"

	def test_reverse_string(self):
		self.assertEqual(reverse_string(self.c_string),self.reversed_c_string)

def reverse_string(c_string):
	reversed = ""
	for i in range(1, len(c_string)+1):
		reversed += c_string[-i]
	return reversed

def main():
	while(True):
		try:
			cmd_line = raw_input('(CTRL+C to exit) Enter a string to reverse:  ')
			cmd_line += "\0"
			print "Reversed string: %s" % reverse_string(cmd_line)
		except (EOFError, KeyboardInterrupt):
			print "\n"
			sys.exit(0)

if __name__ == '__main__':
	main()
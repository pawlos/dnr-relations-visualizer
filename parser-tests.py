import unittest
import parser

class TestParserFunctions(unittest.TestCase):

	def test_getGuest_works_when_there_is_with_phrase(self):
		self.assertEqual('Coyotee',parser.getGuest('Episode with Coyotee'))

	def test_getGuest_works_when_there_is_only_guest_info(self):
		self.assertEqual('Yosamite Sam', parser.getGuest('Yosamite Sam'))


if __name__ == '__main__':
	unittest.main()
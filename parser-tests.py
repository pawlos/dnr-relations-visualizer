import unittest
import parser
from bs4 import BeautifulSoup

class TestParserFunctions(unittest.TestCase):

	def test_getGuest_works_when_there_is_with_phrase(self):
		self.assertEqual('Coyotee',parser.getGuest('Episode with Coyotee'))

	def test_getGuest_works_when_there_is_only_guest_info(self):
		self.assertEqual('Yosamite Sam', parser.getGuest('Yosamite Sam'))

	def test_parseEpisode_extracts_data_correctly_for_default_html(self):
		html = '<td>1008</td><td><a href="default.aspx?showNum=1008">Building Development Teams with Michelle Smith</a></td><td>7/15/2014</td>'
		html = BeautifulSoup(html)
		episode = parser.parseEpisode(html)
		self.assertEqual(1008, episode['no'])
		self.assertEqual('Michelle Smith', episode['guest'])
		self.assertEqual('Building Development Teams with Michelle Smith', episode['title'])

if __name__ == '__main__':
	unittest.main()
import unittest
import parser
import datetime
from bs4 import BeautifulSoup

class TestParserFunctions(unittest.TestCase):

	def test_getGuest_works_when_there_is_with_phrase(self):
		self.assertEqual('Coyotee',parser.getGuest('Episode with Coyotee'))

	def test_getGuest_works_when_there_is_only_guest_info(self):
		self.assertEqual('Yosamite Sam', parser.getGuest('Yosamite Sam'))

	def test_parseEpisode_extracts_episode_no_correctly(self):
		episode = self.execute()
		self.assertEqual(1008, episode['no'])

	def test_parseEpisode_extract_title_correctly(self):
		episode = self.execute()
		self.assertEqual('Michelle Smith', episode['guest'])

	def test_parseEpisode_extract_guest_correctly(self):
		episode = self.execute()
		self.assertEqual('Building Development Teams with Michelle Smith', episode['title'])

	def test_parseEpisode_extract_date_correctly(self):
		episode = self.execute()
		self.assertEqual(datetime.datetime(2014,7,15), episode['date'])

	def test_encode_datetime_does_correctly_returns_string(self):
		date = datetime.datetime(2014,7,15);
		self.assertEqual('2014-07-15', parser.encode_datetime(date))

	def test_parseEpisode_extract_url_correctly(self):
		episode = self.execute()
		self.assertEqual('http://www.dotnetrocks.com/default.aspx?showNum=1008', episode['url'])

	def execute(self):
		html = '<td>1008</td><td><a href="default.aspx?showNum=1008">Building Development Teams with Michelle Smith</a></td><td>7/15/2014</td>'
		html = BeautifulSoup(html)
		return parser.parseEpisode(html)

if __name__ == '__main__':
	unittest.main()
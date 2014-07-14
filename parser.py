import urllib2
import re
from bs4 import BeautifulSoup

def getGuest(title):
	phrase = re.search('with\s+(.*)', title)
	if phrase:
		return phrase.group(1)
	else:
		return title

def parseEpisode(episode):
	return	{ 'no': int(episode.font.text), 
			  'title': episode.a.text,
              'guest': getGuest(episode.a.text)}


if __name__ == '__main__':
	url = 'http://www.dotnetrocks.com/archives.aspx'

	episodes = urllib2.urlopen(url)

	html = episodes.read()
	parsed_html = BeautifulSoup(html)

	items = map(parseEpisode, 
				parsed_html.findAll('tr', attrs={'class':'archivecell'}))
	sortedEposides = sorted(items, key=lambda item: item.__getitem__, reverse=True)
	print sortedEposides
	print "End"
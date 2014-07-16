import urllib2
import re
import datetime
from bs4 import BeautifulSoup
import json

def getGuest(title):
	phrase = re.search('with\s+(.*)', title)
	if phrase:
		return phrase.group(1)
	else:
		return title

def parseEpisode(episode):
	return	{ 'no': int(episode.td.text), 
			  'title': episode.a.text,
              'guest': getGuest(episode.a.text),
              'date': datetime.datetime.strptime(episode.findAll('td')[2].text, '%m/%d/%Y')}

def encode_datetime(obj):
	if isinstance(obj, datetime.datetime):
		return obj.strftime('%Y-%m-%d')
	raise TypeError(repr(o) + " is not JSON serializable")

def toJson(episodes):
	with open('episodes.json', 'w') as output:
		json.dump(episodes, output, default=encode_datetime)


if __name__ == '__main__':
	url = 'http://www.dotnetrocks.com/archives.aspx'

	episodes = urllib2.urlopen(url)

	html = episodes.read()
	parsed_html = BeautifulSoup(html)

	items = map(parseEpisode, 
				parsed_html.findAll('tr', attrs={'class':'archivecell'}))
	sortedEposides = sorted(items, key=lambda item: item.__getitem__, reverse=True)
	toJson(sortedEposides)

	print "End"
import urllib2
import re
import datetime
from bs4 import BeautifulSoup
import json
import sys

baseUrl = 'http://www.dotnetrocks.com/'
title = 'dotnetorocks scraper'
usage = 'usage: parser.py command\n\ncommand:\n\t\tdownload-all - downloads all episodes info\n'

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
              'url' : baseUrl+episode.a['href'],
              'date': datetime.datetime.strptime(episode.findAll('td')[2].text, '%m/%d/%Y'),
              'episodeLen': 0}

def encode_datetime(obj):
	if isinstance(obj, datetime.datetime):
		return obj.strftime('%Y-%m-%d')
	raise TypeError(repr(o) + " is not JSON serializable")

def extractEpisodeTime(html):
	result = re.search('(\d+) minutes?', html.font.text)
	return int(result.group(1) if result != None else 0)

def toJson(episodes):
	with open('episodes.json', 'w') as output:
		json.dump(episodes, output, default=encode_datetime)

def addEpisodeTime(episode):
	#print episode
	print "Fetching episode no. %d" % episode['no']
	episodeContent = urllib2.urlopen(episode['url'])
	parsed_html = BeautifulSoup(episodeContent)
	length = extractEpisodeTime(
			 	parsed_html.findAll('span', attrs={'id':'ContentPlaceHolder1_lblTime'})[0])
	episode['episodeLen'] = length

	return episode

def downloadEpisodes():
	print "Fetching archives..."
	url = baseUrl + '/archives.aspx'

	episodes = urllib2.urlopen(url)

	html = episodes.read()
	parsed_html = BeautifulSoup(html)
	print "Parsing episodes..."
	items = map(parseEpisode, 
				parsed_html.findAll('tr', attrs={'class':'archivecell'}))
	item = map(addEpisodeTime, items)
	sortedEposides = sorted(items, key=lambda item: item.__getitem__, reverse=True)
	toJson(sortedEposides)
	print "End"

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print title
		print usage
	else:
		action = sys.argv[1]
		if action == 'download-all':
			downloadEpisodes()
		else:
			print 'Unknown command'

import urllib2
from bs4 import BeautifulSoup


url = 'http://www.dotnetrocks.com/archives.aspx'

episodes = urllib2.urlopen(url)

html = episodes.read()
parsed_html = BeautifulSoup(html)

items = map(lambda episode: 
				{ 'no': int(episode.font.text), 
				  'title': episode.a.text }, 
			parsed_html.findAll('tr', attrs={'class':'archivecell'}))
sortedEposides = sorted(items, key=lambda item: item.__getitem__, reverse=True)
print sortedEposides
print "End"
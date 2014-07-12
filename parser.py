import urllib2
from bs4 import BeautifulSoup


url = 'http://www.dotnetrocks.com/archives.aspx'

episodes = urllib2.urlopen(url)

html = episodes.read()
parsed_html = BeautifulSoup(html)

print parsed_html.findAll('tr', attrs={'class':'archivecell'})
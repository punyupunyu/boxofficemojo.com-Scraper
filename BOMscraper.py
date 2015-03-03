
#import relevant libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen

#base urls to work from
base_url = "http://boxofficemojo.com/movies/"
index_url = "alphabetical.htm?letter="


#functions & class objects
def get_movie_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	body_id = soup.find("div id","body")
	
	

#metrics
#budget > Production Budget
#domestic box office > Domestic
#foreign box office > Foreign
#release date > Open date
#max screens > Theaters
#opening screens >Opening/ Theaters
#run time > summary page Runtime:

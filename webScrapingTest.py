
import urllib2 
from bs4 import BeautifulSoup

links = ["http://www.counseling.gatech.edu/content/couples-counseling",
		"http://www.counseling.gatech.edu/content/individual-counseling",
		"http://www.counseling.gatech.edu/content/students-crisis",
		"http://www.counseling.gatech.edu/content/referral-services",
		"http://www.counseling.gatech.edu/content/sexual-assault-response",
		"http://www.counseling.gatech.edu/content/life-skills-workshops",
		"http://www.counseling.gatech.edu/content/guide-psychoeducational-assessment",
		"http://www.counseling.gatech.edu/content/career-counseling",
		"http://www.counseling.gatech.edu/content/psychiatric-services",
		"http://www.counseling.gatech.edu/content/group-counseling"]

for link in links:
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page)
	soup.prettify()
	bodyText = soup.find_all("div", class_="body with-aside")

	# ADD TO DATABASE HERE
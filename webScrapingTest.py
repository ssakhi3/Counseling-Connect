
import urllib2 
from bs4 import BeautifulSoup

wiki = "http://www.counseling.gatech.edu/content/referral-services"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)
soup.prettify()
letters = soup.find_all("div", class_="body with-aside")

print(letters)
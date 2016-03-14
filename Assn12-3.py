import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ") or "http://python-data.dr-chuck.net/known_by_Sayf.html"
iterations = int(raw_input("Enter count: ")) + 1
position = int(raw_input("Enter position: "))

names = []
i = 0

while i < iterations :
    i += 1

    # load page
    print "Retrieving: %s" % url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # parse out anchor tags
    anchor_tags = soup("a")

    # find and follow link to next page
    line = anchor_tags[position - 1]
    url = line.get("href", None)
    name = line.contents[0]
    names.append(name)

print "Last name is %s" % names[-2]

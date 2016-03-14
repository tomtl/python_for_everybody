import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter - ") or "http://python-data.dr-chuck.net/comments_238319.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# retrieve all the span tags and sum numbers
cumulative_total = 0
count = 0
span_tags = soup("span")
for span_tag in span_tags :
    number = int(span_tag.contents[0])
    cumulative_total += number
    count += 1

print "Count %s" % count
print "Sum %s" % cumulative_total

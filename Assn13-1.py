import urllib
import xml.etree.ElementTree as ET

url = "http://python-data.dr-chuck.net/comments_238316.xml"
xml = urllib.urlopen(url).read()
data = ET.fromstring(xml)

counts = data.findall(".//count")

cumulative_total = 0
for count in counts :
  cumulative_total += int(count.text)

print "Sum: %s" % cumulative_total

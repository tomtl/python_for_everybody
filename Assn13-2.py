import urllib
import json

url = "http://python-data.dr-chuck.net/comments_238320.json"

json_data = urllib.urlopen(url).read()
data = json.loads(json_data)

comments = data["comments"]

cumulative_total = 0
for person in comments :
    count = person["count"]
    cumulative_total += count

print "Sum: %s" % cumulative_total

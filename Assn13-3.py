import urllib
import json

# set up url
service_url = "http://python-data.dr-chuck.net/geojson?"
address = "Universidad Tecnologica Boliviana"
url = service_url + urllib.urlencode({'sensor':'false', 'address': address})

# retrieve data
print "Retrieving %s" % url
json_data = urllib.urlopen(url).read()
print "Retrieved", len(json_data), "characters"
data = json.loads(json_data)

# output Place ID
place_id = data["results"][0]["place_id"]
print "Place ID: %s" % place_id

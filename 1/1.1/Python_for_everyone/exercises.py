# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_flags = ssl.CERT_NONE
while True:
    try:
        location = input("Enter location: ")
        if not len(location): raise ValueError
        break
    except:
        print("Enter a valid location")

parms = dict()
parms['address'] = location
parms['key'] = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

try:
    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving %s" %url)
    data = urllib.request.urlopen(url, context = ctx)
    data = data.read().decode()
    print("Retrieved %d characters" %len(data))
except:
    print ("Couldn't connect to %s" %url)
    exit()

data = json.loads(data)
print("Place id %s" %data['results'][0]['place_id'])

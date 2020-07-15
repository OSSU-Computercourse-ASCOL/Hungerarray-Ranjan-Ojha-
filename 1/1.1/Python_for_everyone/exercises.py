# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
try:
    print ("Retrieving %s" %url)
    bdata = urllib.request.urlopen(url, context = ctx)
except:
    print ("Couldn't connect to location %s" %url)
    exit()

data = bdata.read()
print ("Retrieved %d characters" %len(data))
data = ET.fromstring(data.decode())

counts = data.findall('.//count')

print ("Count:", len(counts))
print ("Sum:", sum([int(count.text) for count in counts]))




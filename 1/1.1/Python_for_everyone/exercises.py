# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# ignore ssl certificates 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
try:
    print("Retrieving %s" %url)
    data = urllib.request.urlopen(url, context = ctx)
    data = data.read().decode()
    print ("Retrieved %d characters" %len(data))
except:
    print("Couldn't connect to %s" %url)
    exit()

data = json.loads(data)

print ("Count: %d" %len(data['comments']))
print("Sum: %d" %sum([elem['count'] for elem in data['comments']]))

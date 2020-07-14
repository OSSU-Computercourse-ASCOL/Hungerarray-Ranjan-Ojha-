# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
lim = int(input("Enter count: "))
pos = int(input("Enter position: ")) - 1

for i in range(lim):
    print ("Retrieving: %s" %url)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    url = tags[pos]['href']

print ("Retrieving: %s" %url)
print (tags[pos].contents[0])
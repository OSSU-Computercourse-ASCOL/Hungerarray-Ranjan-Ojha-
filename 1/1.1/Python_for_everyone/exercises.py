# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
html = urllib.request.urlopen(url, context=ctx)

charCount = 0
while True:
    data = html.read(3000)
    if not len(data): break
    if not charCount: print(data.decode())
    charCount += len(data)

print (charCount)
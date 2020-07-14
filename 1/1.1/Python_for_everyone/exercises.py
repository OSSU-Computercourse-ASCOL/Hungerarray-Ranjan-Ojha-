# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter url - ")
try:
    sock.connect((url, 80))
except :
    print ("couldn't connect to %s -> %s" %(url.split('/')[1], url))
    exit()

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)

while True:
    data = sock.recv(512)
    if not len(data): break
    print(data.decode(), end=' ')

sock.close()
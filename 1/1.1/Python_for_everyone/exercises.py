# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire docu-
# ment and count the total number of characters and display the count
# of the number of characters at the end of the document.

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter url - ")
try:
    sock.connect((url.split('/')[2], 80))
except :
    print ("couldn't connect to %s -> %s" %(url.split('/')[2], url))
    exit()

cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
sock.send(cmd)

charCount = 0
while True:
    data = sock.recv(3000)
    if not len(data): break
    if not charCount:
        print(data.decode(), end=' ')
    charCount += len(data)

print (charCount)
sock.close()
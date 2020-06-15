from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.settimeout(5)
s.connect(("www.python.org", 80))  # Connect

s.send(bytes("GET /index.html HTTP/1.0\n\n", 'utf-8'))  # Send request
data = s.recv(10)  # Get response
print(data.encode('utf-8'))
s.close()

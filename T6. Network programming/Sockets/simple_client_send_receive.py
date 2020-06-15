from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 9000))  # Connect


for i in 'abc':
    s.send("Get Hello!\n".encode())  # Send request
    data = s.recv(1000)  # Get response
    print(data)
    time.sleep(5)

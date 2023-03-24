#TCP Client side

import socket

env=''
ip_address = ""
#Create a client side socket using IPv4 (AF_INET) and TCP protocol (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if env == "PRODUCTION":
    ip_address = socket.gethostbyname(socket.gethostname())
#Connect the socket to a server located at a ginven IP address and port
client_socket.connect((ip_address, 12345))

#Receive data from the server... You must specify the max number of bytes to receive
msg = client_socket.recv(10)
print(msg.decode("utf-8"))

msg = client_socket.recv(10)
print(msg.decode("utf-8"))
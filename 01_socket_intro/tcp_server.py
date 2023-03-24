# TCP SERVER SIDE

import socket

# Create a server side socket using IPv4 (AF_INET) and TCP protocol (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#See how to get IP address dynamically
print(socket.gethostname()) # Prints the hostname of the machine
print(socket.gethostbyname(socket.gethostname())) # Prints the IP address of the machine

# Bind the socket to a specific tuple (IP address and port)
server_socket.bind(socket.gethostbyname(socket.gethostname()), 12345)

#Put the socket into listening mode to listen for incoming connections
server_socket.listen()
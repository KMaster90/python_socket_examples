# TCP Server side

import socket

env=''
ip_address = ""
# Create a server side socket using IPv4 (AF_INET) and TCP protocol (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#See how to get IP address dynamically
print(socket.gethostname()) # Prints the hostname of the machine
# print(socket.gethostbyname(socket.gethostname())) # Prints the IP address of the machine

# Bind the socket to a specific tuple (IP address and port)
if env == "PRODUCTION":
    ip_address = socket.gethostbyname(socket.gethostname())

server_socket.bind((ip_address, 12345))

#Put the socket into listening mode to listen for incoming connections
server_socket.listen(0)

#Listen forever to accept ANY connection
while True:
    # Accept every single connection and store two pieces of information
    client_socket, client_address = server_socket.accept()
    print(type(client_socket)) # <class 'socket.socket'>
    print(client_socket) # <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('
    print(type(client_address)) # <class 'tuple'>
    print(client_address) # ('

    print(f"Connection from {client_address} has been established!\n")

    #Send a message to the client
    client_socket.send("Welcome to the server!".encode("utf-8"))

    #Close the connection
    client_socket.close()
    break

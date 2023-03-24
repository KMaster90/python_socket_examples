#UDP Server side
import socket
env=''
ip_address = ""

#Create a server side socket IPv4 (AF_INET) and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind the socket to a specific tuple (IP address and port)
if env == "PRODUCTION":
    ip_address = socket.gethostbyname(socket.gethostname())

server_socket.bind((ip_address, 12345))

#We are not listening or accepting connections since UDP is a connectionless protocol

message, address = server_socket.recvfrom(10)
print(message.decode("utf-8"))
print(address)

message, address = server_socket.recvfrom(10)
print(message.decode("utf-8"))
print(address)
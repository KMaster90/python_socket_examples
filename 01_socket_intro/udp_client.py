#UDP Client side
import socket

env=''
ip_address = ""
#Create a client side socket using IPv4 (AF_INET) and TCP protocol (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if env == "PRODUCTION":
    ip_address = socket.gethostbyname(socket.gethostname())

#Send some information via connectionless protocol
client_socket.sendto("Hello server world!!!".encode("utf-8"),(ip_address,12345))
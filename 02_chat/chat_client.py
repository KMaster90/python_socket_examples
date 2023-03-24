#Chat Client side
import socket
ENV = ''
#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname()) if ENV == "PRODUCTION" else ""
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))
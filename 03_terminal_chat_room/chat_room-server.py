#Chat Server side
import socket, threading

ENV = ''

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname()) if ENV == "PRODUCTION" else ""
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a server socket and listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []

def broadcast_message(message):
    '''Send a message to ALL clients connected to the server'''
    pass

def receive_message(client_socket):
    '''Receive an incoming message from a specific client and forward the message to be broadcast'''
    pass

def connect_client():
    '''Connect an incoming client to the server'''
    while True:
        #Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection with {client_address} has been established!")

        #Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        #Add the client socket and name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #Update the server, individual client, and ALL clients
        print(f"Name of client is {client_name}\n") #server
        client_socket.send(f"{client_name}, you have connected to the server successful!".encode(ENCODER)) #individual client
        broadcast_message(f"{client_name} has joined the chat room!") #ALL clients

#Start the server
print("Server is listening for incoming connections...\n")
connect_client()
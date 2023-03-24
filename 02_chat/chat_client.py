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

#Send/Receive messaged
while True:
    #Receive information from the server and print it
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if the connected server wats to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Server has quit the connection")
        break
    else:
        print(f"Server: {message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#Close the client socket
client_socket.close()
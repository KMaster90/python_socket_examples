#Chat Server side
import socket
ENV = ''
#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname()) if ENV == "PRODUCTION" else ""
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a server socket, bind it to a ip/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Accept any incoming connection and let them know they are connected
print("Server is running... \n")
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server".encode(ENCODER))

#Send/Receive messaged
while True:
    #Receive information from the client and print it
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #Quit if the connected client wats to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

#Close the client socket
server_socket.close()
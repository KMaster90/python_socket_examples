#Chat Client side
import socket, threading, time

ENV = ''

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname()) if ENV == "PRODUCTION" else ""
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    '''Send a message to the server to be broadcast'''
    while True:
            #Get a message from the client
            message = input("")

            #Send the message to the server
            client_socket.send(message.encode(ENCODER))

def receive_message():
    '''Receive an incoming message from the server and display it to the client'''
    while True:
        try:
          #Receive an incoming message from the server
          message = client_socket.recv(BYTESIZE).decode(ENCODER)

          #Check for the name flag, else show the message
          if message == "NAME":
              name = input("Enter your name: ")
              client_socket.send(name.encode(ENCODER))
          else:
              print(message)
        except:
           #An error occurred, close the connection
           print("An error occur")
           client_socket.close()
           break
        
#Create threads to continuosly send and receive messages
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

#Start the client
receive_thread.start()

time.sleep(2)
send_thread.start()
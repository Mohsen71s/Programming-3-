# Importing libraries
import socket
import threading

# This function is used to send messages. 
def send_message(s):
    while True:
        msg = input()
        s.send(bytes(msg, "utf-8"))

# This function is used to receive messages.
def recv_message(s):
    while True:
        msg = s.recv(500)
        print(msg.decode("utf-8"))

# Creating a socket 
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to a specific address and port
s1.bind(("127.0.0.1", 1234))

# Setting the socket to listen mode. It can queue up to 5 connection requests.
s1.listen(5)

# The server runs indefinitely, accepting incoming connections and starting new threads for sending and receiving messages.
while True:
    # Accepting a connection request from a client
    clientSocket, clientAddress = s1.accept()
    print("Connection well done!", clientAddress)

    # Creating new threads for each client to handle sending and receiving messages concurrently
    t1 = threading.Thread(target=send_message, args=(clientSocket,))
    t2 = threading.Thread(target=recv_message, args=(clientSocket,))

    # Starting the threads
    t1.start()
    t2.start()

# Importing the libraries
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

# Creating a socket object
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server at the specified address and port
c.connect(("127.0.0.1", 1234))

# Creating new threads for sending and receiving messages concurrently
t1 = threading.Thread(target=send_message, args=(c,))
t2 = threading.Thread(target=recv_message, args=(c,))

# Starting the threads
t1.start()
t2.start()

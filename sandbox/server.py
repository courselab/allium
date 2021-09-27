#!/usr/bin/env python3
#
# Example of an internet server in Phython.


import socket       # Socket API

PORT = 5555         # Listen on this port
HOST = '127.0.0.1'  # at this interface (localhost).

# Create a TCP socket to receive connection request.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Bind the socket to the specified PORT and HOST
    
    s.bind((HOST, PORT))

    # Start to listen on the socket.
    
    s.listen()

    # Connection request received: accept it.
    # Client ad address addr is connect at the newly created socket conn.
    
    conn, addr = s.accept()

    with conn:
        
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

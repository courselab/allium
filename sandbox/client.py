#!/usr/bin/env python3
#
# Example of an internet client in Python

import socket

HOST = '127.0.0.1'  # Connect to this IP
PORT = 65432        # at this port

# Create a TCP socket to connect to server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Try to connect
    
    s.connect((HOST, PORT))

    # Send byte string through socket
    
    s.sendall(b'Hello, world')

    # Receive up to 1024 bytes from the socket.
    
    data = s.recv(1024)

print('Received', repr(data))

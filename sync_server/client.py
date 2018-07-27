
import socket

HOST = '127.0.0.1'
PORT = 25000

ADDRESS = HOST, PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
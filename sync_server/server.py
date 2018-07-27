
import socket
import threading

HOST = '127.0.0.1'
PORT = 25000

ADDRESS = HOST, PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDRESS)
server.listen(5)
print(f'Server started on {HOST}:{PORT}')


def square(a):
    return a * a


def client_handle():
    while True:
        req = client.recv(128)
        if not req:
            break
        # print(f'Request: {req}')
        client.send(str(square(int(req))).encode() + b'\n')
    # print(f'Connection {addr} ended')


while True:
    client, addr = server.accept()
    # print(f'Connected by {addr}')
    threading.Thread(target=client_handle).start()

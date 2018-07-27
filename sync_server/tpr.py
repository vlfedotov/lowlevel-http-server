# time for request

import socket
import time


ADDRESS = '127.0.0.1', 25000


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDRESS)
        start = time.perf_counter()
        client.send(b'1')
        client.recv(128)
        print(time.perf_counter() - start)

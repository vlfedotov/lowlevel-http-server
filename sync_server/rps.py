# requests per second

import socket
import time
import threading

ADDRESS = '127.0.0.1', 25000


requests = 0


def reset_requests():
    global requests
    while True:
        time.sleep(1)
        print(f'rps: {requests}')
        requests = 0


threading.Thread(target=reset_requests).start()


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(ADDRESS)
        client.send(b'1')
        client.recv(128)
        requests += 1

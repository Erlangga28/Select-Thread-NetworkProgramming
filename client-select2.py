import socket
import sys

server_address = ('127.0.0.1', 5001)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

sys.stdout.write('>>')

try:
    while True:
        msg = str(input())
        client_socket.send(msg.encode())
        sys.stdout.write(client_socket.recv(1024).decode())
        sys.stdout.write(client_socket.recv(1024).decode())

except KeyboardInterrupt:
    client_socket.close()
    sys.exit()

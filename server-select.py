import socket
import select
import sys

server_address = ('127.0.0.1', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_pocket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_pocket, [], [])

        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_pocket.append(client_socket)

            else:
                data = sock.recv(1024).decode()
                print(str(sock.getpeername()), str(data))
                if str(data):
                    sock.send(data.encode())
                else:
                    sock.close()
                    input_pocket.remove(sock)
except KeyboardInterrupt:
    server_socket.close()
    sys.exit()
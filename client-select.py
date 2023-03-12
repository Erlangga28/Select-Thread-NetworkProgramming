import socket
import sys

server_address = ('127.0.0.1', 5000)

client_socket = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)

client_socket.connect((server_address))

while True:
	print("Example : 4 + 5")
	
	inp = input()
	
	if inp == "Over":
		break
	
	client_socket.send(inp.encode())


client_socket.close()

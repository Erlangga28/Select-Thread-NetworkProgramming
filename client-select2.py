import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)

client.connect((SERVER, PORT))

while True:
	file1 = open('text.txt', 'w')
	
	inp = input()
	
	if inp == "Over":
		break
	
	client.send(inp.encode())

client.close()

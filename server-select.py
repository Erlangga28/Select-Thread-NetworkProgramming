import socket
import select
import sys

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

clientConnection, clientAddress = server_socket.accept()
data = ''

try:
	while True:
		data = clientConnection.recv(1024).decode()
		if data == 'Over':
			print("Connection is Over")
			break
		result = 0
		operation_list = data.split()
		oprnd1 = operation_list[0]
		operation = operation_list[1]
		oprnd2 = operation_list[2]

		num1 = int(oprnd1)
		num2 = int(oprnd2)
	
		if operation == "+":
			result = num1 + num2
		elif operation == "-":

			result = num1 - num2
		elif operation == "/":
			result = num1 / num2
		elif operation == "*":
			result = num1 * num2
		
		output = str(result)
		print(clientAddress, num1, operation, num2, "=", result)
		clientConnection.send(output.encode())
except KeyboardInterrupt:
	server_socket.close()
	sys.exit()


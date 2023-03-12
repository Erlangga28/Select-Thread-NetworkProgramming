import socket

server_address = ('127.0.0.1', 5001)

server_socket = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
server_socket.bind((server_address))
server_socket.listen(5)

clientConnection, clientAddress = server_socket.accept()

L = ["anna\n", "civic\n", "racecar\n", "remote\n"]

file1 = open('text.txt', 'w')
file1.writelines(L)
file1.close()

def isPalindrome(s):
        return s == s[::-1]

s = L
ans = isPalindrome(s)

file1 = open('text.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    count += 1
  
if ans:
        print(clientAddress, "Line{}: {}".format(count, line.strip()), " - Yes")
else:
        print(clientAddress, "Line{}: {}".format(count, line.strip()), " - No")
clientConnection.send(line.encode())
file1.close()
clientConnection.close()
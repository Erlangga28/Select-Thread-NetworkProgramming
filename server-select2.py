import socket
import select
import sys

server_address = ('127.0.0.1', 5001)

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_address))
server_socket.listen(5)

input_socket = [server_socket]


try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket,[],[])

        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
            else:
                data = sock.recv(1024).decode()
                print(str(sock.getpeername()), str(data))
                if str(data):

                    L = ["anna\n", "civic\n", "racecar\n", "remote\n"]

                    file1 = open(data, 'w')
                    file1.writelines(L)
                    file1.close()
                    
                    def isPalindrome(s):
                        return s == s[::-1]

                    s = L
                    ans = isPalindrome(s)
                    file1 = open(data, 'r')
                    line = file1.readlines()

                    count = 0

                    if not line:
                        break
  
                    if ans:
                        print("Line{}: {}".format(count, line.strip()), " - Yes")
                    else:
                        print("Line{}: {}".format(count, line.strip()), " - No")
                    file2 = open(data, 'r')
                    view = file2.read()
                    sock.send(view.encode())
                    file2.close()
                else:
                    sock.close()
                    input_socket.remove(sock)
except KeyboardInterrupt:
    server_socket.close()
    sys.exit()
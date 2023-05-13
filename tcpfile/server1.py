import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1340
s.bind((Host, Port))
s.listen(5)
client_socket, address = s.accept()
print(f"Connection to {address} established")
fileName = "test.txt"
client_socket.send(fileName.encode('utf-8'))
def sendFile():
    file = open("tcpfile/test.txt", "rb")
    data = file.read()
    client_socket.send(data)
    file.close()
    client_socket.close()
sendFile()


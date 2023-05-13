import socket
import sys
client = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1340
client.connect((Host, Port))
def reciveFile():
 file_name = client.recv(1024).decode('utf-8')
 file_name = "transferedd "+file_name
 file = open(file_name, "wb")
 data = client.recv(1024)
 file.write(data)
 file.close()
reciveFile()

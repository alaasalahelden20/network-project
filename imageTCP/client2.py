import socket
import sys
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1241
client.connect((Host, Port))
file = open('imageTCP\img.JPG', 'rb')
def img_handelling():
 image_data = file.read(2048)
 while image_data:
  client.send(image_data)
  image_data = file.read(2048)
 file.close()
img_handelling()
client.close()
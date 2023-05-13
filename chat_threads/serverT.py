
import socket
import threading

clients=[]
usernames=[]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host=socket.gethostname()
Port=1345
client.bind((Host, Port))
client.listen(5)

def broadcast(msg):
 for client_socket in clients:
  client_socket.send(msg)

def handle(client_socket):
 while True:
  message = client_socket.recv(1024)
  broadcast(message)

def receive():
  while True:
   client_socket, address = client.accept()
   print(f"Connection to {address} established")
   message = client_socket.send('connected'.encode('utf-8'))
   username = client_socket.recv(1024).decode('utf-8')
   usernames.append(username)
   clients.append(client_socket)
   print(f" {username} joined the chatroom ")
   broadcast(f'{username} joined the chatroom successfully'.encode('utf-8'))
   t1=threading.Thread(target=handle, args=(client_socket,))
   t1.start()

receive()
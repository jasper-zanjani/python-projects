import socket

HEADERSIZE=10
msg = 'Welcome to the server!'
msg = f'{len(msg):<{HEADERSIZE}}{msg}'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)


while True:
  clientsocket, address = s.accept()
  print(f'Connection from {address[0]} has been established')

  clientsocket.send(bytes(msg, 'utf-8'))
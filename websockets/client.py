import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
  full_msg = ''
  new_msg = True
  while True:
    msg = s.recv(12)
    if new_msg:
      print(f'new message length: {msg[:HEADERSIZE]}')
    full_msg += msg.decode('utf-8')
  print(full_msg)
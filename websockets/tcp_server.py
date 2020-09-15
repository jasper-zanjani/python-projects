import socket
from vars import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((host, port))
  s.listen(5)
  connection, addr = s.accept()
  with connection:
    print('[*] Established connection')
    while True:
      data = connection.recv(buffer)
      if not data:
        break
      else:
        print(f'[*] Data received: {data.decode("utf-8")}')
      connection.send(data)
import socket
from vars import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'Hello world, this is my first message'

while True:
  try:
    s.sendto(msg.encode(), (host, port))
    response, addr = s.recvfrom(buffer)
    print(f"Server response => {response.decode('utf-8')}")
  except KeyboardInterrupt:
    break

s.close()
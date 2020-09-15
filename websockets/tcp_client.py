import socket
from vars import *

msg = 'Hello world, this is my first message'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  s.send(msg.encode('utf-8'))
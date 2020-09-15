import socket, sys
from vars import *

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

while True:
  try:
    print('Waiting for client...')
    data, address = s.recvfrom(buffer)
    data = data.strip()
    print(f'Data received from address: {address}')
    print("message: ", data)
    try:
      response = f"Hello  {sys.platform}"
    except Exception as e:
      response = sys.exc_info()[0]
    print("Response", response)

    s.sendto(response.encode(), address)
  except KeyboardInterrupt:
    s.close()
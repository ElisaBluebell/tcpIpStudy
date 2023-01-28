from socket import *

port = 2500
BUFFER = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('10.10.21.121', port))

while True:
    data, address = sock.recvfrom(BUFFER)
    celsius = int(data.decode())
    print(celsius)
    fahrenheit = (celsius * 1.8) + 32
    msg = str(fahrenheit)
    sock.sendto(msg.encode(), address)

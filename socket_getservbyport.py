import socket
for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    print(f'{port:4d}:l {socket.getservbyport(port)}')
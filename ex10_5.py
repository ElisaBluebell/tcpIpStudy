import socket

help(socket.gethostbyname)

print('getattr(SOCK_STREAM):', getattr(socket, 'SOCK_STREAM'))
print()
print('getattr(SOCK_DGRAM):', getattr(socket, 'SOCK_DGRAM'))

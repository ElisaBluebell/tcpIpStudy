import socket
HOSTS = [
    socket.gethostname()
]

for host in HOSTS:
    print('{} : {}'.format(host, socket.gethostbyname(host)))
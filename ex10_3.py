import socket
HOSTS = ['www.naver.com']
for host in HOSTS:
    print(host)
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print(' Hostname:', hostname)
        print(' Aliases :', aliases)
        print(' Addresses:', addresses)
    except socket.error as emsg:
        print('ERROR:', emsg)
    print()

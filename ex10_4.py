import socket

from _socket import gethostbyaddr

try:
    ipaddrlist = socket.gethostbyname('www.ulsan.ac.kr')
    print('IpAddress:', ipaddrlist)
except socket.error as emsg:
    print('Error:', emsg)

try:
    hostbyaddress = gethostbyaddr('147.46.10.58')
    print('Hostname:', hostbyaddress[0])
except socket.error as emsg:
    print('Error:', emsg)
from socket import *

hostname, aliaslist, ipaddrlist = gethostbyaddr('203.249.39.46')

print('Hostname :', hostname)
print('Aliases :', aliaslist)
print('Addresses:', ipaddrlist)

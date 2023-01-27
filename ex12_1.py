from socket import *
import _thread

BUFFSIZE = 1024
host_addr = '10.10.21.121'
port = 2500


def handler(clientsock, addr):
    while True:
        data = clientsock.recv(BUFFSIZE)
        print('data:' + repr(data.decode()))
        if not data:
            break


def write_handler(clientsock, addr):
    while True:
        response = input('메세지 입력: ')
        clientsock.send(response.encode())
        print('sent:' + repr(response))


if __name__ == '__main__':
    ADDR = (host_addr, port)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)

    while True:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        _thread.start_new_thread(handler, (clientsock, addr))
        _thread.start_new_thread(write_handler, (clientsock, addr))

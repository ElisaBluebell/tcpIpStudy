# multiprocessing 모듈을 이용한 TCP 서버 프로그램

from socket import socket
from multiprocessing import Process


def handle(sock):
    while True:
        msg = sock.recv(1024)
        print(f'Received message: {msg.decode()}')
        if msg.decode() == 'Hello':
            p2 = Process(target=hello_answer, args=(sock,))
            p2.start()
        elif msg.decode() == 'Good':
            p3 = Process(target=good_answer, args=(sock,))
            p3.start()
        else:
            sock.send(msg)


def hello_answer(sock):
    sock.send('Hello Client'.encode())


def good_answer(sock):
    sock.send('Good Afternoon'.encode())


if __name__ == "__main__":
    sock = socket()
    addr = ('', 2500)
    sock.bind(addr)
    sock.listen(4)

    while True:
        c_sock, r_addr = sock.accept()
        print(f'{r_addr} is connected')
        p1 = Process(target=handle, args=(c_sock,))
        p1.start()

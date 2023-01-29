import socket
import threading


def handler(sock):
    while True:
        try:
            msg, addr = sock.recvfrom(1024)
        except:
            continue
        else:
            print(msg.decode())

conn = ('localhost', 2500)
svr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_id = input("ID를 입력하세요: ")

cThread = threading.Thread(target=handler, args=(svr,))
cThread.daemon = True
cThread.start()
while True:
    msg = '[' + my_id + '] ' + input()
    svr.sendto(msg.encode(), conn)

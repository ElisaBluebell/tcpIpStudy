# 섭씨온도를 받아 화씨온도로 변환하여 전송하는 TCP 서버 프로그램

import sys
import threading
from socket import *


class ThreadServer(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket  # 인스턴스 변수 정의
        print("New socket added: ", clientAddress)

    def run(self):
        while True:
            data = self.clientsocket.recv(BUFSIZE)  # 데이터 수신
            if not data:  # 연결이 종료되었음
                break
            data = float(data.decode())  # 수신 데이터를 float 형으로 변환
            data = 9.0 / 5.0 * data + 32.0  # 화씨온도 계산
            data = '{:.1f}'.format(data)
            self.clientsocket.send(data.encode())  # 화씨온도 전송


PORT = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(eval(sys.argv[1]))
else:
    port = PORT

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(1)

while True:
    s.listen(1)
    clientsock, clientAddress = s.accept()
    newthread = ThreadServer(clientAddress, clientsock)
    newthread.start()

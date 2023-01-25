# time_server.py

import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
address = ('10.10.21.121', 5000)  # 종단점 주소
sock.bind(address)  # 주소와 소켓 결합
sock.listen(5)  # 연결 대기

while True:
    client, addr = sock.accept()  # 연결 허용. 클라이언트 소켓과 주소 반환
    print("Connection requested from", addr)
    client.send(time.ctime(time.time()).encode())  # bytes형 메시지 전송
    client.close()  # 소켓 해제
# threading 모듈을 이용한 TCP 채팅 서버 프로그램

import socket
import threading


def handler(c, a):  # 데이터를 수신하여 처리하는 함수
    global connections
    while True:
        try:
            data = c.recv(1024)
            if not data:  # 데이터가 없으면 연결이 종료된 것이므로 소켓 제거
                connections.remove(c)
                c.close()
                continue
        except:
            continue

        for connection in connections:
            try:
                connection.send(bytes(data))  # 모든 클라이언트에게 데이터 전송
            except:
                continue


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 2500))
sock.listen(1)
connections = []  # 서버와 연결된 클라이언트 목록
print("서버 준비 완료")

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c, a))  # 서브스레드 생성
    cThread.start()  # 서브스레드 실행
    # ↓파이참이 골라준 워닝을 감추는 주석, 오류에 대한 처리는 아니고 차량 진단기에서 오류 코드 지우는 느낌
    # noinspection PyUnboundLocalVariable
    connections.append(c)  # 새 클라이언트를 목록에 추가
    print("연결된 클라이언트: ", connections)

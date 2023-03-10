# threading class를 이용한 TCP 에코 서버 프로그램

import socket, threading

# threading.Thread 서브 클래스
class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)  # 부모 클래스 __init__() 실행
        self.csocket = clientsocket  # 인스턴스 변수 정의
        print("New socket added: ", clientAddress)

    def run(self):  # 자동 실행
        print("Connection from: ", clientAddress)

        msg = ''
        while True:
            data = self.csocket.recv(2048)  # 데이터 수신
            msg = data.decode()

            if msg == 'quit':  # quit가 수신되면 종료
                break

            print("from client", msg)
            self.csocket.send(bytes(msg, 'UTF-8'))  # 에코

        print("Client at ", clientAddress, " disconnected...")

host = ""
port = 2500

# 서버 소켓 생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("Server started")
print("Waiting for client request..")

while True:  # 클라이언트마다 하나의 스레드가 배정된다.
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

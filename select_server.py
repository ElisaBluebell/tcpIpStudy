# select()를 이용한 다중 TCP 에코 서버
# 읽기 이벤트만 조사한다

import socket, select

sock_list = []  # 이벤트 조사 소켓 목록
BUFFER = 1024
port = 2500

s_sock = socket.socket()  # TCP 소켓
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_sock.bind(('', port))
s_sock.listen(5)

sock_list.append(s_sock)  # 서버 소켓을 목록에 추가
print("Server waiting on port " + str(port))

while True:
    r_sock, w_sock, e_sock = select.select(sock_list, [], [], 0)  # 감시 설정

    for s in r_sock:  # 읽기 이벤트 소켓 조사
        if s == s_sock:  # 서버 소켓?
            c_sock, addr = s_sock.accept()
            sock_list.append(c_sock)  # 클라이언트 소켓 목록 추가
            print(" Client (%s, %s) connected" %addr)
        else:  # 클라이언트 소켓
            try:
                data = s.recv(BUFFER)
                print("Received: ", data.decode())
                if data:
                    s.send(data)  # 에코

            except:  # 연결 종료됨
                print("Client (%s, %s) is offline" %addr)
                s.close()
                sock_list.remove(s)  # 연결이 종료된 소켓은 목록에서 제거
                continue

s_sock.close()

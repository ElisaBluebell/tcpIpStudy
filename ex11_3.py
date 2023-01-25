import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 주소 입력
svrIP = '10.10.21.121'

# 포트 번호 입력
port = 2502  # 기본 포트

sock.connect((svrIP, port))
print('Connected to ' + svrIP)

while True:
    sock.settimeout(1.0)  # 타입아웃을 1.0초로 설정한다.

    # 데이터가 수신되지 않으면 다음으로 진행한다.
    try:
        r_msg = sock.recv(2014)
        print(r_msg.decode())
    except socket.timeout:  # 타입아웃 동안 데이터가 수신되지 않으면 예외발생
        pass

    msg = input('Sending message: ')

    # 송신 데이터가 없으면 다시 진행
    if not msg:
        continue

    try:  # 데이터 전송
        sock.send(msg.encode())  # 메시지 전송

    except:  # 연결이 종료됨
        print('연결이 종료되었습니다.')
        break

    try: # 데이터 읽기
        msg = sock.recv(1024)
        if not msg:
            print("연결이 종료되었습니다.")
            break
        print(f'Received message: {msg.decode()}')

    except:  # 연결이 종료됨
        print("연결이 종료되었습니다.")
        break

sock.close()

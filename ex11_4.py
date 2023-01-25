import socket

# 숫자에 대한 영어 사진
table = {'홍길동': 20150001, '심순애': 20150002, '박문수': 20150003}

s = socket.socket()  # AF_INET, SOCK_STREAM
address = ("10.10.21.121", 2502)
s.bind(address)
s.listen(1)
print('Waiting...')
c_socket, c_addr = s.accept()
print("Connection from", c_addr)
while True:
    data = c_socket.recv(1024).decode()  # 요청 수신
    try:
        resp = table[data]  # 데이터를 key로 사용하여 value를 가져온다.
    except:
        c_socket.send('이름이 없습니다.'.encode())  # 오류가 있을 때
    else:
        c_socket.send(str(resp).encode())  # 변환 값을 전송


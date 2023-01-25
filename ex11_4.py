import socket

# 이름과 학번
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
        # int 자료형은 전송시 오류가 발생하므로 str로 자료형을 변경
        c_socket.send(str(resp).encode())  # 변환 값을 전송


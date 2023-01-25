import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
sock.connect(('10.10.21.121', 5000))  #서버로 연결 요청. 연결되면 반환됨
print("현재 시각: ", sock.recv(1024).decode())  # 데이터 수신
sock.close()  # 소켓을 닫는다.
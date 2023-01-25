import socket

port = 2501  # 포트 번호
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("Waiting for client")
while True:
    print("<- ", end='')
    data, addr = sock.recvfrom(BUFFSIZE)  # 메시지 수신
    print(data.decode())  # 수신 메시지 출력

    resp = input("-> ")
    sock.sendto(resp.encode(), addr)


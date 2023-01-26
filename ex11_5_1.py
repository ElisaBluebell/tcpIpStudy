import socket


def bin_to_dec(binary):
    result = 0
    if binary == 0:
        return 0
    for i in range(len(str(binary))):
        result += (int(str(binary)[-(i + 1)]) * 2) ** i
    return result


port = 3704
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print("수신 대기 중")

while True:
    data, addr = sock.recvfrom(BUFFER)
    print(f"Received message: ({data.decode()[:-1]}, '{data.decode()[-1]}')")
    print(addr)
    data = data.decode()
    if data[-1] == 'b':
        number = str(bin_to_dec(int(data[:-1]))) + 'd'
    else:
        number = str(bin(int(data[:-1]))[2:]) + 'b'
    sock.sendto(number.encode(), addr)

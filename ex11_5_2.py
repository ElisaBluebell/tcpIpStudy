import socket

BUFFSIZE = 1024
port = 3704

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    while True:
        number = input('숫자 입력:')
        try:
            if int(number) < 0:
                print('잘못된 입력입니다.')
            else:
                int(number)
                str(number)
                break
        except:
            print('잘못된 입력입니다.')

    while True:
        binary = input('진수 입력, 1: 10진수, 2: 2진수')
        if binary == '1':
            number += 'd'
            break
        elif binary == '2':
            number += 'b'
            break
        else:
            print('잘못된 입력입니다.')

    sock.sendto(number.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print(f"Server says:({data.decode()[:-1]}, '{data.decode()[-1]}')")

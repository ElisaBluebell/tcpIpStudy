import socket
import threading


def recvmsg():
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                print("연결이 종료되었습니다.")
                break
            print(f'Received message: {msg.decode()}')

        except:
            print("연결이 종료되었습니다.")
            break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svrIP = input(("Server IP(default: 127.0.0.1): "))
if svrIP == '':
    svrIP = '10.10.21.121'

port = input('port(default: 2500): ')
if port == '':
    port = 2500
else:
    port = int(port)

sock.connect((svrIP, port))
print('Connected to ' + svrIP)

while True:
    msg = input('Sending message: ')

    if not msg:
        continue

    try:
        sock.send(msg.encode())

    except:
        print('연결이 종료되었습니다.')
        break
    Thread = threading.Thread(target=recvmsg, daemon=True)
    Thread.start()


sock.close()

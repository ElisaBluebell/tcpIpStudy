# Video server(송신)

import cv2
import imutils
import pickle
import socket
import struct

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9000
server_addr = ('10.10.21.121', port)

# 주소와 포트번호 바인드
server_socket.bind(server_addr)

# 접속 대기
server_socket.listen(5)
print("접속 대기:", server_addr)

# 클라이언트 연결
while True:
    client_socket, addr = server_socket.accept()
    print(addr, '와 연결됨')
    if client_socket:
        vid = cv2.VideoCapture(0)  # 웹카메라
        if vid.isOpened():
            print('width:{}, height:{}'.format(vid.get(3), vid.get(4)))
        while(vid.isOpened()):
            ing, frame = vid.read()  # 프레임 획득
            frame = imutils.resize(frame, width=640)  # 프레임 크기 조절
            frame_bytes = pickle.dumps(frame)  # 프레임을 바이트 스트림으로 변환
            message = struct.pack("Q", len(frame_bytes)) + frame_bytes  # 메시지 = [frame 길이(unsigned 8bytes) + frame]
            client_socket.sendall(message)  # 메시지 전송

            cv2.imshow('Server Video', frame)  # 전송 영상 표시
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()

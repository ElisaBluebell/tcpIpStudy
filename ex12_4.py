from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *


class ChatClient:
    client_socket = None

    def __init__(self):
        self.initialize_gui()

    def initialize_socket(self):
        '''
        TCP socket을 생성하고 server와 연결
        '''
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        remote_ip = self.ip_widget.get()
        remote_port = int(self.port_widget.get())
        self.client_socket.connect((remote_ip, remote_port))
        self.chat_transcript_area.insert('end', '연결되었습니다.\n')
        self.chat_transcript_area.yview(END)
        self.listen_thread()

    def send_chat(self):
        '''
        message를 전송하는 버튼 콜백 함수
        '''
        senders_name = self.name_widget.get().strip() + ":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)  # 수신 창 끝으로 이동
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def initialize_gui(self):
        self.root = Tk()
        fr = []
        for i in range(0, 5):
            fr.append(Frame(self.root))
            fr[i].pack(fill=BOTH)

        self.name_label = Label(fr[0], text='사용자 이름')
        self.recv_label = Label(fr[1], text='수신 메시지:')
        self.send_label = Label(fr[3], text='송신 메시지:')
        self.send_btn = Button(fr[3], text='전송', command=self.send_chat)
        self.chat_transcript_area = ScrolledText(fr[2], height=20, width=60)
        self.enter_text_widget = ScrolledText(fr[4], height=5, width=60)
        self.name_widget = Entry(fr[0], width=10)
        self.ip_label = Label(fr[0], text='서버 주소')
        self.ip_widget = Entry(fr[0], width=10)
        self.port_label = Label(fr[0], text='포트 번호')
        self.port_widget = Entry(fr[0], width=5)
        self.connect_btn = Button(fr[0], text='연결', command=self.initialize_socket)

        self.name_label.pack(side=LEFT)
        self.name_widget.pack(side=LEFT)
        self.ip_label.pack(side=LEFT)
        self.ip_widget.pack(side=LEFT)
        self.port_label.pack(side=LEFT)
        self.port_widget.pack(side=LEFT)
        self.connect_btn.pack(side=RIGHT)
        self.recv_label.pack(side=LEFT)
        self.send_btn.pack(side=RIGHT, padx=20)
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=LEFT)
        self.enter_text_widget.pack(side=LEFT, padx=2, pady=2)

    def listen_thread(self):
        t = Thread(target=self.recieve_message, args=(self.client_socket, ))
        t.start()

    def recieve_message(self, so):
        while True:
            buf = so.recv(256)
            if not buf:  # 연결이 종료됨
                break
            self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
            self.chat_transcript_area.yview(END)
        so.close()


if __name__ == "__main__":
    ChatClient()
    mainloop()

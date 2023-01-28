import threading
from socket import socket, SOCK_STREAM, AF_INET
from tkinter import END, Label, Entry, Button, W, mainloop


class CelToFahClient:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(("localhost", 2500))

        message_label = Label(text='Enter a temperature(c)', font=('D2Coding', 14))
        self.entry1 = Entry(font=('D2Coding', 14), width=5)

        recv_label = Label(text='Temperature in F', font=('D2Coding', 14))
        self.entry2 = Entry(font=('D2Coding', 14), width=5)

        calc_button = Button(text='전송', font=('D2Coding', 12), command=self.calculate)

        message_label.grid(row=0, column=0, sticky=W)
        recv_label.grid(row=1, column=0, sticky=W)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        calc_button.grid(row=0, column=2, padx=10, pady=10)

        cThread = threading.Thread(target=self.handler)
        cThread.daemon = True
        cThread.start()

        mainloop()

    def calculate(self):
        temp = float(self.entry1.get())
        self.sock.send(str(temp).encode())

    def handler(self):
        while True:
            try:
                r_msg = self.sock.recv(1024)
            except:
                pass
            else:
                self.entry2.delete(0, END)
                self.entry2.insert(0, r_msg.decode())
                self.entry1.delete(0, END)


if __name__ == "__main__":
    cel_to_fah_client = CelToFahClient()
    cel_to_fah_client

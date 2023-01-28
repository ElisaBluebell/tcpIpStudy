import sys

from socket import *

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton


class CelToFahClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(100)
        self.setFixedWidth(290)
        self.set_ui()


    def set_ui(self):
        guide = QLabel(self)
        guide.setText('Enter a temperature(c)')
        guide.setGeometry(20, 20, 130, 20)

        result = QLabel(self)
        result.setText('Temperature in F')
        result.setGeometry(20, 60, 200, 20)

        self.celsius = QLineEdit(self)
        self.celsius.setGeometry(170, 20, 40, 20)
        self.celsius.setValidator(QIntValidator(self))

        self.fahrenheit = QLineEdit(self)
        self.fahrenheit.setGeometry(170, 60, 40, 20)
        self.fahrenheit.setReadOnly(True)

        send = QPushButton(self)
        send.setText('전송')
        send.setGeometry(230, 20, 40, 20)
        send.clicked.connect(self.calculate)

    def calculate(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        address = ('10.10.21.121', 2500)
        buffer = 1024
        sock.sendto(self.celsius.text().encode(), address)

        fahrenheit = sock.recvfrom(buffer)[0]
        self.fahrenheit.setText(fahrenheit.decode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    client = CelToFahClient()
    client.show()
    app.exec_()

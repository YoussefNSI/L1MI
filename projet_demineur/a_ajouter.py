import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.contre_ia = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        button1 = QPushButton('Jouer contre un humain', self)
        button1.clicked.connect(lambda: self.set_contre_ia(False))
        layout.addWidget(button1)

        button2 = QPushButton('Jouer contre une IA', self)
        button2.clicked.connect(lambda: self.set_contre_ia(True))
        layout.addWidget(button2)

        self.setLayout(layout)

    def set_contre_ia(self, value):
        self.contre_ia = value
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())

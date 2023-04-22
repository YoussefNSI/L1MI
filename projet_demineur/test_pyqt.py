import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un QLabel avec du texte
        label = QLabel('Bonjour, PyQt5!', self)

        # Positionner le QLabel dans la fenêtre
        label.move(50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

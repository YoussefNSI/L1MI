import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MineSweeper(QWidget):
    def __init__(self, rows, cols, num_mines):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.minefield = [[0 for j in range(cols)] for i in range(rows)]
        self.buttons = [[QPushButton() for j in range(cols)] for i in range(rows)]
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        for i in range(self.rows):
            for j in range(self.cols):
                button = self.buttons[i][j]
                button.setFixedSize(20, 20)
                button.clicked.connect(lambda _, i=i, j=j: self.buttonClicked(i, j))
                layout.addWidget(button, i, j)
        self.setLayout(layout)

        self.placeMines()
        self.updateCounts()

    def placeMines(self):
        mines = 0
        while mines < self.num_mines:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.cols - 1)
            if self.minefield[i][j] == 0:
                self.minefield[i][j] = -1
                mines += 1

    def updateCounts(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.minefield[i][j] == -1:
                    continue
                count = 0
                for ii in range(max(0, i - 1), min(self.rows, i + 2)):
                    for jj in range(max(0, j - 1), min(self.cols, j + 2)):
                        if self.minefield[ii][jj] == -1:
                            count += 1
                self.minefield[i][j] = count

    def buttonClicked(self, i, j):
        button = self.buttons[i][j]
        if self.minefield[i][j] == -1:
            button.setText("*")
            self.showGameOver()
        else:
            count = self.minefield[i][j]
            if count == 0:
                button.setText("")
                self.revealEmpty(i, j)
            else:
                button.setText(str(count))

    def revealEmpty(self, i, j):
        for ii in range(max(0, i - 1), min(self.rows, i + 2)):
            for jj in range(max(0, j - 1), min(self.cols, j + 2)):
                button = self.buttons[ii][jj]
                if button.text() == "":
                    continue
                count = self.minefield[ii][jj]
                if count == 0:
                    button.setText("")
                    self.revealEmpty(ii, jj)
                else:
                    button.setText(str(count))

    def showGameOver(self):
        messageBox = QMessageBox()
        messageBox.setText("Game Over")
        messageBox.exec

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MineSweeper")
        self.centralWidget = MineSweeper(10, 10, 10)
        self.setCentralWidget(self.centralWidget)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")

        newGameAction = fileMenu.addAction("New Game")
        newGameAction.triggered.connect(self.newGame)

    def newGame(self):
        self.centralWidget.deleteLater()
        self.centralWidget = MineSweeper(10, 10, 10)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

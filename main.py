from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
from random import randint
from gui import Ui_MainWindow

class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushed)
        self.counter = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.counter > 0:
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x, y, r = randint(50, 300), randint(50, 300), randint(50, 300)
            qp.drawEllipse(x, y, r, r)
        qp.end()

    def pushed(self):
        self.counter += 1
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
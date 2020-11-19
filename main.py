from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
from random import randint

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui.ui', self) 
        self.show()
        self.pushButton.clicked.connect(self.pushed)
        self.counter = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.counter > 0:
            qp.setBrush(QColor(255, 255, 0))
            x, y, r = randint(50, 300), randint(50, 300), randint(50, 300)
            qp.drawEllipse(x, y, r, r)
        qp.end()

    def pushed(self):
        self.counter += 1
        self.repaint()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_() 
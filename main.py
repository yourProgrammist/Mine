import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def run(self, qp):
        x = random.choice(range(50, 400))
        y = random.choice(range(50, 400))
        a = random.choice(range(10, 250))
        qp.setBrush(QColor(255, 225, 0))
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

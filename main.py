import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow
import random
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(random.choice(range(0, 256)), random.choice(range(0, 256)), random.choice(range(0, 256))))
        qp.drawEllipse(x, y, a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

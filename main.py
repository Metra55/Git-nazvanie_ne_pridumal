import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.mikhail_button.clicked.connect(self.run)

        self.risovat=False

    def paintEvent(self, event) -> None:
        if not self.risovat:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_cir(qp)

    def draw_cir(self, qp):
        qp.setBrush(QColor('yellow'))
        start = random.randint(0, 250)

        rad = random.randint(0, 250)
        qp.drawEllipse(start, start, start + rad, start + rad)

    def run(self):
        self.risovat=True
        self.update()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

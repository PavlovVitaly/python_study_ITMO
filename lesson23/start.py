# PyQt
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton
)


class Start(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._increment = True
        self._initUi()
        self._initSignals()

    def _initUi(self):
        self.resize(400, 300)
        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 400)
        self.btn = QPushButton('Butt', self)
        self.setCentralWidget(self.btn)

    def onClick(self):
        """Слот"""
        if self._increment:
            self.resize(self.width() + 10,
                        self.height() + 10)
        else:
            self.resize(self.width() - 10,
                        self.height() - 10)

        if self.width() <= self.minimumWidth():
            self._increment = True

        if self.width() >= self.maximumWidth():
            self._increment = False

    def _initSignals(self):
        self.btn.clicked.connect(self.onClick)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Start()
    w.show()
    sys.exit(app.exec_())

import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class ThreadTest(QThread):
    def __init__(self, parent):
        super().__init__(parent)

    def run(self):
        for i in range(20):
            print(i)
            time.sleep(1)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        threadStart = QPushButton("start")
        threadStart.clicked.connect(self.testFor)
        vbox = QVBoxLayout()
        vbox.addWidget(threadStart)

        self.resize(300,300)
        self.setLayout(vbox)

    def testFor(self):
        thread1 = ThreadTest(self)
        thread1.start()

    #     for i in range(10):
    #         print(i)
    #         time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

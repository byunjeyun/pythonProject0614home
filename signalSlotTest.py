import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SignalThread(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(100, 200)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        signalThr = SignalThread()

        signalThr.signal1.connect(self.signal1_print)
        signalThr.signal2.connect(self.signal2_print)
        signalThr.run()

    @pyqtSlot()
    def signal1_print(self):
        print("signal1 emit!!")

    @pyqtSlot(int, int)
    def signal2_print(self, arg1, arg2):
        print("signal2 emit!!", arg1, arg2)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("D:/1byunz/pythonProject0614home/ui/img_test.ui")[0]

class TestWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.img1_btn.clicked.connect(self.outputImg1)
        self.img2_btn.clicked.connect(self.outputImg2)
        self.img3_btn.clicked.connect(self.outputImg3)

    def outputImg1(self):
        pic1=QPixmap("/img/sun.png")
        self.img_label.setPixmap(QPixmap(pic1))
    def outputImg2(self):
        pic2=QPixmap("/img/cloud.png")
        self.img_label.setPixmap(QPixmap(pic2))
    def outputImg3(self):
        pic3=QPixmap("/img/windrain.png")
        self.img_label.setPixmap(QPixmap(pic3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWindow()
    ex.show()
    sys.exit(app.exec_())
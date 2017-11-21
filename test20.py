#coding: utf8
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        vbox=QtGui.QVBoxLayout()
        btn=QtGui.QPushButton('Dialog',self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        # btn.move(20,20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lb1=QtGui.QLabel('Knowledge only matters',self)
        # self.lb1.move(130,20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font,ok=QtGui.QFontDialog.getFont()
        if ok:
            self.lb1.setFont(font)

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
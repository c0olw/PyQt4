#coding: utf-8
import sys
from PyQt4 import QtGui

# def main():
#
#     app=QtGui.QApplication(sys.argv)
#
#     w=QtGui.QWidget()
#     w.resize(250,150)
#     w.move(300,300)
#     w.setWindowTitle('simple')
#     w.show()
#
#     sys.exit(app.exec_())

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('a.jpg'))

        self.show()

def main():

    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

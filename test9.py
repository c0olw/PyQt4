#coding: utf8
import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):

        textEdit=QtGui.QTextEdit()
        self.setCentralWidget(textEdit)
        """
        这里我们创建了一个文本编辑框(text edit)部件。
        我们把它设置成QtGui.QMainWindow的中央部件，
        中央部件占据了各种栏之外所有的剩余空间。 
        """

        exitAction=QtGui.QAction(QtGui.QIcon('d.jpg'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Main window')
        self.show()

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
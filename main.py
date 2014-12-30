import sys
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import re

#Convert ui to Class
principal_ui = uic.loadUiType('principal.ui')[0]


class VentanaPrincipal(QtGui.QMainWindow, principal_ui):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.frame.move((screen.width()-self.frame.geometry().width())/2, (screen.height()-self.frame.geometry().height())/2)
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    principal = VentanaPrincipal()
    principal.showMaximized()
    sys.exit(app.exec_())




 

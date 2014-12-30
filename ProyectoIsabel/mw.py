# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Nov 23 22:19:20 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName(_fromUtf8("mainwindow"))
        mainwindow.resize(706, 430)
        mainwindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        mainwindow.setWindowOpacity(0.8)
        self.centralwidget = QtGui.QWidget(mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 90, 431, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_titulo = QtGui.QLabel(self.verticalLayoutWidget)
        self.lbl_titulo.setEnabled(True)
        self.lbl_titulo.setStyleSheet(_fromUtf8("\n"
"font: 24pt \"Sans Serif\";"))
        self.lbl_titulo.setTextFormat(QtCore.Qt.RichText)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName(_fromUtf8("lbl_titulo"))
        self.verticalLayout.addWidget(self.lbl_titulo)
        self.btn_1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.verticalLayout.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.verticalLayout.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.verticalLayout.addWidget(self.btn_3)
        self.btn_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.verticalLayout.addWidget(self.btn_4)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(_translate("mainwindow", "Inventario", None))
        self.lbl_titulo.setText(_translate("mainwindow", "Inventario de biblioteca", None))
        self.btn_1.setText(_translate("mainwindow", "Inventario", None))
        self.btn_2.setText(_translate("mainwindow", "Busqueda", None))
        self.btn_3.setText(_translate("mainwindow", "Modificar", None))
        self.btn_4.setText(_translate("mainwindow", "Eliminar", None))


import sys
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import re
from Cliente import *
from Conexion import *
#Convert ui to Class
principal_ui = uic.loadUiType('principal.ui')[0]
cliente_ui = uic.loadUiType('cliente.ui')[0]

class VentanaCliente(QtGui.QDialog, cliente_ui):
  cliente = Cliente()
  selected_index = -1 
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)
    self.tb_clientes.clicked.connect(self.elegir_click)
    self.tb_clientes.doubleClicked.connect(self.elegir_dobleclick)
    self.buscar()
  def elegir_click(self):
    selected = self.tabla_datos.selectedIndexes()
    for select in selected:
      self.selected_index = select.row()
     
  def elegir_dobleclick(self):
    selected = self.tabla_datos.selectedIndexes()
    for select in selected:
      self.selected_index = select.row()

  def guardar(self):
    self.cliente.nombre = str(self.txt_nombre.text())
    self.cliente.apellido = str(self.txt_apellido.text())
    self.cliente.direccion = str(self.txt_direccion.text())
    self.cliente.telefono = str(self.txt_telefono.text())
    self.cliente.mail = str(self.txt_mail.text())
    var_time = self.txt_nacimiento.date()
    self.cliente.nacimiento = var_time.toPyDate()
    self.cliente.guardar()

  def buscar(self):
    model = QStandardItemModel()
    model.setColumnCount(6)
    model.setHorizontalHeaderLabels(self.cliente.headernames)
    for cliente_o in self.cliente.consultar_todos():
      li = [cliente_o.nombre, cliente_o.apellido, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail]
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
      model.appendRow(row)
    self.tb_clientes.setModel(model)



class VentanaPrincipal(QtGui.QMainWindow, principal_ui):
  def __init__(self,parent=None):
    QtGui.QMainWindow.__init__(self,parent)
    self.setupUi(self)
    screen = QtGui.QDesktopWidget().screenGeometry()
    self.frame.move((screen.width()-self.frame.geometry().width())/2, (screen.height()-self.frame.geometry().height())/2)
    self.inicializar()

  def inicializar(self):
    self.action_cliente.triggered.connect(self.Abrir_cliente)

  def Abrir_cliente(self):
    cliente = VentanaCliente()
    cliente.exec_()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    principal = VentanaPrincipal()
    principal.showMaximized()
    sys.exit(app.exec_())




 

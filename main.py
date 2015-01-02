import sys
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import re
from Cliente import *
from Conexion import *
from Producto import *
from Detalle import *
from Factura import *
from Modo import *
#Convert ui to Class
principal_ui = uic.loadUiType('principal.ui')[0]
cliente_ui = uic.loadUiType('cliente.ui')[0]
producto_ui = uic.loadUiType('producto.ui')[0]
factura_ui = uic.loadUiType('factura.ui')[0]
detalle_ui = uic.loadUiType('detalle.ui')[0]

class VentanaDetalle(QtGui.QDialog, detalle_ui):
  detalle = Detalle()
  producto = Producto()

  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()
  
  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)
    productos = self.producto.consultar_todos()
    print len(productos)
    for p in productos:
      self.cbo_producto.addItem(p.nombre,p.id)
    pass

  def guardar(self):
    self.detalle.producto.id = (self.cbo_producto.currentIndex()+1)
    self.detalle.cantidad = str(self.txt_cantidad.text())
    self.detalle.descuento = str(self.txt_descuento.text())
    self.detalle.producto.consultar()
    self.close()

class VentanaFactura(QtGui.QDialog, factura_ui):
  factura = Factura()
  detalles = []
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_agregar.clicked.connect(self.agregar)
    cliente = Cliente()
    modo = Modo()
    for p in cliente.consultar_todos():
      self.cbo_cliente.addItem(p.nombre,p.id)
    for p in modo.consultar_todos():
      self.cbo_modo.addItem(p.nombre,p.id)
 
     
  def agregar(self):
    detalle = VentanaDetalle()
    detalle.exec_()
    d = detalle.detalle
    self.detalles.append(d)
    d = None
    print d
    detalle = None
    self.actualizar()
   
  def actualizar(self):
    model = QStandardItemModel()
    model.setColumnCount(3)
    model.setHorizontalHeaderLabels(Detalle.headernames)
    for d in self.detalles:
      li = [d.producto.nombre, d.cantidad, d.descuento]
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
      model.appendRow(row)
    self.tb_detalles.setModel(model)




class VentanaProducto(QtGui.QDialog, producto_ui):
  producto = Producto()
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)


  def guardar(self):
    self.producto.nombre = str(self.txt_nombre.text())
    self.producto.precio = str(self.txt_precio.text())
    self.producto.stock = str(self.txt_stock.text())
    self.producto.guardar()



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
    self.cliente.cedula = str(self.txt_cedula.text())
    var_time = self.txt_nacimiento.date()
    self.cliente.nacimiento = var_time.toPyDate()
    self.cliente.guardar()

  def buscar(self):
    model = QStandardItemModel()
    model.setColumnCount(6)
    model.setHorizontalHeaderLabels(self.cliente.headernames)
    for cliente_o in self.cliente.consultar_todos():
      li = [cliente_o.nombre, cliente_o.apellido,cliente_o.cedula, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail]
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
    self.action_producto.triggered.connect(self.Abrir_producto)
    self.action_factura.triggered.connect(self.Abrir_factura)

  def Abrir_factura(self):
    factura = VentanaFactura()
    factura.exec_()

  def Abrir_producto(self):
    producto = VentanaProducto()
    producto.exec_()

  def Abrir_cliente(self):
    cliente = VentanaCliente()
    cliente.exec_()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    principal = VentanaPrincipal()
    principal.showMaximized()
    sys.exit(app.exec_())




 

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
  selected_index = -1 
  productos = []

  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)
    self.btn_eliminar_todo.clicked.connect(self.borrarTodo)
    self.btn_eliminar_selec.clicked.connect(self.borrarSelec)
    self.btn_buscar.clicked.connect(self.buscar)
    self.cargarProductos()


  def guardar(self):
    try:
      if self.validarDatos():
        self.producto.id = str(self.txt_codigo.text())
        self.producto.descripcion = str(self.txt_descripcion.text())
        self.producto.cantidad = str(self.txt_cantXunidad.text())
        self.producto.precioUnit = str(self.txt_precioVenta.text())
        self.producto.precioC = str(self.txt_precioCompra.text())
        self.producto.precioV = str(self.txt_precioImpuesto.text())
        self.producto.existentes = str(self.txt_uniExistencia.text())
        self.producto.pedidos = str(self.txt_uniPedido.text())
        var_time = self.txt_fecha.date()
        self.producto.fecha = var_time.toPyDate()
        self.producto.comentario = str(self.txt_comentario.toPlainText())
        self.producto.guardar()
        self.cargarProductos()
        self.limpiar()
        QMessageBox.about(self,"Correcto","Producto guardado con exito")
      else:
        QMessageBox.about(self,"Error","Ingrese datos correctos")
    except:
      QMessageBox.about(self,"Error","Ingrese un nuevo Codigo")
 

  def validarDatos(self):
    try:
      codigo = str(self.txt_codigo.text())
      precioCompra = str(self.txt_precioCompra.text())
      precioVenta = str(self.txt_precioVenta.text())
      precioImpuesto = str(self.txt_precioImpuesto.text())
      uniExistencia = str(self.txt_uniExistencia.text()) 
      uniPedido =  str(self.txt_uniPedido.text())
      
      if len(precioCompra)>0:
        tmp = precioCompra.split('.')
	if len(tmp) == 2:
	  if tmp[0].isdigit() == False or tmp[1].isdigit() == False:
            return False
	elif len(tmp) == 1:
          if tmp[0].isdigit() == False:
            return False
        else:
          return False
      
      if len(precioCompra)==0:
        return False

      if len(codigo)<1 or codigo.isdigit() == False  or len(str(self.txt_descripcion.text()))<1:
        print ' tres pimeros'
	return False
          
      
      if len(precioVenta)>0:
        tmp = precioVenta.split('.')
	if len(tmp) == 2:
	  if tmp[0].isdigit() == False or tmp[1].isdigit() == False:
            return False
	elif len(tmp) == 1:
          if tmp[0].isdigit() == False:
            return False
        else:
          return False
      
      if len(precioImpuesto)>0:
        tmp = precioImpuesto.split('.')
	if len(tmp) == 2:
	  if tmp[0].isdigit() == False or tmp[1].isdigit() == False:
            return False
	elif len(tmp) == 1:
          if tmp[0].isdigit() == False:
            return False
        else:
          return False

      if len(uniExistencia)>0:
        tmp = uniExistencia.split('.')
	if len(tmp) == 2:
	  if tmp[0].isdigit() == False or tmp[1].isdigit() == False:
            return False
	elif len(tmp) == 1:
          if tmp[0].isdigit() == False:
            return False
        else:
          return False

      if len(uniPedido)>0:
        tmp = uniPedido.split('.')
	if len(tmp) == 2:
	  if tmp[0].isdigit() == False or tmp[1].isdigit() == False:
            return False
	elif len(tmp) == 1:
          if tmp[0].isdigit() == False:
            return False
        else:
          return False
    except:
      return False
    
    return True

  
  def borrarTodo(self):
    try:
      rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
      if rst == QMessageBox.Ok:
        self.producto.borrarProductos()
	QMessageBox.about(self,"Correcto", "Se ha eliminado todos los Clientes")
    except:
      QMessageBox.about(self,"Error", "Problemas con la base de datos")
    self.cargarProductos()

  def borrarSelec(self):
    try:
      selected = self.tb_productos_eliminar.selectedIndexes()
      self.selected_index = selected.__getitem__(0)
      select = self.productos[self.selected_index.row()]
      self.producto.id = select[0]
      
      rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
      if rst == QMessageBox.Ok:
        self.producto.borrarProducto()
        QMessageBox.about(self,"Correcto", "Se ha eliminado al Cliente")
    except:
      QMessageBox.about(self,"Error", "Problemas con la base de datos")
    self.cargarProductos()

  def limpiar(self):
    self.txt_codigo.setText('')
    self.txt_descripcion.setText('')
    self.txt_cantXunidad.setText('')
    self.txt_precioCompra.setText('')
    self.txt_precioVenta.setText('')
    self.txt_precioImpuesto.setText('')
    self.txt_uniExistencia.setText('')
    self.txt_uniPedido.setText('')
    self.txt_comentario.setPlainText('')

  def buscar(self):
    
    atribute= (str(self.txt_buscar.text())).strip()
    name=''
    print atribute   
    if atribute != '':
      if self.radioButton_codigo.isChecked():
        name= 'id'
        self.cargarBusqueda(atribute,name)
      elif self.radioButton_descripcion.isChecked():
        name= 'descripcion'
        self.cargarBusqueda(atribute,name)
      else:
        self.cargarProductos()
    elif self.radioButton_fecha.isChecked():
        name= 'fecha'
        desde = self.txt_desde.date()
        hasta = self.txt_hasta.date()
        self.cargarBusquedaFecha(str(desde.toPyDate),str(hasta.toPyDate),name)
    else: 
      self.cargarProductos()
  
  def cargarBusquedaFecha(self,desde,hasta,name):
    self.productos = []
    tmp =[]
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.producto.headernames)
    for producto_o in self.producto.consultar_By_Date(desde,hasta,name):
      
      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_productos.setModel(model)
    self.producto.id = 0



  def cargarBusqueda(self,atribute,name):
    self.productos = []
    tmp =[]
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.producto.headernames)
    for producto_o in self.producto.consultar_By_Atribute(atribute,name):
      
      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_productos.setModel(model)
    self.producto.id = 0



  def cargarProductos(self):
    self.productos = []
    tmp =[]
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.producto.headernames)
    for producto_o in self.producto.consultar_todos():
      
      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_productos.setModel(model)
    self.tb_productos_eliminar.setModel(model)
    self.producto.id = 0


class VentanaCliente(QtGui.QDialog, cliente_ui):
  cliente = Cliente()
  selected_index = -1 
  clientes = []
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)
    self.btn_eliminar_todo.clicked.connect(self.borrarTodo)
    self.btn_eliminar_selec.clicked.connect(self.borrarSelec)
    self.btn_buscar.clicked.connect(self.buscar)
    #self.tb_clientes.clicked.connect(self.elegir_click)
    self.tb_clientes.doubleClicked.connect(self.elegir_dobleclick)
    #self.buscar()
    self.cargarClientes()

  #def elegir_click(self):
    #selected = self.tb_clientes.selectedIndexes()
    #for select in selected:
      #self.selected_index = select.row()
      #print str(self.selected_index)
     
  def elegir_dobleclick(self):
    selected = self.tb_clientes.selectedIndexes()
    self.selected_index = selected.__getitem__(0)
    select = self.clientes[self.selected_index.row()]
    self.tabWidget.setCurrentWidget(self.tab_1)
    
    self.cliente.id = select[7]
    self.txt_nombre.setText(select[0])
    self.txt_apellido.setText(select[1])
    self.txt_direccion.setText(select[3])
    self.txt_telefono.setText(select[5])
    self.txt_mail.setText(select[6])
    self.txt_cedula.setText(select[2])
    self.txt_nacimiento.setDateTime(QtCore.QDateTime(select[4]))
    #for select in selected:
      #self.selected_index = select.row()
      #print self.selected_index

  def borrarTodo(self):
    try:
      rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
      if rst == QMessageBox.Ok:
        self.cliente.borrarClientes()
	QMessageBox.about(self,"Correcto", "Se ha eliminado todos los Clientes")
    except:
      QMessageBox.about(self,"Error", "Problemas con la base de datos")
    self.cargarClientes()

  def borrarSelec(self):
    try:
      selected = self.tb_clientes_eliminar.selectedIndexes()
      self.selected_index = selected.__getitem__(0)
      select = self.clientes[self.selected_index.row()]
      self.cliente.id = select[7]
      
      rst=QMessageBox.warning(self,"Alerta","Esta seguro que desea eliminar", QMessageBox.Cancel, QMessageBox.Ok)
      if rst == QMessageBox.Ok:
        self.cliente.borrarCliente()
        QMessageBox.about(self,"Correcto", "Se ha eliminado al Cliente")
    except:
      QMessageBox.about(self,"Error", "Problemas con la base de datos")
    self.cargarClientes()


  def guardar(self):
    if self.validarDatos():
      self.cliente.nombre = str(self.txt_nombre.text())
      self.cliente.apellido = str(self.txt_apellido.text())
      self.cliente.direccion = str(self.txt_direccion.text())
      self.cliente.telefono = str(self.txt_telefono.text())
      self.cliente.mail = str(self.txt_mail.text())
      self.cliente.cedula = str(self.txt_cedula.text())
      var_time = self.txt_nacimiento.date()
      self.cliente.nacimiento = var_time.toPyDate()
      self.cliente.guardar()
      self.cargarClientes()
      self.limpiar()
      QMessageBox.about(self,"Correcto","Cliente guardado con exito")
    else:
      QMessageBox.about(self,"Error","Ingrese datos correctos")
    

  def validarDatos(self):
    try:
      if len(str(self.txt_nombre.text()))<1 or len(str(self.txt_apellido.text()))<1 or (str(self.txt_cedula.text())).isdigit()==False:
        return False
    except:
      return False
    
    return True
  
  def limpiar(self):
    self.txt_nombre.setText('')
    self.txt_apellido.setText('')
    self.txt_direccion.setText('')
    self.txt_telefono.setText('')
    self.txt_mail.setText('')
    self.txt_cedula.setText('')
    

  def buscar(self):
    
    atribute= (str(self.txt_buscar.text())).strip()
    name=''
    print atribute   
    if atribute != '':
      if self.radioButton_nombre.isChecked():
        name= 'nombre'
        print 'nombre = entro'
        self.cargarBusqueda(atribute,name)
      elif self.radioButton_apellido.isChecked():
        name= 'apellido'
        self.cargarBusqueda(atribute,name)
      elif self.radioButton_cedula.isChecked():
        name= 'cedula'
        self.cargarBusqueda(atribute,name)
      else:
        self.cargarClientes()
    else: 
      self.cargarClientes()
    
  def cargarBusqueda(self,atribute,name):
    self.clientes = []
    tmp =[]
    
    model = QStandardItemModel()
    model.setColumnCount(7)
    model.setHorizontalHeaderLabels(self.cliente.headernames)
    for cliente_o in self.cliente.consultar_By_Atribute(atribute,name):
      li = [cliente_o.nombre, cliente_o.apellido,cliente_o.cedula, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail]
      tmp= [cliente_o.nombre, cliente_o.apellido,cliente_o.cedula, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail,cliente_o.id]
      self.clientes.append(tmp)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
      model.appendRow(row)
    self.tb_clientes.setModel(model)
    self.cliente.id = 0
 
  def cargarClientes(self):
    self.clientes = []
    tmp =[]
    model = QStandardItemModel()
    model.setColumnCount(7)
    model.setHorizontalHeaderLabels(self.cliente.headernames)
    for cliente_o in self.cliente.consultar_todos():
      
      li = [cliente_o.nombre, cliente_o.apellido,cliente_o.cedula, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail]
      tmp= [cliente_o.nombre, cliente_o.apellido,cliente_o.cedula, cliente_o.direccion,cliente_o.nacimiento,cliente_o.telefono,cliente_o.mail,cliente_o.id]
      self.clientes.append(tmp)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_clientes.setModel(model)
    self.tb_clientes_eliminar.setModel(model)
    self.cliente.id = 0




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




 

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
from Reporte import *

#Convert ui to Class
principal_ui = uic.loadUiType('principal.ui')[0]
cliente_ui = uic.loadUiType('cliente.ui')[0]
producto_ui = uic.loadUiType('producto.ui')[0]
factura_ui = uic.loadUiType('factura.ui')[0]
detalle_ui = uic.loadUiType('detalle.ui')[0]
reporte_ui = uic.loadUiType('reporte.ui')[0]

class VentanaDetalle(QtGui.QDialog, detalle_ui):
  detalle = Detalle()
  producto = Producto()

  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.detalle = Detalle()
    self.producto = Producto()
    self.inicializar()
  
  def inicializar(self):
    self.btn_guardar.clicked.connect(self.guardar)
    productos = self.producto.consultar_todos()
    for p in productos:
      self.cbo_producto.addItem(p.descripcion,p.id)

  def guardar(self):
    self.detalle.producto.id = (self.cbo_producto.currentIndex()+1)
    cantidad =  str(self.txt_cantidad.text())
    self.detalle.cantidad = cantidad if len(cantidad)>0 else 0
    descuento = str(self.txt_descuento.text())
    self.detalle.descuento = descuento if len(descuento)>0 else 0
    self.close()

class VentanaFactura(QtGui.QDialog, factura_ui):
  factura = Factura()
  detalles = []
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.factura = Factura()
    self.detalles = []
    self.inicializar()
    self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent)
    self.cbo_cliente.currentIndexChanged.connect(self.cambio_cliente)
    print 'd'

  def cambio_cliente(self):
    id = (self.cbo_cliente.itemData(self.cbo_cliente.currentIndex())).toInt()
    print id[0]
    cliente = Cliente()
    cliente.id =id[0]
    cliente.consultar()
    self.txt_cedula.setText( cliente.cedula)
    self.txt_direccion.setText(cliente.direccion)

  def closeEvent(self, event):
    print "Closing"

  def inicializar(self):
    self.btn_agregar.clicked.connect(self.agregar)
    self.btn_guardar.clicked.connect(self.guardar)
    cliente = Cliente()
    modo = Modo()
    for p in cliente.consultar_todos():
      self.cbo_cliente.addItem(p.nombre,p.id)
    for p in modo.consultar_todos():
      self.cbo_modo.addItem(p.nombre,p.id)
    self.cambio_cliente()
 
  def guardar(self):
    self.factura.modo.id  = (self.cbo_modo.currentIndex()+1)
    self.factura.cliente.id = (self.cbo_cliente.currentIndex()+1)
    self.factura.detalles = self.detalles
    var_time = self.date_fecha.date()
    self.factura.fecha = var_time.toPyDate()
    self.factura.guardar()


  def agregar(self):
    detalle = VentanaDetalle()
    detalle.exec_()
    d = Detalle()
    d.producto = Producto()
    d.producto.id = detalle.detalle.producto.id
    d.cantidad = detalle.detalle.cantidad
    d.descuento = detalle.detalle.descuento
    d.producto.consultar()
    self.detalles.append(d)
    self.actualizar()
   
  def actualizar(self):
    total = 0
    dcto = 0
    model = QStandardItemModel()
    model.setColumnCount(6)
    headernames = ['Codigo','Producto','Precio', 'Cantidad','Descuento','Total']
    model.setHorizontalHeaderLabels(headernames)
    for d in self.detalles:
      li = [d.producto.codigo, d.producto.descripcion, d.producto.precioUnit, d.cantidad, d.descuento, (float(d.producto.precioUnit)*float(d.cantidad)) -float(d.descuento)]
      print d.producto.precioV
      print d.cantidad
      print d.descuento
      if d.producto.precioV is None:
        d.producto.precioV = d.producto.precioUnit
      total = total + (float(d.producto.precioV)*float(d.cantidad)) - float(d.descuento)
      dcto = dcto + float(d.descuento)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
      model.appendRow(row)
    self.tb_detalles.setModel(model)
    iva = (total * 12) / 100
    self.txt_iva.setText(str(iva))
    self.txt_total.setText(str(total+iva))
    self.txt_dscto.setText(str(dcto))
   


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
    self.btn_limpiar.clicked.connect(self.limpiar)
    self.btn_eliminar_todo.clicked.connect(self.borrarTodo)
    self.btn_eliminar_selec.clicked.connect(self.borrarSelec)
    self.tb_productos.doubleClicked.connect(self.elegir_dobleclick)
    self.btn_buscar.clicked.connect(self.buscar)
    self.cargarProductos()

  def elegir_dobleclick(self):
    selected = self.tb_productos.selectedIndexes()
    self.selected_index = selected.__getitem__(0)
    select = self.productos[self.selected_index.row()]
    self.tabWidget.setCurrentWidget(self.tab_1)
    
    self.producto.id = select[0]
    self.txt_codigo.setText(str(select[0]))
    self.txt_descripcion.setText(str(select[1]))
    self.txt_cantXunidad.setText(str(select[2]))
    self.txt_precioCompra.setText(str(select[4]))
    self.txt_precioVenta.setText(str(select[3]))
    self.txt_precioImpuesto.setText(str(select[5]))
    self.txt_uniExistencia.setText(str(select[6]))
    self.txt_uniPedido.setText(str(select[7]))
    self.txt_comentario.setPlainText(str(select[9]))
    self.txt_fecha.setDateTime(QtCore.QDateTime(select[8]))


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
        self.cargarBusquedaFecha(str(desde.toPyDate()),str(hasta.toPyDate()),name)
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

class VentanaReporte(QtGui.QDialog, reporte_ui):
  
  reporte = Reporte()
  selected_index = -1 
  productos = []
  reportes = [0,0,0,0]
  
  def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.setupUi(self)
    self.inicializar()

  def inicializar(self):
    self.btn_generar_inventario.clicked.connect(self.buscarProducto)
    #self.btn_eliminar_todo.clicked.connect(self.borrarTodo)
    #self.btn_eliminar_selec.clicked.connect(self.borrarSelec)
    #self.btn_buscar.clicked.connect(self.buscar)
    #self.tb_clientes.clicked.connect(self.elegir_click)
    #self.tb_clientes.doubleClicked.connect(self.elegir_dobleclick)
    self.cargarProductos()
    
  def buscarProducto(self):
    
    atribute= (str(self.txt_buscar_inventario.text())).strip()
    name=''
    print atribute   
    if atribute != '':
      if self.radioButton_codigoInventario.isChecked():
        name= 'id'
        self.cargarBusquedaInventario(atribute,name)
      elif self.radioButton_descripcionInventario.isChecked():
        name= 'descripcion'
        self.cargarBusquedaInventario(atribute,name)
      else:
        self.cargarProductos()
    elif self.radioButton_fechaInventario.isChecked():
        name= 'fecha'
        desde = self.txt_inventario_desde.date()
        hasta = self.txt_inventario_hasta.date()
        self.cargarBusquedaFechaInventario(str(desde.toPyDate()),str(hasta.toPyDate()),name)
    else: 
      self.cargarProductos()
  
  def cargarBusquedaFechaInventario(self,desde,hasta,name):
    self.productos = []
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.reporte.headernames_producto)
    for producto_o in self.reporte.consultar_By_Date(desde,hasta,name):
      self.reportes[0] = self.reportes[0] + int(producto_o.cantidad)
      self.reportes[1] = self.reportes[1] + float(producto_o.precioUnit)
      self.reportes[2] = self.reportes[2] + float(producto_o.precioC)
      self.reportes[3] = self.reportes[3] + float(producto_o.precioV)

      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_inventario.setModel(model)
    self.cargarSumaInventario()
    self.reporte.id = 0



  def cargarBusquedaInventario(self,atribute,name):
    self.productos = []
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.reporte.headernames_producto)
    for producto_o in self.reporte.consultar_By_Atribute(atribute,name):
      
      self.reportes[0] = self.reportes[0] + int(producto_o.cantidad)
      self.reportes[1] = self.reportes[1] + float(producto_o.precioUnit)
      self.reportes[2] = self.reportes[2] + float(producto_o.precioC)
      self.reportes[3] = self.reportes[3] + float(producto_o.precioV)

      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_inventario.setModel(model)
    self.cargarSumaInventario()
    self.reporte.id = 0
 

  def cargarProductos(self):
    self.productos = []
    model = QStandardItemModel()
    model.setColumnCount(10)
    model.setHorizontalHeaderLabels(self.reporte.headernames_producto)
    for producto_o in self.reporte.consultar_productoTodos():
      self.reportes[0] = self.reportes[0] + int(producto_o.cantidad)
      self.reportes[1] = self.reportes[1] + float(producto_o.precioUnit)
      self.reportes[2] = self.reportes[2] + float(producto_o.precioC)
      self.reportes[3] = self.reportes[3] + float(producto_o.precioV)

      li = [producto_o.id, producto_o.descripcion,producto_o.cantidad, producto_o.precioUnit,producto_o.precioC,producto_o.precioV,producto_o.existentes,producto_o.pedidos,producto_o.fecha,producto_o.comentario]
      self.productos.append(li)
      row = []
      for name in li:
        item = QStandardItem(str(name))
        item.setEditable(False)
        row.append(item)
	
      model.appendRow(row)
    self.tb_inventario.setModel(model)
    self.cargarSumaInventario()
    self.reporte.id = 0

  def cargarSumaInventario(self):
    self.txt_cantidadTotal_2.setText(str(self.reportes[0]))
    self.txt_unidadTotal_2.setText(str(self.reportes[1]))
    self.txt_compraTotal_2.setText(str(self.reportes[2]))
    self.txt_ventaTotal_2.setText(str(self.reportes[3]))
    self.reportes = [0,0,0,0]

  def closeEvent(self, evnt):
    print 'holi'
    super(VentanaCliente, self).closeEvent(evnt)

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
    self.action_reporte.triggered.connect(self.Abrir_reporte)
  
  def Abrir_reporte(self):
    reporte = VentanaReporte()
    reporte.exec_()
  
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




 

from Conexion import *
from objeto import *
class Reporte(Objeto):
  
  #Factura
  descuento = 0
  pecioTotal = 0
  

  #Producto
  codigo = 0
  descripcion = ''
  cantidad = 0
  precioUnit = 0
  precioC = 0
  precioV = 0
  existentes = 0
  pedidos = 0
  fecha = ''
  comentario = ''
 
  headernames_producto = ['Codigo','Descripcion','Cantidad','Precio Unit','Precio C', 'Precio V', 'Existentes', 'Pedidos', 'Fecha','Comentario']
  headernames_venta = ['Codigo','Descripcion','Cantidad','Precio Unit','Descuento', 'Precio Total', 'Fecha']

  atributos = 'producto_id, producto_descripcion, \
              producto_cantidadUnidad, producto_precioVenta, \
	      producto_precioCompra, producto_precioImpuesto, \
	      producto_unidadExistente, producto_unidadPedida, \
	      producto_fecha, producto_comentario'
  tabla = ' producto'

  def __init__(self):
    self.inicializar()



  #FACTURA
  def consultar_ventaTodos(self):
    lista=[]
    query = 'SELECT p.producto_id, p.producto_descripcion, d.detalle_cantidad, p.producto_precioVenta, d.detalle_descuento, \
             f.factura_fecha, p.producto_precioCompra FROM Factura f INNER JOIN Detalle d ON d.detalle_factura = f.factura_id \
             INNER JOIN Producto p ON d.detalle_producto = p.producto_id ;'
 
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print result
    lista = self.enlistarVenta(result)
    print len(lista)
    cursor.close()
    print lista
    return lista

  def consultarVenta_By_Atribute(self,atribute):
    lista=[]
    query = 'SELECT p.producto_id, p.producto_descripcion, d.detalle_cantidad, p.producto_precioVenta, d.detalle_descuento, \
             f.factura_fecha, p.producto_precioCompra FROM Factura f INNER JOIN Detalle d ON d.detalle_factura = f.factura_id \
             INNER JOIN Producto p ON d.detalle_producto = p.producto_id WHERE f.factura_id = %s;'

    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(atribute,))
    result = cursor.fetchall()
    print result
    lista = self.enlistarVenta(result)
    print len(lista)
    cursor.close()
    print lista
    return lista


  def consultarVenta_By_Mode(self,atribute):
    lista=[]
    query = 'SELECT p.producto_id, p.producto_descripcion, d.detalle_cantidad, p.producto_precioVenta, d.detalle_descuento, \
             f.factura_fecha, p.producto_precioCompra FROM Factura f INNER JOIN Detalle d on f.factura_id=d.detalle_factura INNER JOIN \
             Producto p ON p.producto_id = d.detalle_producto INNER JOIN Modo ON modo_id = f.factura_modo WHERE modo_id = %s;'
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(atribute,))
    result = cursor.fetchall()
    print result
    lista = self.enlistarVenta(result)
    print len(lista)
    cursor.close()
    print lista
    return lista
  
  #aqui saco las facturas entre esas fechas y de ahi quiero sacar lo productos de esas facturas 
  def consultarVenta_By_Date(self,desde,hasta):
    lista=[]
    query = 'SELECT p.producto_id, p.producto_descripcion, d.detalle_cantidad, p.producto_precioVenta, d.detalle_descuento, \
             f.factura_fecha, p.producto_precioCompra FROM Factura f INNER JOIN Detalle d ON d.detalle_factura = f.factura_id \
             INNER JOIN Producto p ON d.detalle_producto = p.producto_id WHERE f.factura_fecha BETWEEN %s and %s ;'
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(desde,hasta))
    #cursor.execute(query,('2005-01-01','2009-01-01'))
    result = cursor.fetchall()
    print result
    lista = self.enlistarVenta(result)
    print len(lista)
    cursor.close()
    print lista
    return lista


  def enlistarVenta(self, listas):
    lista=[]
    for r in listas: 
      venta = Reporte()
      venta.mapearVentas(r)
      lista.append(venta)
    return lista

  def mapearVentas(self, datarow):
    print self.id
    print datarow
    self.codigo = datarow[0]
    self.descripcion = datarow[1]
    self.cantidad = datarow[2]
    self.precioUnit = datarow[3]
    self.descuento = datarow[4]
    self.precioTotal = datarow[2] * datarow[3]
    self.fecha = datarow[5]
    self.precioC = datarow[6]




  #PRODUCTO

  def consultar_productoTodos(self):
    #tabla = ' producto'
    #self.inicializar()
    lista=[]
    query = self.query_select_all
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print result
    lista = self.enlistarProducto(result)
    print len(lista)
    cursor.close()
    print lista
    return lista

  def consultar_By_Atribute(self,atribute,name):
    lista=[]
    query = self.query_search + name + self.query_search_end
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(atribute,))
    result = cursor.fetchall()
    print result
    lista = self.enlistarProducto(result)
    print len(lista)
    cursor.close()
    print lista
    return lista

  def consultar_By_Date(self,desde,hasta,name):
    lista=[]
    query = self.query_search_date + name + self.query_search_date_end
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(desde,hasta))
    #cursor.execute(query,('2005-01-01','2009-01-01'))
    result = cursor.fetchall()
    print result
    lista = self.enlistarProducto(result)
    print len(lista)
    cursor.close()
    print lista
    return lista


  def enlistarProducto(self, listas):
    lista=[]
    for r in listas: 
      producto = Reporte()
      producto.mapearProductos(r)
      lista.append(producto)
    return lista

  def mapearProductos(self, datarow):
    print self.id
    print datarow
    self.id = datarow[0]
    self.descripcion = datarow[1]
    self.cantidad = datarow[2]
    self.precioUnit = datarow[3]
    self.precioC = datarow[4]
    self.precioV = datarow[5]
    self.existentes = datarow[6]
    self.pedidos = datarow[7]
    self.fecha = datarow[8]
    self.comentario = datarow[9]

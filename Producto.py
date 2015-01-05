from Conexion import *
from objeto import *
class Producto(Objeto):
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
 
  headernames = ['Codigo','Descripcion','Cantidad','Precio Unit','Precio C', 'Precio V', 'Existentes', 'Pedidos', 'Fecha','Comentario']
  atributos = 'producto_id, producto_descripcion, \
              producto_cantidadUnidad, producto_precioVenta, \
	      producto_precioCompra, producto_precioImpuesto, \
	      producto_unidadExistente, producto_unidadPedida, \
	      producto_fecha, producto_comentario'
  tabla = ' producto'

  def __init__(self):
    self.inicializar()

  def guardar(self):
    consulta = 'SELECT * FROM Producto WHERE producto_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, (self.id,))
    if cursor.fetchone() is None:
      print 'query'
      query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.execute(query,(self.id,self.descripcion,str(self.cantidad),str(self.precioUnit),str(self.precioC),str(self.precioV),str(self.existentes),str(self.pedidos),str(self.fecha),self.comentario))
      conexion.commit()
      cursor.close()
      print query
    else:
      cursor.close()
      self.modificar() 
     
  def modificar(self):
    query = (self.query_update+' producto_descripcion = %s , \
        producto_cantidadUnidad = %s, producto_precioVenta = %s, \
	producto_precioCompra = %s, producto_precioImpuesto = %s, \
	producto_unidadExistente = %s, producto_unidadPedida = %s, \
	producto_fecha = %s, producto_comentario = %s'+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.descripcion,str(self.cantidad),str(self.precioUnit),str(self.precioC),str(self.precioV),str(self.existentes),str(self.pedidos),str(self.fecha),self.comentario,self.id))
    conexion.commit()
    cursor.close()

  def borrarProductos(self):
    self.eliminar_todo()  
 
  def borrarProducto(self):
    self.eliminar()  

  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      producto = Producto()
      producto.mapeardatos(r)
      lista.append(producto)
    return lista

  def mapeardatos(self, datarow):
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

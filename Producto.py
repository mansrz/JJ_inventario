from Conexion import *
from objeto import *
class Producto(Objeto):
  nombre = ''
  precio = 0
  stock = 0
  headernames = ['Nombre','Precio','Stock']
  atributos = 'producto_id, producto_nombre, \
              producto_precio, producto_stock'
  tabla = ' producto'

  def __init__(self):
    self.inicializar()

  def guardar(self):
    query = self.query_insert + ' %s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.nombre,self.precio,self.stock ))
    conexion.commit()
    cursor.close()
    print query

  def modificar(self):
    query = (self.query_update+' producto_nombre = %s , \
        producto_precio = %s, producto_stock =%s'+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.precio,self.stock,self.id))
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      producto = Producto()
      producto.mapeardatos(r)
      lista.append(producto)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.precio = datarow[2]
    self.stock = datarow[3]


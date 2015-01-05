from Conexion import *
from objeto import *
from Factura import *
from Producto import * 
from Modo import *
class Detalle(Objeto):
  factura = 0
  producto = Producto()
  cantidad = 0
  descuento = 0
  headernames = ['Producto', 'Cantidad','Descuento']
  atributos = 'detalle_id,detalle_factura,detalle_producto\
              ,detalle_cantidad,detalle_descuento'
  tabla = ' detalle'

  def __init__(self):
    self.inicializar()

  def guardar(self):
    query = self.query_insert + '%s,%s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,self.factura,self.producto.id,self.cantidad,self.descuento))
    conexion.commit()
    cursor.close()
    print query

  def modificar(self):
    query = (self.query_update+' detalle_producto = %s , \
       detalle_cantidad =%s, detalle_descuento =%s  '+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.producto.id,self.cantidad,self.descuento,self.id))
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      detalle = Detalle()
      detalle.mapeardatos(r)
      lista.append(detalle)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.factura = datarow[1]
    self.producto.id = datarow[2]
    self.cantidad = datarow[3]
    self.descuento = datarow[4]
    self.producto.consultar()

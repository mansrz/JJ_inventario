from Conexion import *
from objeto import *
from Cliente import *
from Modo import *
class Factura(Objeto):
  cliente = Cliente()
  fecha = ''
  modo = Modo()
  transaccion = ''
  headernames = ['Cliente','Fecha','Modo','Transaccion']
  atributos = 'factura_id, factura_cliente, factura_fecha,\
              factura_modo, factura_transaccion'
  tabla = ' factura'

  def __init__(self):
    self.inicializar()

  def guardar(self):
    query = self.query_insert + ' %s,%s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.cliente.id,self.fecha,self.modo.id,self.transaccion))
    conexion.commit()
    cursor.close()
    print query

  def modificar(self):
    query = (self.query_update+' factura_cliente = %s , \
       factura_fecha = %s , factura_modo = %s ,\
      factura_transaccion = %s  '+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.cliente.id,self.fecha,self.modo.id,self.transaccion))
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      factura = Factura()
      factura.mapeardatos(r)
      lista.append(factura)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.cliente.id = datarow[1]
    self.fecha = datarow[2]
    self.modo.id = datarow[3]
    self.transaccion = datarow[4]
    self.cliente.consultar()
    self.modo.consultar()



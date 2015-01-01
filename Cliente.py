from Conexion import *
from objeto import * 
class Cliente(Objeto):
  nombre = ''
  apellido = ''
  direccion = ''
  nacimiento = ''
  telefono = ''
  mail = ''
  headernames = ['Nombre','Apellido','Direccion','Fecha de Nacimiento','Telefono','Mail']
  atributos = 'cliente_id, cliente_nombre, cliente_apellido, cliente_direccion, cliente_nacimiento,\
              cliente_telefono, cliente_mail '
  tabla = ' cliente'
  def __init__(self):
    self.inicializar()

  def cargar(self):
    pass
     #TODO
  def guardar(self):
    query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.nombre,self.apellido,self.direccion,str(self.nacimiento),self.telefono,self.mail))
    conexion.commit()
    cursor.close()
    print query

  def modificar(self):
    query = (self.query_update+' cliente_nombre = %s , cliente_apellido = %s\
        , cliente_direccion = %s , cliente_nacimiento = %s , cliente_telefono = %s , \
        cliente_mail = %s '+self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.apellido,self.direccion,str(self.nacimiento),self.telefono,self.mail,self.id))
    conexion.commit()
    cursor.close()


  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      cliente = Cliente()
      cliente.mapeardatos(r)
      lista.append(cliente)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.apellido = datarow[2]
    self.direccion = datarow[3]
    self.nacimiento = datarow[4]
    self.telefono = datarow[5]
    self.mail = datarow[6]
   

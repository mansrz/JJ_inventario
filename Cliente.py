from Conexion import *
from objeto import * 
class Cliente(Objeto):
  nombre = ''
  apellido = ''
  direccion = ''
  nacimiento = ''
  telefono = ''
  cedula = ''
  mail = ''
  headernames = ['Nombre','Apellido','Cedula','Direccion','Fecha de Nacimiento','Telefono','Mail']
  atributos = 'cliente_id, cliente_nombre, cliente_apellido, cliente_direccion, cliente_nacimiento,\
              cliente_telefono, cliente_mail,cliente_cedula '
  tabla = ' cliente'
  
  def __init__(self):
    self.inicializar()

  def cargar(self):
    pass
     #TODO

  def buscarByCI(self, cedula):
    query = 'SELECT * FROM clientes WHERE cliente_cedula = %s'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, self.cedula)
    result = cursor.fetchall()
    #conexion.commit()
    cursor.close()
    return result
     

  def guardar(self):
    consulta = 'SELECT * FROM Cliente WHERE cliente_id = %s ;'
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(consulta, (str(self.id),))
    if cursor.fetchone() is None:
      query = self.query_insert + ' %s,%s,%s,%s,%s,%s,%s,%s '+self.query_insert_end
      cursor.execute(query,(str(self.contar()),self.nombre,self.apellido,self.direccion,str(self.nacimiento),self.telefono,self.mail,self.cedula))
      conexion.commit()
      cursor.close()
      print query
    else:
      cursor.close()
      self.modificar()

  def borrarClientes(self):
    self.eliminar_todo()  
  
  def borrarCliente(self):
    self.eliminar()

  def modificar(self):
    query = (self.query_update+' `cliente_nombre` = %s , `cliente_apellido` = %s\
        , `cliente_direccion` = %s , `cliente_nacimiento` = %s , `cliente_telefono` = %s , \
        `cliente_mail` = %s, `cliente_cedula`= %s' + self.query_update_end)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    print self.nombre
    print self.apellido
    print self.id
    print self.telefono
    cursor.execute(query,(self.nombre,self.apellido,self.direccion,str(self.nacimiento),self.telefono,self.mail,self.cedula,self.id))
    conexion.commit()
    cursor.close()
    #COrrelo


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
    self.direccion = datarow[4]
    self.nacimiento = datarow[5]
    self.telefono = datarow[6]
    self.mail = datarow[7]
    self.cedula = datarow[3]

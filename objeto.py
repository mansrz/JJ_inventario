from Conexion import *
class Objeto():
  conexion = Conexion()
  tabla = ''
  id = 0
  atributos = ''
  query_insert = ''
  query_insert_end = ''
  query_update = ''
  query_update_end = ''
  query_delete = ''
  query_select_all = ''
  query_select_me = ''

  def inicializar(self):
    tabla = self.tabla
    atributos = self.atributos
    self.query_insert = 'INSERT INTO '+tabla.title()+' ('+atributos+') VALUES ('
    self.query_insert_end = ');'
    self.query_update = 'UPDATE '+tabla.title()+' SET '
    self.query_update_end = ' WHERE '+tabla+'_id= %s  ;'
    self.query_delete = 'DELETE FROM '+tabla.title()+ ' WHERE '+tabla+'_id = %s ;'
    self.query_select_all = 'SELECT * FROM '+ tabla.title() +' ;'
    self.query_select_me  = 'SELECT * FROM '+ tabla.title() +' WHERE '+tabla+'_id =%s ;'

  def contar(self):
    print (self.tabla.title())
    query = ('SELECT '+self.tabla+'_id from '+self.tabla.title()+' ORDER BY '+self.tabla+'_id DESC LIMIT 1;')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    if result is None:
      return 1
    return (result[0]+1)
 
  def __init__(self):
    pass
 
  def modificar(self):
    pass
  
  def consultar_todos(self):
    lista=[]
    query = self.query_select_all
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print result
    lista = self.enlistar(result)
    print len(lista)
    cursor.close()
    return lista

  def mapeardatos(self, datarow):
    pass
  def consultar(self):
    query = self.query_select_me
    print query
    conexion = self.conexion.getConnection()
    cursor = conexion.cursor()
    cursor.execute(query,(self.id,))
    result = cursor.fetchall()
    self.mapeardatos(result[0])
    cursor.close()
 
  def eliminar(self):
    query = self.query_delete 
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,))
    conexion.commit()
    cursor.close()
 

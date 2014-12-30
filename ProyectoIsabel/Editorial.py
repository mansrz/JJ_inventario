from conection import *
class Editorial():
  conexion = Conexion()
  id=''
  nombre=''
  pais=''
  def __init__(self):
    pass

  def recargar(self):
    query = ('SELECT * FROM proyecto_laboratorio.Editorial where editorial_id=%s')
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,))
    result=cursor.fetchall()
    for r in result: 
      self.nombre =r[1]
      self.pais =r[2]
    cursor.close()
    return result


  def guardar(self):
    query = ('INSERT INTO `Editorial`\
    (`editorial_nombre`,\
     `editorial_pais`) VALUES(%s,%s)')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.nombre,self.pais))
    conexion.commit()
    cursor.close()

    return 0

  def consultar(self):
    return 0

  def modificar(self):
    return 0

  def eliminar(self):
    return 0

  def mapeardatos(self, datarow):
    return 0

  def contar(self):
    query = ('SELECT editorial_id from proyecto_laboratorio.Editorial ORDER BY editorial_id DESC LIMIT 1;')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    print result[0]
    return (result[0]+1)
 
  def consultar_todos(self):
    query = ('SELECT * FROM proyecto_laboratorio.Editorial')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    for r in result:
      print r
    cursor.close()
    return result



  


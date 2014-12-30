from conection import *
class Cuenta():
  nick=''
  nombre=''
  conexion = Conexion()
  def crear(self):
    pass
  def eliminar(self):
    pass
  def modificar(self):
    pass

  def guardar(self):
    query = ('INSERT INTO `Cuenta`\
    (`cuenta_id`,`cuenta_nombre`,`cuenta_nick`,\
    `cuenta_pwd`) VALUES(%s,%s,%s,%s)')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.nombre,self.nick,self.pwd))
    conexion.commit()
    cursor.close()


  def contar(self):
    query = ('SELECT cuenta_id from proyecto_laboratorio.Cuenta ORDER BY cuenta_id DESC LIMIT 1;')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    print result[0]
    return (result[0]+1)
 
 

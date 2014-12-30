import datetime
from Editorial import *
from conection import*

class Libro():
  id=''
  titulo=''
  autor=''
  fecha=''
  numregistro=''
  clave=''
  volumen=''
  editorial= Editorial()
  edicion_anio=''
  procedencia=''
  conexion = Conexion()

  def __init__(self):
    pass

     #TODO
  def guardar(self):
    self.editorial.recargar()
    query = ('INSERT INTO `Libro`\
    (`libro_id`,`libro_titulo`,\
     `libro_autor`,`libro_fecha`,\
     `libro_numregistro`,`libro_clave`,\
     `libro_volumen`,`libro_editorial`,\
     `libro_edicion_anio`,`libro_procedencia`)\
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(str(self.contar()),self.titulo,self.autor,str(self.fecha),self.numregistro,self.clave,self.volumen,self.editorial.id,self.edicion_anio,self.procedencia))
    conexion.commit()
    cursor.close()


  def verificar(self):
    valido = False if ((len(self.titulo)<2) | (len(self.autor)<2) | (len(self.numregistro)<2) | (len(self.clave)<2) | (len(self.volumen)<2) | (len(self.edicion_anio)<2) | (len(self.procedencia)<2) ) else True 
    return valido

  def contar(self):
    query = ('SELECT libro_id from proyecto_laboratorio.Libro ORDER BY libro_id DESC LIMIT 1;')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    print result[0]
    return (result[0]+1)
        
  def consultar_todos(self, filtro):
    lista=[]
    print filtro
    query = ('SELECT * FROM proyecto_laboratorio.Libro '+filtro)
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    for r in result: 
      libro = Libro()
      libro.mapeardatos(r)
      lista.append(libro)

    cursor.close()
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.titulo = datarow[1]
    self.autor = datarow[2]
    self.numregistro = datarow[4]
    self.clave = datarow[5]
    self.volumen = datarow[6]
    self.edicion_anio = datarow[8]
    self.procedencia = datarow[9]
    self.editorial.id = datarow[7]
    self.fecha = datarow[3]
    self.editorial.recargar()


  def consultar(self):
    pass
  def recargar(self):
    pass
  def eliminar(self):
    query = ('DELETE FROM Libro WHERE libro_id = %s')
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.id,))
    conexion.commit()
    cursor.close()
  
  def modificar(self):
    query = ('UPDATE Libro SET \
            `libro_titulo`=%s,\
     `libro_autor`=%s,`libro_fecha`=%s,\
     `libro_numregistro`=%s,`libro_clave`=%s,\
     `libro_volumen`=%s,`libro_editorial`=%s,\
     `libro_edicion_anio`=%s,`libro_procedencia`=%s\
        WHERE `libro_id` = %s')
    print query
    conexion = self.conexion.getConnection()
    cursor= conexion.cursor()
    cursor.execute(query,(self.titulo,self.autor,self.fecha,self.numregistro,self.clave,self.volumen,self.editorial.id,self.edicion_anio,self.procedencia,self.id))
    conexion.commit()
    cursor.close()









    


	
		

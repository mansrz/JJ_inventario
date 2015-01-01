from Conexion import *
from Objeto import * 
class Modo(Objeto):
  nombre = ''
  detalles = ''
  headernames = ['Nombre','Detalles']
  atributos = ['modo_id','modo_nombre','modo_detalles']
  tabla = ' modo'
  def __init__(self):
    self.inicializar()

    #TODO
  def enlistar(self, listas):
    lista=[]
    for r in listas: 
      modo  = Modo()
      modo.mapeardatos(r)
      lista.append(modo)
    return lista

  def mapeardatos(self, datarow):
    self.id = datarow[0]
    self.nombre = datarow[1]
    self.detalles = datarow[2]


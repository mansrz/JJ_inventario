import sys
from mw import *
from conection import *
from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Editorial import *
from libro import *
from Usuario import *
import re

usuario = uic.loadUiType('usuario.ui')[0]
ui = uic.loadUiType('mainwindow.ui')[0]
pantalla1 = uic.loadUiType('pantallaprueba.ui')[0]
login = uic.loadUiType('login.ui')[0]
ingresar = uic.loadUiType('ingresar.ui')[0]
consultar = uic.loadUiType('consultar.ui')[0]
base = uic.loadUiType('base.ui')[0]
editorial_crear = uic.loadUiType('editorial.ui')[0]
estilo = open('st.stylesheet','r').read()

class Usuario_crear(QtGui.QDialog, usuario):
    usuario = Cuenta()
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()
        self.setStyleSheet(estilo )
    def inicializar(self):
        self.boton_cancelar.clicked.connect(self.cerrar)
        self.boton_limpiar.clicked.connect(self.limpiar)
        self.boton_crear.clicked.connect(self.guardar)

    def guardar(self):
        if(self.mapeardatos()):
          self.usuario.guardar()
          self.limpiar()
          QMessageBox.about(self,"Exito","Guardado con exito")
        else:
          QMessageBox.about(self,"Error","Ingrese datos correctos")
        
    def mapeardatos(self):
        try:
          self.usuario.nombre = str(self.texto_nombre.text())
          self.usuario.nick = str(self.texto_nick.text())
          self.usuario.pwd = str(self.texto_pwd.text())
          if len(self.usuario.nombre)<1 or len(self.usuario.nick)<1 or len(self.usuario.pwd)<1:
            return False
        except:
          return False
        return True

    def cerrar(self):
        self.close()

    def limpiar(self):
        self.texto_nombre.setText('')
        self.texto_nick.setText('')
        self.texto_pwd.setText('')
        self.usuario = Cuenta()

class Editorial_crear(QtGui.QDialog, editorial_crear):
    editorial= Editorial()
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()
        self.setStyleSheet(estilo )
    def inicializar(self):
        self.boton_cancelar.clicked.connect(self.cerrar)
        self.boton_limpiar.clicked.connect(self.limpiar)
        self.boton_crear.clicked.connect(self.guardar)

    def guardar(self):
        if(self.mapeardatos()):
          self.editorial.guardar()
          self.limpiar()
          QMessageBox.about(self,"Exito","Guardado con exito")
        else:
          QMessageBox.about(self,"Error","Ingrese datos correctos")
        
    def mapeardatos(self):
        try:
          self.editorial.nombre = str(self.texto_nombre.text())
          self.editorial.pais = str(self.texto_pais.text())
          if len(self.editorial.nombre)<1 or len(self.editorial.pais)<1:
            return False
        except:
          return False
        return True

    def cerrar(self):
        self.close()

    def limpiar(self):
        self.texto_nombre.setText('')
        self.texto_pais.setText('')
        self.editorial = Editorial()

class Base(QtGui.QDialog, base):
    lista = []
    editorial = Editorial()
    libro = Libro()
    headernames = ['Titulo','Autor','Fecha','N. Registro', 'Clave', 'Volumen', 'Editorial', 'Anio','Procedencia']
    selected_index=-1

    def __init__(self, parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.setupUi(self)
#     screen = QtGui.QDesktopWidget().screenGeometry()
#     self.widget.move((screen.width()-self.widget.geometry().width())/2, (screen.height()-self.widget.geometry().height())/2)
      self.inicializar()
      self.setStyleSheet(estilo )
    def mapearfiltro(self):
      filtro =' WHERE'
      str_and = ' '
      id = str(self.texto_id.text())
      titulo = str(self.texto_titulo.text())
      autor = str(self.texto_autor.text())
      numregistro = str(self.texto_numregistro.text())
      clave = str(self.texto_clave.text())
      volumen = str(self.texto_volumen.text())
      edicion_anio = str(self.texto_edicion_anio.text())
      procedencia = str(self.texto_procedencia.text())
      editorial = str(self.cbo_editorial.currentIndex()+1)
      anio_ = str(self.texto_anio_.text())
      print anio_
      dia = str(self.texto_dia.text())
      print dia
      mes = str(self.texto_mes.text())
      print mes
      if len(id)>0 :
        filtro = filtro + ' libro_id="'+re.sub(r'\D','',id)+'" '
        print filtro
        str_and = ' AND '
      if len(titulo)>0 :
        filtro = filtro + str_and + 'libro_titulo="' + titulo + '" ' 
        str_and = ' AND '
      if len(autor)>0 :
        filtro = filtro + str_and + 'libro_autor="' + autor  + '" ' 
        str_and = ' AND ' 
      if len(numregistro)>0 :
        filtro = filtro + str_and + 'libro_numregistro="' + numregistro + '" ' 
        str_and = ' AND '
      if len(clave)>0:
        filtro = filtro + str_and + 'libro_clave="' + clave + '" ' 
        str_and = ' AND '
      if len(volumen)>0:
        filtro = filtro + str_and + 'libro_volumen="' + volumen + '" '
        str_and = ' AND '
      if len(edicion_anio)>0:
        filtro = filtro + str_and + 'libro_edicion_anio="' + edicion_anio + '" '
        str_and = ' AND '
      if len(procedencia)>0:
        filtro = filtro + str_and + 'libro_procedencia="' + procedencia + '" ' 
        str_and = ' AND '
      if len(editorial) >0 and int(editorial)>0:
        filtro = filtro + str_and + 'libro_editorial="' + editorial + '" ' 
        str_and =' AND '
      if len(dia)>0 and dia!='0':
        filtro = filtro + str_and + 'day(libro_fecha) like "' + dia + '" ' 
        str_and =' AND '
        print str(dia)
      if len(mes)>0 and mes !='0':
        filtro = filtro + str_and + 'month(libro_fecha) like "' + mes + '" ' 
        str_and =' AND '
      if len(anio_)>4 and anio_ !='0':
        filtro = filtro + str_and + 'year(libro_fecha) like "' + anio_ + '" ' 
        str_and =' AND '
        print str(anio_)
      print filtro
      if str_and == ' ':
        filtro =''
      return filtro


    def inicializar(self):
      libro = Libro()
      self.boton_buscar.clicked.connect(self.boton_buscarclick)
      self.tabla_datos.clicked.connect(self.elegir_click)
      self.tabla_datos.doubleClicked.connect(self.elegir_dobleclick)
      self.lista = libro.consultar_todos(self.mapearfiltro())
      for editor in self.editorial.consultar_todos():
          self.cbo_editorial.addItem(editor[1],editor[0])
      self.buscar()

    def elegir_click(self):
      selected = self.tabla_datos.selectedIndexes()
      for select in selected:
        self.selected_index = select.row()

    def elegir_dobleclick(self):
      selected = self.tabla_datos.selectedIndexes()
      for select in selected:
        self.selected_index = select.row()
    
    def boton_buscarclick(self):   
      filtro = self.mapearfiltro()
      self.lista = self.libro.consultar_todos(filtro)
      self.buscar()

    def buscar(self):
      model = QStandardItemModel()
      model.setColumnCount(8)
      model.setHorizontalHeaderLabels(self.headernames)
      for libro in self.lista:
        li = [libro.titulo,libro.autor,libro.fecha,libro.numregistro,libro.clave,libro.volumen,libro.editorial.nombre,libro.edicion_anio,libro.procedencia]
        row = []
        for name in li:
          item = QStandardItem(str(name))
          item.setEditable(False)
          row.append(item)
        model.appendRow(row)
      self.tabla_datos.setModel(model)

        
class Modificar(Base):
    def __init__(self, **kwds):
      super(Modificar, self).__init__(**kwds)
      self.boton_cerrar.setText('Modificar')
      self.boton_cerrar.clicked.connect(self.modificar_elemento)
      self.setStyleSheet(estilo )

    def modificar_elemento(self):
      print 'Holi'
      modificar = Modificar_libro()
      modificar.libro = self.lista[self.selected_index]
      modificar.mapeardatos_mod()
      modificar.exec_()      
      self.boton_buscarclick()
      pass

    def diferencias(self):
      pass
      
#TODO
#agregar boton modificar
#hacer query modificar
     

      
class Eliminar(Base):
    def __init__(self, **kwds):
      super(Eliminar, self).__init__(**kwds)
      self.boton_cerrar.setText('Eliminar')
      self.setStyleSheet(estilo )
      self.boton_cerrar.clicked.connect(self.eliminar_elemento)

    def eliminar_elemento(self):
      respuesta = QMessageBox.question(self,"Eliminar","Seguro que desea eliminar el libro?",1,2)
      print respuesta
      if (respuesta==1):
        self.lista[self.selected_index].eliminar()
        self.boton_buscarclick()


class Consultar(QtGui.QDialog, consultar):
    lista = []
    editorial = Editorial()
    libro = Libro()
    headernames = []
    headernames.append("Titulo")
    headernames.append("Autor")
    headernames.append("Fecha")
    headernames.append("N.Registro")
    headernames.append("Clave")
    headernames.append("Volumen")
    headernames.append("Editoral")
    headernames.append("Anio")
    headernames.append("Procedencia")
    selected_index=-1

    def __init__(self, parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.setupUi(self)
#     screen = QtGui.QDesktopWidget().screenGeometry()
#     self.widget.move((screen.width()-self.widget.geometry().width())/2, (screen.height()-self.widget.geometry().height())/2)
      self.setStyleSheet(estilo )
      self.inicializar()

    def inicializar(self):
      libro = Libro()
      self.boton_buscar.clicked.connect(self.boton_buscarclick)
      self.tabla_datos.clicked.connect(self.elegir_click)
      self.tabla_datos.doubleClicked.connect(self.elegir_dobleclick)
      self.lista = libro.consultar_todos(self.mapearfiltro())
      for editor in self.editorial.consultar_todos():
          self.cbo_editorial.addItem(editor[1],editor[0])

      self.buscar()

    def elegir_click(self):
      selected = self.tabla_datos.selectedIndexes()
      for select in selected:
        self.selected_index = select.row()

    def elegir_dobleclick(self):
      selected = self.tabla_datos.selectedIndexes()
      for select in selected:
        self.selected_index = select.row()

    def mapearfiltro(self):
      filtro =' WHERE'
      str_and = ' '
      id = str(self.texto_id.text())
      titulo = str(self.texto_titulo.text())
      autor = str(self.texto_autor.text())
      numregistro = str(self.texto_numregistro.text())
      clave = str(self.texto_clave.text())
      volumen = str(self.texto_volumen.text())
      edicion_anio = str(self.texto_edicion_anio.text())
      procedencia = str(self.texto_procedencia.text())
      editorial = str(self.cbo_editorial.currentIndex()+1)
      anio_ = str(self.texto_anio_.text())
      print anio_
      dia = str(self.texto_dia.text())
      print dia
      mes = str(self.texto_mes.text())
      print mes
      if len(id)>0 :
        filtro = filtro + ' libro_id="'+re.sub(r'\D','',id)+'" '
        print filtro
        str_and = ' AND '
      if len(titulo)>0 :
        filtro = filtro + str_and + 'libro_titulo="' + titulo + '" ' 
        str_and = ' AND '
      if len(autor)>0 :
        filtro = filtro + str_and + 'libro_autor="' + autor  + '" ' 
        str_and = ' AND ' 
      if len(numregistro)>0 :
        filtro = filtro + str_and + 'libro_numregistro="' + numregistro + '" ' 
        str_and = ' AND '
      if len(clave)>0:
        filtro = filtro + str_and + 'libro_clave="' + clave + '" ' 
        str_and = ' AND '
      if len(volumen)>0:
        filtro = filtro + str_and + 'libro_volumen="' + volumen + '" '
        str_and = ' AND '
      if len(edicion_anio)>0:
        filtro = filtro + str_and + 'libro_edicion_anio="' + edicion_anio + '" '
        str_and = ' AND '
      if len(procedencia)>0:
        filtro = filtro + str_and + 'libro_procedencia="' + procedencia + '" ' 
        str_and = ' AND '
      if len(editorial) >0 and int(editorial)>0:
        filtro = filtro + str_and + 'libro_editorial="' + editorial + '" ' 
        str_and =' AND '
      if len(dia)>0 and dia!='0':
        filtro = filtro + str_and + 'DAY(libro_fecha) like "' + dia + '" ' 
        str_and =' AND '
        print str(dia)
      if len(mes)>0 and mes !='0':
        filtro = filtro + str_and + 'MONTH(libro_fecha) like "' + mes + '" ' 
        str_and =' AND '
      if len(anio_)>4 and anio_ !='0':
        filtro = filtro + str_and + 'YEAR(libro_fecha) like "' + anio_ + '" ' 
        str_and =' AND '
        print str(anio_)
      print filtro
      if str_and == ' ':
        filtro =''
      return filtro

    def boton_buscarclick(self):   
      filtro = self.mapearfiltro()
      self.lista = self.libro.consultar_todos(filtro)
      self.buscar()

    def buscar(self):
      model = QStandardItemModel()
      model.setColumnCount(8)
      model.setHorizontalHeaderLabels(self.headernames)
      for libro in self.lista:
        li = [libro.titulo,libro.autor,libro.fecha,libro.numregistro,libro.clave,libro.volumen,libro.editorial.nombre,libro.edicion_anio,libro.procedencia]
        row = []
        for name in li:
          item = QStandardItem(str(name))
          item.setEditable(False)
          row.append(item)
        model.appendRow(row)
      self.tabla_datos.setModel(model)

        


class Ingresar(QtGui.QDialog, ingresar):
    editorial= Editorial()
    libro = Libro()
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.inicializar()
        self.setStyleSheet(estilo )
    def inicializar(self):
        self.boton_modificar.hide()
        self.boton_cancelar.clicked.connect(self.cerrar)
        self.boton_limpiar.clicked.connect(self.limpiar)
        self.boton_crear.clicked.connect(self.guardar)
        self.boton_agregarEditorial.clicked.connect(self.creareditorial)
        for editor in self.editorial.consultar_todos():
          self.cbo_editorial.addItem(editor[1],editor[0])

    def creareditorial(self):
        editorial = Editorial_crear()
        editorial.exec_()
        self.cbo_editorial.clear()
        for editor in self.editorial.consultar_todos():
          self.cbo_editorial.addItem(editor[1],editor[0])

    def guardar(self):
        if(self.mapeardatos()):
          self.libro.guardar()
          self.limpiar()
          QMessageBox.about(self,"Exito","Guardado con exito")

        else:
          QMessageBox.about(self,"Error","Ingrese datos correctos")
        
    def mapeardatos(self):
        try:
          self.libro.titulo = str(self.texto_titulo.text())
          self.libro.autor = str(self.texto_autor.text())
          self.libro.numregistro = str(self.texto_numregistro.text())
          self.libro.clave = str(self.texto_clave.text())
          self.libro.volumen = str(self.texto_volumen.text())
          self.libro.edicion_anio = str(self.texto_edicion_anio.text())
          self.libro.procedencia = str(self.texto_procedencia.text())
          self.libro.editorial.id = self.cbo_editorial.currentIndex()+1
          var_time = self.date_fecha.date()
          self.libro.fecha = var_time.toPyDate()
          if not self.libro.verificar():
            return False
        except:
          return False
        return True

    def cerrar(self):
        self.close()

    def limpiar(self):
        self.texto_titulo.setText('')
        self.texto_autor.setText('')
        self.texto_numregistro.setText('')
        self.texto_clave.setText('')
        self.texto_volumen.setText('')
        self.texto_edicion_anio.setText('')
        self.texto_procedencia.setText('')
        self.libro = Libro()


#TODO Clase de ventana ingresar modificada para guardar
class Modificar_libro(Ingresar):
    def __init__(self, **kwds):
      super(Modificar_libro, self).__init__(**kwds)
      self.boton_crear.hide()
      self.boton_modificar.show()
      self.setStyleSheet(estilo )
      self.boton_modificar.clicked.connect(self.modificar)

    def modificar(self):
      self.mapeardatos()
      self.libro.modificar()
      self.limpiar()
      QMessageBox.about(self,"Exito","Modificado con exito")
      self.cerrar()


    def mapeardatos_mod(self):
        try:
          self.texto_titulo.setText(self.libro.titulo)
          self.texto_autor.setText(self.libro.autor)
          self.texto_numregistro.setText(self.libro.numregistro)
          self.texto_clave.setText(self.libro.clave)
          self.texto_volumen.setText(self.libro.volumen)
          self.texto_edicion_anio.setText(self.libro.edicion_anio)
          self.texto_procedencia.setText(self.libro.procedencia)
          self.cbo_editorial.setCurrentIndex(self.libro.editorial.id)
          self.date_fecha.setDate(self.libro.fecha)
        except:
          return False
        return True




class VentanaPrincipal(QtGui.QMainWindow, ui):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.widget.move((screen.width()-self.widget.geometry().width())/2, (screen.height()-self.widget.geometry().height())/2)
        self.inicializar()
        self.setStyleSheet(estilo)

    def inicializar(self):
        self.btn_1.clicked.connect(self.btn1_clicked)
        self.btn_2.clicked.connect(self.btn2_clicked)
        self.btn_3.clicked.connect(self.btn3_clicked)
        self.btn_4.clicked.connect(self.btn4_clicked)
        self.boton_agregarUsuario.clicked.connect(self.agregar)

    def agregar(self):
        agregar = Usuario_crear()
        agregar.exec_()

    def btn1_clicked(self):
        ingresar=Ingresar()
        ingresar.exec_()

    def btn3_clicked(self):
        modificar = Modificar()
        modificar.exec_()

    def btn4_clicked(self):
        eliminar = Eliminar()
        eliminar.exec_() 

    def btn2_clicked(self):
        consultar=Consultar()
        consultar.exec_()


class Prueba(QtGui.QDialog, pantalla1):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)

class Login(QtGui.QDialog, login):
    conexion = Conexion()
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.setStyleSheet(estilo)
        self.boton_iniciarsesion.clicked.connect(self.login_act)

    def login_act(self):
        name = str(self.input_usuario.text())
        pwd = str(self.input_pwd.text())
        query = ('SELECT COUNT(*) FROM proyecto_laboratorio.Cuenta WHERE cuenta_nick= %s AND cuenta_pwd = %s')
        conexion = self.conexion.getConnection()
        cursor= conexion.cursor()
        cursor.execute(query,(name,pwd))
        result=cursor.fetchone()
        print result
        if result[0]>0:
            self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Usuario o contrasena equivocadas', QtGui.QMessageBox.Ok)
        cursor.close()
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if Login().exec_() == QtGui.QDialog.Accepted:
        print 'holiwis'
        principal = VentanaPrincipal()
        principal.showMaximized()
        sys.exit(app.exec_())




    

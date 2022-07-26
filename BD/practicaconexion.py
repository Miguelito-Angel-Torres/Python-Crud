import mysql.connector
from mysql.connector import Error
from BD_MySQL.principal import ejecutarOpcion 

class Conexion():
    #Constructor:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(

            )
        except Error as ex :
            print("Error en agregar la variable la conexion:{0}".format(ex))

    def listar(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM persona order by nombre ASC")
                resultado = cursor.fetchall()
                return resultado 
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
    
    def registrar(self,persona):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("INSERT INTO persona(idalumno,nombre,apellidos,materias,calificacion,estatus)Values(null,'{0}','{1}','{2}','{3}','{4}'")
                cursor.execute(sql.format(persona[0],persona[1],persona[2],persona[3],persona[4]))
                self.conexion.commint()
                print("!Persona Registrada!\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
    
    def actualizar(self,personas):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("UPDATE persona set nombre = {0},apellido = {1} where idalumno ='{5}' ")
                cursor.execute(sql.format(personas[0],personas[1],personas[5]))
                self.conexion.commint()
                print("Persona Actualizada\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
    
    def eliminar(self,codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = ("DELETE FROM persona where idalumno = '{0}'")
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commint()
                print("Persona Eliminado\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))



#IMPORTACIONES
from funciones import PedirDatosparaEliminacion,pedirDatosRegistro,PedirDatosparaActualiza,ListarPersonas
from BD.conexion import DAD
from mysql.connector import Error

def menuPrincipal():
    continuar = True 
    while(continuar == True):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("===MenuPrincipal===")
            print("===================")
            print("1. Listar")
            print("2.Registrar")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Salir")
            print("====================")

            opcion = int(input("Seleccione una opcion:"))

            if(opcion <1 or opcion > 5):
                print("Opcion incorrecta,ingresa nuevamente.")

            elif(opcion == 5):
                continuar=False
                print("Gracias por usar el sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    #Instanciar la clase:
    dao = DAD()
    if opcion==1:
        try:
            persona = dao.listar()
            if(len(persona)>0):
                ListarPersonas(persona)           
            else:
                print("No se encontramos personas...")

        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
    elif opcion==2:
        persona = pedirDatosRegistro()
        try:
            dao.registrar(persona)
        
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
    elif opcion ==3:
        try:
            persona = dao.listar()
            if len(persona)>0:
                otravariablepersona = PedirDatosparaActualiza(persona)
                if not(otravariablepersona == ""):
                    dao.actualizar(otravariablepersona)
                else:
                    print("Codigo de cusro no encontrado \n")         
            else:
                print("No se encontraron persona")
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
    elif opcion ==4:
        try:
            persona = dao.listar()
            if len(persona)>0:
                codigoEliminar = PedirDatosparaEliminacion(persona)
                if not(codigoEliminar == ""):
                    dao.eliminar(codigoEliminar)
                else:
                    print("Codigo no Encontrado")
            else:
                print("No se enontraron personas")


        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
    else:
        print("Opcion no validad")

if __name__ == "__main__":
    menuPrincipal()


#funciones
def ListarPersonas(personas):
    print("\n==Listado de Personas==")
    contador =  1
    for cur in personas:
        datoscodigo = cur[0]
        datos = "{0}.Codigo:{1} |Nombre:{2}"
        print(datos.format(contador,datoscodigo[0],cur[1]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    nombre = input("Ingrese nombre:")
    apellido = input("Ingrese apellido:")
    materia = input("Ingrese materia:")
    CalificaCorrecto = False
    while(not CalificaCorrecto):
        califica = input("Ingrese calificacion:")
        if califica.isnumeric():
            if (int(califica)>0 and int(califica)<21):
                CalificaCorrecto = True
                calificax = int(califica)
            else:
                print("La calificacion deber ser de 0 hasta 20")
        else:
            print("Debes ser un numero")
        
    estatus = input("Ingrese estatus:")

    persona = (nombre,apellido,materia,calificax,estatus)
    return persona 


def PedirDatosparaEliminacion(personas):
    ListarPersonas(personas)
    existeCodigo =  False
    codigoEliminar = int(input("Ingrese el codigo que vas a eliminar:"))
    
    for cur in personas:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""

    return(codigoEliminar)


def PedirDatosparaActualiza(personas):
    ListarPersonas(personas)
    existeCodigo = False
    codigoEditar = int(input("Inquide el Codigo que deseas Actualizar:"))
    for cur in personas:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
    
    if existeCodigo ==True:
        nombre = input("Ingrese nombre a Modificar:")
        calificar = input("Ingrese calificacion  a Modificar:")
        calificacion  = False
        if calificar.isnumeric():
            if(int(calificar)>0 and int(calificar)<21):
                calificacion = True
                calificar = int(calificar)
            else:
                print("")
        else:
            print("")

        person = (codigoEditar,nombre)
    else:
        person = ""

    return person 

    




    









            


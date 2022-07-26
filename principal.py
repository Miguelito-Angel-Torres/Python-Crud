#IMPORTACIONES
from funciones import PedirDatosparaEliminacion
from funciones import pedirDatosRegistro
from funciones import PedirDatosparaActualiza
from BD.conexion import DAD

#IMPORTACIONES PARA ERRORES
from mysql.connector import Error
#IMPORTACIONOES LAS Funciones
from funciones import ListarPersonas


def menuPrincipal():
    #Para que se repita tantas veces que el usuario desee:
    continuar = True
    while(continuar == True):   
        opcionCorrecta = False # Es decir que ahorita tenemos la opcion Incorrecta y no tenemos opcioncorrecta
        while(not opcionCorrecta):#Mientras la opcion no es correcta
            print("==========================================")
            print("==========MENU PRINCIPAL =================")
            print("==========================================")
            print("1.- Listar")
            print("2.- Registrar")
            print("3.- Actualizar")
            print("4.- Eliminar")
            print("5.- Salir")
            print("============================================")
            opcion=int(input("Seleccione una ópcion:"))
            
            if(opcion <1 or opcion >5):
                print("Opcion incorrecta,ingrese nuevamente...")
            elif(opcion ==5):
                continuar=False
                print("¡Gracias por usar este sistema¡")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


    
def ejecutarOpcion(opcion):
    #print("Esta es la opcion Seleccionada",opcion)
    #Instanciar la clase :
    dao = DAD()
    if opcion==1:
        try:
            personas=dao.listar()
            if len(personas)>0:  
                ListarPersonas(personas)
            else:
                print("No se encontraron personas....")
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
            
        #except Error as  ex:
            #print("Occurrio un error: {0}".format(ex))
    elif opcion==2:
        persona= pedirDatosRegistro()
        try:
            dao.registrar(persona)

        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
        
        
    elif opcion==3:
        try:
            personas = dao.listar()
            if len(personas)>0:
                personas = PedirDatosparaActualiza(personas)
                if not(personas == "" ):
                    dao.actualizar(personas)
                else:
                    print("Codigo de curso no encontrado...\n")
            else:
                print("No se encontraron personas....")
                
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
        
    elif opcion==4:
       
        try:
            #Primera sera mostrar los cursos:
            personas = dao.listar()
            if len(personas)>0:
                codigoEliminar = PedirDatosparaEliminacion(personas)
                if not(codigoEliminar == "" ):
                    dao.eliminar(codigoEliminar)
                else:
                    print("Codigo de Curso no encontrado")
            else:
                print("No se encontraron personas....")
                
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
        

       
    else:
        print("Opcion no válida...")
   



menuPrincipal()
#52
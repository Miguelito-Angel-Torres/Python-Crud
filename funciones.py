def ListarPersonas(personas):
    print("\n===============Listado de Personas=============================:")
    contador = 1
    for cur in personas:
        datoscodigo = cur[0]
        datos ="{0}. Codigo:{1} |Nombre:{2} |Apellido:{3} |Materia:{4} |Calificaicon:{5}({6} estatus)"
        print(datos.format(contador,cur[0],cur[1],cur[2],cur[3],cur[4],cur[5]))
        print("Codigo:"  , (datoscodigo + (7*15)))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    nombre = input("Ingrese nombre: ")
    apellido=input("Ingrese apellido: ")
    materia = input("Ingrese materia: ")
    
    calificaCorrecto = False
    while (not calificaCorrecto):
        califica = input("Ingrese calificacion: ")
        if califica.isnumeric():
            if (int(califica) > 0 and int(califica) <21):
                calificaCorrecto = True
                califica = int(califica)
            else:
                print("Las calificaciones debe ver 0 hasta 20")
        else:
            print("Debe ser un numero unicamente.")

    estatus = input("Ingrese estatus: ")

    
    persona = (nombre,apellido,materia,califica,estatus)

    return persona

def PedirDatosparaEliminacion(personas):
    #Para que haga el mismo procedimiento de la func.ListarPersonas
    ListarPersonas(personas)
    existeCodigo = False
    codigoEliminar = int(input("Indique el Codigo que deseas Eliminar:"))
    for cur in personas:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar =""


    return (codigoEliminar)


    
def PedirDatosparaActualiza(personas):
    #LISTAR LAS PERSONAS CON LA FUNCION:
    ListarPersonas(personas)
    #VERFICAR EL CODIGO DE LA PERSONA QUE DESEAMOS ACTUALIZAR:
    existeCodigo = False
    codigoEditar = int(input("Indique el Codigo que deseas Actualizar:"))
    for cur in personas:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo == True:
        nombre = input("Ingrese nombre a Modificar: ")
        apellido=input("Ingrese apellido a Modificar: ")
        materia = input("Ingrese materia a Modificar: ")
    
        calificaCorrecto = False
        while (not calificaCorrecto):
            califica = input("Ingrese calificacion a Modificar: ")
            if califica.isnumeric():
                if (int(califica) > 0 and int(califica) <21):
                    calificaCorrecto = True
                    califica = int(califica)
                else:
                    print("Las calificaciones debe ver 0 hasta 20")
            else:
                print("Debe ser un numero unicamente.")

        estatus = input("Ingrese estatus a Modificar: ")

    
        person = (codigoEditar,nombre,apellido,materia,califica,estatus)
        
    else:
        person =""
   

    return person




            
    
    
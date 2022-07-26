import mysql.connector

from mysql.connector import Error

class Conexion():
    try:

        conexion = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '',
            db='cursophp')

        if conexion.is_connected():
            print("Conexion Exitosa.")
            info_server = conexion.get_server_info() # Le indico que traiga la informacion del Servidor
            print(info_server)

        # cursor : Para porder ejecutar la instruccion 
            cursor = conexion.cursor() #Los cursores nos indica hacer busqueda,insercion y actualizacion
        #Una instruccion:
            cursor.execute("SELECT DATABASE()")
            row = cursor.fetchone()# Para obtener un registro
            print("Conexion a la base de datos: {} " .format(row))
            cursor.execute("SELECT * FROM empleados")
            resultado= cursor.fetchall() #Para ontener todo los registro
            for fila in resultado:
                print(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            print("Total de Registro",cursor.rowcount)
            


    


    except Error as ex:
        print("Error durante la Conexion.", ex)

    finally:
        if conexion.is_connected():
            conexion.close()
            print("Conexion Finalizado")



"""from BD.conexionfirme import DAD

dao =DAD()

filas=dao.listar()

for fila in filas:

    print(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])"""
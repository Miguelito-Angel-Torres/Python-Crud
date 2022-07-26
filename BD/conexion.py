#Importacion para que funcione el mysql
import mysql.connector
from mysql.connector import Error


class DAD():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db='persona'

            )
        except Error as ex:
            print("Error durante la Conexion:{0}".format(ex))
       

    def listar(self):
        
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM persona ORDER BY nombre ASC")
                resultado = cursor.fetchall()# Recorrido -- Contiene las lista de la tabla 
                return resultado
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
    
    def registrar(self,persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = "INSERT INTO persona(idalumno,nombre,apellidos,materia,calificacion,estatus)VALUES(null,'{0}','{1}','{2}','{3}','{4}')"
                cursor.execute(sql.format(persona[0],persona[1],persona[2],persona[3],persona[4]))
                self.conexion.commit()
                print("!Persona Registrado¡\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))

    def actualizar(self,personas):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = "UPDATE persona SET nombre ='{0}',apellidos ='{1}',materia ='{2}',calificacion ='{3}',estatus ='{4}' WHERE idalumno = '{5}'"
                cursor.execute(sql.format(personas[1],personas[2],personas[3],personas[4],personas[5],personas[0]))
                self.conexion.commit()
                print("!Persona Actualizado¡\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
        
        


    def eliminar(self,codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql = "DELETE FROM persona WHERE idalumno = '{0}' "
                cursor.execute(sql.format(codigoEliminar))
                # commit para que se culmina la instruccion
                self.conexion.commit()
                print("!Persona Eliminado¡\n")
            except Error as ex:
                print("Error durante la Conexion:{0}".format(ex))
     



       
                




    
        







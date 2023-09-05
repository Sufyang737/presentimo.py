from conexion import Conexion

class Alumno:
    def __init__(self):
        self.id = 0 
        self.nombre = ""
        self.apellido1 = ""
        self.apellido2 = ""
        self.turno = ""
        self.curso = ""
        self.conexion = Conexion().conectar()

    def save(self, nombre, apellido1, apellido2, turno, curso):
        try:
            cursor = self.conexion.cursor() 
            self.sql = f"""
                    INSERT INTO alumnos(nombre,apellido1,apellido2,turno,curso) values('{nombre}','{apellido1}','{apellido2}','{turno}','{curso}')
                    """
            cursor.execute(self.sql)  
            self.conexion.commit()
            resp = cursor.rowcount
            cursor.close()  
            self.conexion.close()
            if resp == 1:
                return True
            else:
                return False
            

        except:
            return False
        

    def consultar_alumnos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None

    def cerrar_conexion(self):
        self.conexion.close()
        
    #Conexiones de las funcione
    def buscar_por_nombre(self, nombre):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos WHERE nombre = '{nombre}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
    
    def buscar_por_apellido(self, apellido1):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos WHERE apellido1 = '{apellido1}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None

    def buscar_por_curso(self, curso):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos WHERE curso = '{curso}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
        
    def buscar_por_turno(self, turno):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos WHERE turno = '{turno}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
        
    
    def eliminar_datos(self, id_alumno):
        try:
            cursor = self.conexion.cursor()
            sql = f"""
                DELETE FROM alumnos 
                WHERE id = {id_alumno}
            """
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Error al eliminar datos:", str(e))
            return False



        

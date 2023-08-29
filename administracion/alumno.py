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
        
    #def eliminar_datos(self, nombre, apellido1, apellido2, turno, curso):
    #cursor = conexion.cursor()
    #sql = "DELETE FROM alumnos WHERE nombre = '{nombre}' AND apellido1 = '{apellido1}' AND apellido2 = '{apellido2}' AND turno = '{turno}' AND curso = '{curso}''"
    #cursor.execute(sql)
    #conexion.commit()
    #cursor.close()
    #conexion.close()
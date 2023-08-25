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

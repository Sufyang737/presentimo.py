from conexion import Conexion

class Alumno:
    def __init__(self):
        self.id = 0 
        self.nombre = ""
        self.apellido1 = ""
        self.apellido2 = ""
        self.turno = ""
        self.curso = ""
        self.fecha = ""
        self.presentismo = ""
        self.idAlumno = 0
        self.conexion = Conexion().conectar()


    def save_alumno(self, nombre, apellido1, apellido2, turno, curso):
        try:
            cursor = self.conexion.cursor()
        
            # Insertar datos en la tabla 'alumnos'
            sql_alumnos = f"""
                INSERT INTO alumnos(nombre, apellido1, apellido2, turno, curso)
                VALUES ('{nombre}', '{apellido1}', '{apellido2}', '{turno}', '{curso}')
            """
            cursor.execute(sql_alumnos)
            self.conexion.commit()
            resp = cursor.rowcount
            cursor.close()  
            self.conexion.close()
        
            if resp == 1:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al guardar datos en la base de datos: {str(e)}")
            return False

    def save_asistencia(self, fecha, presentismo):
        try:
            cursor = self.conexion.cursor()
            idAlumno = cursor.lastrowid
            # Insertar datos en la tabla 'asistencia' con la relación de clave externa
            sql_asistencia = f"""
                INSERT INTO asistencia(fecha, presentismo, idAlumno)
                VALUES ('{fecha}', '{presentismo}', '{idAlumno}')
            """
            cursor.execute(sql_asistencia)
            self.conexion.commit()
            resp = cursor.rowcount
            cursor.close()  
            self.conexion.close()
        
            if resp == 1:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al guardar datos en la base de datos: {str(e)}")
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

    def consultar_asistencia(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT a.nombre, a.apellido1, asi.fecha FROM alumnos a inner join asistencia asi on a.id = asi.idAlumno ")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
        
    def consultar_presentismo(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT a.nombre, a.apellido1, asi.fecha FROM alumnos a inner join asistencia asi on a.id = asi.idAlumno")
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
            cursor.execute(f"SELECT * FROM alumnos a inner join asistencia asi on a.id=asi.idAlumno WHERE a.nombre = '{nombre}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
    
    def buscar_por_apellido(self, apellido1):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos a inner join asistencia asi on a.id=asi.idAlumno WHERE a.apellido1 = '{apellido1}'")
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
            cursor.execute(f"SELECT * FROM alumnos a inner join asistencia asi on a.id=asi.idAlumno WHERE a.turno = '{turno}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None

    def buscar_por_presentismo(self, presentismo):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos a inner join asistencia asi on a.id=asi.idAlumno WHERE asi.presentismo = '{presentismo}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
    
    def buscar_por_fecha(self, fecha):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT * FROM alumnos a inner join asistencia asi on a.id=asi.idAlumno WHERE asi.fecha = '{fecha}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None

    def buscar_por_asistencia(self, curso):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f"SELECT a.nombre, a.apellido1, asi.fecha FROM alumnos a inner join asistencia asi on a.id = asi.idAlumno WHERE a.curso = '{curso}'")
            data = cursor.fetchall()
            cursor.close()
            return data
        except:
            return None
        

    def editar_datos_alumnos(self, nombre, apellido1, apellido2, turno, curso, id):
        try:
            cursor = self.conexion.cursor()

            # Verificar si el alumno con el ID dado existe
            cursor.execute(f"SELECT * FROM alumnos WHERE id = {id}")
            alumno_existente = cursor.fetchone()

            if not alumno_existente:
                cursor.close()
                return False, "Alumno no encontrado"

            # Actualizar los datos del alumno
            cursor.execute(f"""
                UPDATE alumnos
                SET nombre = '{nombre}',
                    apellido1 = '{apellido1}',
                    apellido2 = '{apellido2}',
                    turno = '{turno}',
                    curso = '{curso}'
            """)
            cursor.execute(f"""
                UPDATE asistencia
                SET presentismo = '{presentismo}',
                    fecha = '{fecha}'
            """)

            self.conexion.commit()
            cursor.close()
            return True, "Datos del alumno actualizados con éxito"
        except Exception as e:
            print(f"Error al editar datos del alumno: {str(e)}")
            return False, "Error al editar datos del alumno en la base de datos"
        
    def editar_datos_asistencia(self,  presentismo, fecha, id):
        try:
            cursor = self.conexion.cursor()

            # Verificar si el alumno con el ID dado existe
            cursor.execute(f"SELECT * FROM asistencia WHERE id = {id}")
            alumno_existente = cursor.fetchone()

            if not alumno_existente:
                cursor.close()
                return False, "Registro"

            # Actualizar los datos del alumno
            cursor.execute(f"""
                UPDATE asistencia
                SET presentismo = '{presentismo}',
                    fecha = '{fecha}'
            """)

            self.conexion.commit()
            cursor.close()
            return True, "Datos del alumno actualizados con éxito"
        except Exception as e:
            print(f"Error al editar datos del alumno: {str(e)}")
            return False, "Error al editar datos del alumno en la base de datos"
        
    def eliminar_datos(self, idAlumno):
        try:
            cursor = self.conexion.cursor()
            # Delete records from asistencia table that reference the alumno to be deleted
            sql = f"""
                DELETE FROM asistencia
                WHERE idAlumno = {idAlumno}
            """
            cursor.execute(sql)
            # Delete record from alumnos table
            sql = f"""
                DELETE FROM alumnos 
                WHERE id = {idAlumno}
            """
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Error al eliminar datos:", str(e))
            return False
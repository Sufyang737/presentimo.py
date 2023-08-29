import mysql.connector

class Conexion:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escuela"
        )

    def conectar(self):
        return self.con
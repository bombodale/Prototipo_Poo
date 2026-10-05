import mysql.connector
from mysql.connector import Error


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._conexion = None
        return cls._instance

    HOST = "localhost"
    USER = "root"
    PASSWORD = ""              
    DATABASE = "eco_tech_solutions"
    PORT = 3306

    def conectar(self):
        try:
            self._conexion = mysql.connector.connect(
                host=self.HOST,
                user=self.USER,
                password=self.PASSWORD,
                database=self.DATABASE,
                port=self.PORT,
                autocommit=False
            )
            return self._conexion
        except Error as e:
            print(f"[DB] Error de conexión: {e}")
            return None

    def obtener_conexion(self):
        if self._conexion is None or not self._conexion.is_connected():
            self.conectar()
        return self._conexion

    def cerrar(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()
            self._conexion = None
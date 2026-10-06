import inspect
import re

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

    SCHEMAS = {
        "persona": """
            CREATE TABLE IF NOT EXISTS persona (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                direccion VARCHAR(255),
                telefono VARCHAR(30),
                email VARCHAR(150)
            )
        """,
        "empleado": """
            CREATE TABLE IF NOT EXISTS empleado (
                id INT PRIMARY KEY,
                fecha_inicio_contrato DATE,
                salario VARCHAR(255),
                departamento_id INT NULL
            )
        """,
        "departamento": """
            CREATE TABLE IF NOT EXISTS departamento (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                gerente_id INT NULL
            )
        """,
        "proyecto": """
            CREATE TABLE IF NOT EXISTS proyecto (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        """,
        "registro_tiempo": """
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fecha DATE,
                horas DECIMAL(5,2) NOT NULL DEFAULT 0,
                descripcion TEXT,
                empleado_id INT NOT NULL,
                proyecto_id INT NOT NULL
            )
        """,
        "usuario": """
            CREATE TABLE IF NOT EXISTS usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
                contrasena_hash VARCHAR(255) NOT NULL,
                rol ENUM('admin', 'gerente', 'empleado') NOT NULL DEFAULT 'empleado'
            )
        """,
        "empleado_proyecto": """
            CREATE TABLE IF NOT EXISTS empleado_proyecto (
                empleado_id INT NOT NULL,
                proyecto_id INT NOT NULL,
                PRIMARY KEY (empleado_id, proyecto_id)
            )
        """,
    }

    @staticmethod
    def _to_snake_case(nombre):
        nombre = re.sub(r'(?<!^)(?=[A-Z])', '_', nombre)
        return nombre.lower()

    def _obtener_modelos(self):
        import modelo

        clases = []
        for _, member in inspect.getmembers(modelo, inspect.isclass):
            if member.__module__.startswith("modelo") and member.__name__ not in {"Cifrador", "GeneradorInformes"}:
                clases.append(member)
        return sorted({clase.__name__: clase for clase in clases}.values(), key=lambda c: c.__name__)

    def crear_tablas_modelos(self):
        conn = self.obtener_conexion()
        if conn is None:
            return []

        cursor = conn.cursor()
        prioridad = {
            "persona": 0,
            "empleado": 1,
            "departamento": 2,
            "proyecto": 3,
            "registro_tiempo": 4,
            "usuario": 5,
            "empleado_proyecto": 99,
        }

        nombres_modelos = [self._to_snake_case(clase.__name__) for clase in self._obtener_modelos()]
        orden_tablas = sorted(set(nombres_modelos + ["empleado_proyecto"]), key=lambda nombre: (prioridad.get(nombre, 100), nombre))

        creadas = []
        for nombre_tabla in orden_tablas:
            if nombre_tabla in self.SCHEMAS:
                cursor.execute(self.SCHEMAS[nombre_tabla])
                creadas.append(nombre_tabla)

        conn.commit()
        cursor.close()
        return creadas

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
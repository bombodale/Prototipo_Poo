from config.conexion import Database
from modelo.departamento import Departamento


class DepartamentoDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, dep: Departamento):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        gerente_id = dep.get_gerente().get_id() if dep.get_gerente() else None
        cursor.execute(
            "INSERT INTO departamento (nombre, gerente_id) VALUES (%s,%s)",
            (dep.get_nombre(), gerente_id)
        )
        conn.commit()
        dep._id = cursor.lastrowid
        cursor.close()
        return dep

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM departamento")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def agregar_empleado(self, dep_id, emp_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE empleado SET departamento_id=%s WHERE id=%s", (dep_id, emp_id)
        )
        conn.commit()
        cursor.close()

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM departamento WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
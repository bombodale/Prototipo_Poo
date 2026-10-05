from config.conexion import Database
from modelo.proyecto import Proyecto


class ProyectoDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, proy: Proyecto):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s,%s,%s)",
            (proy.get_nombre(), proy.get_descripcion(), proy.get_fecha_inicio())
        )
        conn.commit()
        proy._id = cursor.lastrowid
        cursor.close()
        return proy

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM proyecto")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def asignar_empleado(self, proyecto_id, empleado_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT IGNORE INTO empleado_proyecto (empleado_id, proyecto_id) VALUES (%s,%s)",
            (empleado_id, proyecto_id)
        )
        conn.commit()
        cursor.close()

    def desasignar_empleado(self, proyecto_id, empleado_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM empleado_proyecto WHERE empleado_id=%s AND proyecto_id=%s",
            (empleado_id, proyecto_id)
        )
        conn.commit()
        cursor.close()

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proyecto WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
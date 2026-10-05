from config.conexion import Database


class RegistroTiempoDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, fecha, horas, descripcion, empleado_id, proyecto_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registro_tiempo (fecha, horas, descripcion, empleado_id, proyecto_id) "
            "VALUES (%s,%s,%s,%s,%s)",
            (fecha, horas, descripcion, empleado_id, proyecto_id)
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        return nuevo_id

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM registro_tiempo")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def total_horas_proyecto(self, proyecto_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COALESCE(SUM(horas),0) FROM registro_tiempo WHERE proyecto_id=%s",
            (proyecto_id,)
        )
        total = cursor.fetchone()[0]
        cursor.close()
        return float(total)

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registro_tiempo WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
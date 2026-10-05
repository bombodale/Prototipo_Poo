#CRUD reutilizable.
from config.conexion import Database


class CRUD_DB:
    def __init__(self, tabla):
        self.tabla = tabla
        self.db = Database()

    # ---------- CREATE ----------
    def insertar(self, datos: dict):
        columnas = ", ".join(datos.keys())
        marcadores = ", ".join(["%s"] * len(datos))
        sql = f"INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})"
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(datos.values()))
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        return nuevo_id

    # ---------- READ ----------
    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.tabla}")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def buscar_por_id(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.tabla} WHERE id = %s", (id,))
        fila = cursor.fetchone()
        cursor.close()
        return fila

    # ---------- UPDATE ----------
    def actualizar(self, id, datos: dict):
        asignaciones = ", ".join([f"{k} = %s" for k in datos.keys()])
        sql = f"UPDATE {self.tabla} SET {asignaciones} WHERE id = %s"
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(sql, tuple(datos.values()) + (id,))
        conn.commit()
        afectados = cursor.rowcount
        cursor.close()
        return afectados

    # ---------- DELETE ----------
    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.tabla} WHERE id = %s", (id,))
        conn.commit()
        afectados = cursor.rowcount
        cursor.close()
        return afectados
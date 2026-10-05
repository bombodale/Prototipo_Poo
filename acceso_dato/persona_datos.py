from config.conexion import Database
from modelo.persona import Persona


class PersonaDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, persona: Persona):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO persona (nombre, direccion, telefono, email) VALUES (%s,%s,%s,%s)",
            (persona.get_nombre(), persona.get_direccion(),
             persona.get_telefono(), persona.get_email())
        )
        conn.commit()
        persona.set_id(cursor.lastrowid)
        cursor.close()
        return persona

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM persona")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def actualizar(self, persona: Persona):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE persona SET nombre=%s, direccion=%s, telefono=%s, email=%s WHERE id=%s",
            (persona.get_nombre(), persona.get_direccion(),
             persona.get_telefono(), persona.get_email(), persona.get_id())
        )
        conn.commit()
        cursor.close()

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM persona WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
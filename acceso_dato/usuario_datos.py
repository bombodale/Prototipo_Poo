from config.conexion import Database
from modelo.usuario import Usuario
from modelo.cifrador import Cifrador


class UsuarioDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, nombre_usuario, password, rol):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario, contrasena_hash, rol) VALUES (%s,%s,%s)",
            (nombre_usuario, Cifrador.hash_password(password), rol)
        )
        conn.commit()
        cursor.close()

    def obtener(self, nombre_usuario):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM usuario WHERE nombre_usuario=%s", (nombre_usuario,)
        )
        fila = cursor.fetchone()
        cursor.close()
        if not fila:
            return None
        return Usuario(
            id=fila["id"],
            nombre_usuario=fila["nombre_usuario"],
            contrasena_hash=fila["contrasena_hash"],
            rol=fila["rol"]
        )

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
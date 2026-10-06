from config.conexion import Database
from modelo.usuario import Usuario
from modelo.cifrador import Cifrador


class UsuarioDAO:
    def __init__(self):
        self.db = Database()

    def _validar_rol(self, rol):
        rol_normalizado = (rol or "").strip().lower()
        if rol_normalizado not in Usuario.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido: {rol}. Roles válidos: {sorted(Usuario.ROLES_VALIDOS)}")
        return rol_normalizado

    def crear(self, nombre_usuario, password, rol):
        nombre_usuario = (nombre_usuario or "").strip()
        password = password or ""
        if not nombre_usuario:
            raise ValueError("El nombre de usuario es obligatorio.")
        if not password:
            raise ValueError("La contraseña es obligatoria.")

        rol = self._validar_rol(rol)
        if self.obtener(nombre_usuario) is not None:
            raise ValueError(f"El usuario '{nombre_usuario}' ya existe.")

        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario, contrasena_hash, rol) VALUES (%s,%s,%s)",
            (nombre_usuario, Cifrador.hash_password(password), rol)
        )
        conn.commit()
        cursor.close()
        return True

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

    def autenticar_usuario(self, nombre_usuario, password):
        usuario = self.obtener(nombre_usuario)
        if usuario is None:
            return None
        if usuario.autenticar(nombre_usuario, password):
            usuario.generar_sesion()
            return usuario
        return None

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre_usuario, rol FROM usuario ORDER BY id")
        filas = cursor.fetchall()
        cursor.close()
        return filas

    def cambiar_rol(self, id_usuario, nuevo_rol):
        rol = self._validar_rol(nuevo_rol)
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET rol=%s WHERE id=%s", (rol, id_usuario))
        conn.commit()
        cursor.close()
        return True

    def cambiar_password(self, id_usuario, nueva_password):
        nueva_password = (nueva_password or "").strip()
        if not nueva_password:
            raise ValueError("La nueva contraseña no puede estar vacía.")

        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuario SET contrasena_hash=%s WHERE id=%s",
            (Cifrador.hash_password(nueva_password), id_usuario)
        )
        conn.commit()
        cursor.close()
        return True

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        return True       
from cifrado import Cifrado

class Usuario:
    """Representa un usuario del sistema para autenticación y autorización."""

    def __init__(self, nombre_usuario: str, contrasena: str, rol: str):
        self._nombre_usuario = nombre_usuario
        self._contrasena_hash = Cifrado.hashContrasena(contrasena)
        self._rol = rol

    @property
    def nombre_usuario(self) -> str:
        return self._nombre_usuario

    @property
    def rol(self) -> str:
        return self._rol

    def autenticar(self, usuario: str, contrasena: str) -> bool:
        """Verifica credenciales comparando el hash almacenado."""
        return (self._nombre_usuario == usuario and
                self._contrasena_hash == Cifrado.hashContrasena(contrasena))

    def verificarPermiso(self, rol_requerido: str) -> bool:
        """Comprueba si el rol del usuario satisface el permiso requerido."""
        return self._rol == rol_requerido or self._rol == "admin"

    def cambiarContrasena(self, nueva_contrasena: str) -> bool:
        """Actualiza la contraseña almacenando su nuevo hash."""
        self._contrasena_hash = Cifrado.hashContrasena(nueva_contrasena)
        return True

    def generarSesion(self) -> bool:
        """Simula la generación de una sesión exitosa."""
        return True

    def __str__(self):
        return f"Usuario({self._nombre_usuario}, rol={self._rol})"
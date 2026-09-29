import base64
import hashlib

class Cifrado:
    """Clase utilitaria para cifrado y hash de datos sensibles."""

    @staticmethod
    def cifrarDatos(dato: str) -> str:
        """Cifra un dato usando codificación Base64 (simulación)."""
        return base64.b64encode(dato.encode('utf-8')).decode('utf-8')

    @staticmethod
    def descifrarDatos(dato_cifrado: str) -> str:
        """Descifra un dato codificado en Base64."""
        return base64.b64decode(dato_cifrado.encode('utf-8')).decode('utf-8')

    @staticmethod
    def hashContrasena(contrasena: str) -> str:
        """Genera un hash SHA-256 para almacenar contraseñas de forma segura."""
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
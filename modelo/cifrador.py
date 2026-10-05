import base64
import hashlib


class Cifrador:
    _CLAVE = hashlib.sha256(b"EcoTechSolutions2026").digest()

    @classmethod
    def cifrar_datos(cls, dato):
        if dato is None:
            return None
        dato_bytes = str(dato).encode("utf-8")
        cifrado = bytes(
            b ^ cls._CLAVE[i % len(cls._CLAVE)]
            for i, b in enumerate(dato_bytes)
        )
        return base64.b64encode(cifrado).decode("utf-8")

    @classmethod
    def descifrar_datos(cls, dato_cifrado):
        if not dato_cifrado:
            return None
        try:
            cifrado = base64.b64decode(dato_cifrado)
            descifrado = bytes(
                b ^ cls._CLAVE[i % len(cls._CLAVE)]
                for i, b in enumerate(cifrado)
            )
            return descifrado.decode("utf-8")
        except Exception:
            return None

    @classmethod
    def hash_password(cls, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @classmethod
    def verificar_password(cls, password: str, hash_guardado: str) -> bool:
        return cls.hash_password(password) == hash_guardado
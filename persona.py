import re

class Persona:
    """Clase base que representa a una persona con atributos comunes."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    # Getters y setters con validación básica
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, valor: str):
        self._direccion = valor.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not self._validar_telefono(valor):
            raise ValueError("Teléfono inválido. Debe tener entre 7 y 15 dígitos.")
        self._telefono = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if not self._validar_email(valor):
            raise ValueError("Correo electrónico inválido.")
        self._email = valor

    def _validar_email(self, email: str) -> bool:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))

    def _validar_telefono(self, telefono: str) -> bool:
        patron = r'^\+?[\d\s-]{7,15}$'
        return bool(re.match(patron, telefono))

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, valor: str):
        self.nombre = valor

    def getDireccion(self) -> str:
        return self.direccion

    def setDireccion(self, valor: str):
        self.direccion = valor

    def getTelefono(self) -> str:
        return self.telefono

    def setTelefono(self, valor: str):
        self.telefono = valor

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, valor: str):
        self.email = valor
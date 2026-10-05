class Persona:
    """Clase base del diagrama UML."""

    def __init__(self, nombre="", direccion="", telefono="", email="", id=None):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    # -------- Getters / Setters --------
    def get_id(self):
        return self._id

    def set_id(self, valor):
        self._id = valor

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, valor):
        self._direccion = valor

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, valor):
        self._telefono = valor

    def get_email(self):
        return self._email

    def set_email(self, valor):
        if valor and "@" not in valor:
            raise ValueError("Email inválido.")
        self._email = valor

    def __str__(self):
        return f"Persona(id={self._id}, nombre={self._nombre}, email={self._email})"
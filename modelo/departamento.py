class Departamento:
    """Agregación: los empleados existen independientemente del departamento."""

    def __init__(self, id=None, nombre="", gerente=None):
        self._id = id
        self._nombre = nombre
        self._gerente = gerente
        self._empleados = []

    # -------- Getters / Setters --------
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_gerente(self):
        return self._gerente

    def set_gerente(self, gerente):
        self._gerente = gerente

    def get_empleados(self):
        return self._empleados

    # -------- Métodos del UML --------
    def agregar_empleado(self, empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    def remover_empleado(self, empleado):
        if empleado in self._empleados:
            self._empleados.remove(empleado)

    def listar_empleados(self):
        return list(self._empleados)

    def __str__(self):
        return f"Departamento({self._nombre}, empleados={len(self._empleados)})"
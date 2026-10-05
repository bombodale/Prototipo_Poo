class Proyecto:

    def __init__(self, id=None, nombre="", descripcion="", fecha_inicio=None):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._empleados = []

    # -------- Getters / Setters --------
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, valor):
        self._descripcion = valor

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_empleados(self):
        return self._empleados

    # -------- Métodos del UML --------
    def asignar_empleado(self, empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)

    def desasignar_empleado(self, empleado):
        if empleado in self._empleados:
            self._empleados.remove(empleado)

    def obtener_horas_totales(self, registros=None):
        if registros is None:
            return 0.0
        return sum(r.get_horas() for r in registros if r.get_proyecto().get_id() == self._id)

    def __str__(self):
        return f"Proyecto({self._nombre})"
class RegistroTiempo:

    def __init__(self, id=None, fecha=None, horas=0.0, descripcion="",
                 empleado=None, proyecto=None):
        self._id = id
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion
        self._empleado = empleado
        self._proyecto = proyecto

    # -------- Getters / Setters --------
    def get_id(self):
        return self._id

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, valor):
        self._fecha = valor

    def get_horas(self):
        return float(self._horas)

    def set_horas(self, valor):
        if valor < 0 or valor > 24:
            raise ValueError("Las horas deben estar entre 0 y 24.")
        self._horas = valor

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, valor):
        self._descripcion = valor

    def get_empleado(self):
        return self._empleado

    def get_proyecto(self):
        return self._proyecto

    # -------- Método agregado en UML final --------
    def validar_horas(self):
        return 0 <= float(self._horas) <= 24

    def __str__(self):
        return f"RegistroTiempo({self._fecha}, {self._horas}h)"
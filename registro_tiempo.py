from datetime import date

class RegistroTiempo:
    """Registro de horas trabajadas por un empleado en un proyecto."""

    def __init__(self, id: int, fecha: date, horas: float, descripcion: str,
                 empleado, proyecto):
        self._id = id
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion
        self._empleado = empleado
        self._proyecto = proyecto

        # Composición: el registro se agrega a empleado y proyecto
        empleado.agregarRegistroTiempo(self)
        proyecto.agregarRegistroTiempo(self)

    # --- Getters y setters ---
    @property
    def id(self) -> int:
        return self._id

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: date):
        self._fecha = valor

    @property
    def horas(self) -> float:
        return self._horas

    @horas.setter
    def horas(self, valor: float):
        if not self.validarHoras(valor):
            raise ValueError("Las horas deben ser mayores a 0 y menores o iguales a 24.")
        self._horas = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str):
        self._descripcion = valor.strip()

    @property
    def empleado(self):
        return self._empleado

    @property
    def proyecto(self):
        return self._proyecto

    # --- Métodos ---
    def validarHoras(self, horas: float = None) -> bool:
        """Valida que las horas estén en el rango permitido."""
        h = horas if horas is not None else self._horas
        return 0 < h <= 24

    def getHoras(self) -> float:
        return self.horas

    def setHoras(self, valor: float):
        self.horas = valor

    def getDescripcion(self) -> str:
        return self.descripcion

    def setDescripcion(self, valor: str):
        self.descripcion = valor

    def __str__(self):
        return f"RegistroTiempo(id={self._id}, horas={self._horas}, empleado={self._empleado.nombre})"
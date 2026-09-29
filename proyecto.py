from datetime import date

class Proyecto:
    """Iniciativa o trabajo en el que participan empleados."""

    def __init__(self, nombre: str, descripcion: str, fecha_inicio: date):
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._empleados = []          # Asociación * -> Empleado
        self._registros_tiempo = []   # Composición 1..* -> RegistroTiempo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @property
    def empleados(self) -> list:
        return self._empleados.copy()

    @property
    def registros_tiempo(self) -> list:
        return self._registros_tiempo.copy()

    def asignarEmpleado(self, empleado) -> bool:
        """Asocia un empleado al proyecto."""
        if empleado not in self._empleados:
            self._empleados.append(empleado)
        return True

    def desasignarEmpleado(self, empleado) -> bool:
        """Elimina la asociación de un empleado al proyecto."""
        if empleado in self._empleados:
            self._empleados.remove(empleado)
        return True

    def obtenerHorasTotales(self) -> float:
        """Suma las horas registradas en el proyecto (solo válidas)."""
        total = 0.0
        for reg in self._registros_tiempo:
            if reg.validarHoras():
                total += reg.horas
        return total

    def agregarRegistroTiempo(self, registro):
        """Usado por RegistroTiempo para la composición."""
        self._registros_tiempo.append(registro)

    def __str__(self):
        return f"Proyecto({self._nombre}, inicio={self._fecha_inicio})"
class Departamento:
    """Unidad organizacional que agrupa empleados bajo un gerente."""

    def __init__(self, nombre: str, gerente):
        self._nombre = nombre
        self._gerente = gerente
        self._empleados = []   # Agregación * -> Empleado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def gerente(self):
        return self._gerente

    @property
    def empleados(self) -> list:
        return self._empleados.copy()

    def agregarEmpleado(self, empleado) -> bool:
        """Agrega un empleado a la lista del departamento."""
        if empleado not in self._empleados:
            self._empleados.append(empleado)
        return True

    def removerEmpleado(self, empleado) -> bool:
        """Remueve un empleado del departamento."""
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            if empleado.departamento == self:
                empleado._departamento = None
        return True

    def listarEmpleados(self) -> list:
        """Devuelve la lista de empleados del departamento."""
        return self._empleados.copy()

    def __str__(self):
        return f"Departamento({self._nombre}, gerente={self._gerente.nombre if self._gerente else 'N/A'})"
from datetime import date
from persona import Persona
from cifrado import Cifrado

class Empleado(Persona):
    """Representa a un empleado de Eco Tech Solutions."""

    def __init__(self, id: int, nombre: str, direccion: str, telefono: str,
                 email: str, fecha_inicio_contrato: date, salario: float):
        super().__init__(nombre, direccion, telefono, email)
        self._id = id
        self._fecha_inicio_contrato = fecha_inicio_contrato
        self._salario_cifrado = Cifrado.cifrarDatos(str(salario))
        self._departamento = None          # Agregación 0..1
        self._proyectos = []               # Asociación *
        self._registros_tiempo = []        # Composición 1..*

    # --- Propiedades ---
    @property
    def id(self) -> int:
        return self._id

    @property
    def fecha_inicio_contrato(self) -> date:
        return self._fecha_inicio_contrato

    @property
    def salario(self) -> float:
        """Descifra y devuelve el salario."""
        return float(Cifrado.descifrarDatos(self._salario_cifrado))

    @salario.setter
    def salario(self, valor: float):
        self._salario_cifrado = Cifrado.cifrarDatos(str(valor))

    @property
    def departamento(self):
        return self._departamento

    @property
    def proyectos(self) -> list:
        return self._proyectos.copy()

    @property
    def registros_tiempo(self) -> list:
        return self._registros_tiempo.copy()

    # --- Métodos de negocio ---
    def asignarDepartamento(self, depto):
        """Asigna el empleado a un departamento (agregación)."""
        if self._departamento is not None:
            self._departamento.removerEmpleado(self)
        self._departamento = depto
        if depto is not None:
            depto.agregarEmpleado(self)
        return True

    def asignarProyecto(self, proyecto):
        """Asocia el empleado a un proyecto (asociación *)."""
        if proyecto not in self._proyectos:
            self._proyectos.append(proyecto)
            proyecto.asignarEmpleado(self)
        return True

    def removerProyecto(self, proyecto):
        """Elimina la asociación con un proyecto."""
        if proyecto in self._proyectos:
            self._proyectos.remove(proyecto)
            proyecto.desasignarEmpleado(self)
        return True

    def calcularSueldoTotal(self) -> float:
        """Calcula el sueldo total (puede ser sobrescrito por subclases)."""
        return self.salario

    def descifrarSalario(self) -> float:
        """Método explícito para obtener el salario descifrado."""
        return self.salario

    def validarEmail(self) -> bool:
        return self._validar_email(self.email)

    def validarTelefono(self) -> bool:
        return self._validar_telefono(self.telefono)

    def agregarRegistroTiempo(self, registro):
        """Usado por RegistroTiempo para la composición."""
        self._registros_tiempo.append(registro)

    def __str__(self):
        return f"Empleado(id={self._id}, nombre={self.nombre}, email={self.email})"
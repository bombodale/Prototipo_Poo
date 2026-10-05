from modelo.persona import Persona
from modelo.cifrador import Cifrador


class Empleado(Persona):
    def __init__(self, id=None, nombre="", direccion="", telefono="", email="",
                 fecha_inicio_contrato=None, salario=0.0,
                 departamento=None, proyectos=None):
        super().__init__(nombre, direccion, telefono, email, id=id)
        self._fecha_inicio_contrato = fecha_inicio_contrato
        self._salario = salario                  # se cifra al persistir
        self._departamento = departamento        # objeto Departamento
        self._proyectos = proyectos if proyectos is not None else []
        self._registros_tiempo = []              # composición

    # -------- Getters / Setters --------
    def get_fecha_inicio_contrato(self):
        return self._fecha_inicio_contrato

    def set_fecha_inicio_contrato(self, valor):
        self._fecha_inicio_contrato = valor

    def get_salario(self):
        return self._salario

    def set_salario(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = valor

    def get_departamento(self):
        return self._departamento

    def get_proyectos(self):
        return self._proyectos

    # -------- Métodos del UML --------
    def asignar_departamento(self, departamento):
        self._departamento = departamento
        if departamento and self not in departamento.get_empleados():
            departamento.agregar_empleado(self)

    def asignar_proyecto(self, proyecto):
        if proyecto not in self._proyectos:
            self._proyectos.append(proyecto)
            if self not in proyecto.get_empleados():
                proyecto.asignar_empleado(self)

    def remover_proyecto(self, proyecto):
        if proyecto in self._proyectos:
            self._proyectos.remove(proyecto)
            if self in proyecto.get_empleados():
                proyecto.desasignar_empleado(self)

    def calcular_sueldo_total(self):
        """Polimorfismo: puede sobrescribirse en subclases (Gerente, etc.)."""
        return self._salario

    def agregar_registro_tiempo(self, registro):
        self._registros_tiempo.append(registro)

    def obtener_registros_tiempo(self):
        return self._registros_tiempo

    def __str__(self):
        return f"Empleado(id={self.get_id()}, nombre={self.get_nombre()}, salario=***)"
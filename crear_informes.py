class CrearInformes:
    """Genera informes y permite su exportación."""

    def __init__(self, formato: str = "PDF"):
        self._formato = formato

    @property
    def formato(self) -> str:
        return self._formato

    @formato.setter
    def formato(self, valor: str):
        self._formato = valor.upper()

    def generarInformeEmpleados(self, empleados: list) -> str:
        lineas = ["=== INFORME DE EMPLEADOS ==="]
        for emp in empleados:
            lineas.append(f"ID: {emp.id} | Nombre: {emp.nombre} | Email: {emp.email} | Depto: {emp.departamento.nombre if emp.departamento else 'Sin asignar'}")
        return "\n".join(lineas)

    def generarInformeProyectos(self, proyectos: list) -> str:
        lineas = ["=== INFORME DE PROYECTOS ==="]
        for proy in proyectos:
            lineas.append(f"Proyecto: {proy.nombre} | Horas totales: {proy.obtenerHorasTotales()}")
        return "\n".join(lineas)

    def generarInformeHoras(self, registros: list) -> str:
        lineas = ["=== INFORME DE HORAS ==="]
        for reg in registros:
            lineas.append(f"ID: {reg.id} | Empleado: {reg.empleado.nombre} | Proyecto: {reg.proyecto.nombre} | Horas: {reg.horas}")
        return "\n".join(lineas)

    def exportarPDF(self, contenido: str):
        print(f"[Exportando a PDF] {contenido[:50]}...")

    def exportarExcel(self, contenido: str):
        print(f"[Exportando a Excel] {contenido[:50]}...")
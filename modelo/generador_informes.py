class GeneradorInformes:
    """Genera informes y exporta a PDF/Excel (según apartado 5.1)."""

    def __init__(self, formato="PDF"):
        self._formato = formato

    def get_formato(self):
        return self._formato

    def set_formato(self, valor):
        if valor.upper() not in ("PDF", "EXCEL"):
            raise ValueError("Formato no soportado.")
        self._formato = valor.upper()

    def generar_informe_empleados(self, empleados):
        print("\n--- Informe de Empleados ---")
        for e in empleados:
            print(f"  ID {e.get_id()}: {e.get_nombre()} | Email: {e.get_email()}")

    def generar_informe_proyectos(self, proyectos):
        print("\n--- Informe de Proyectos ---")
        for p in proyectos:
            print(f"  ID {p.get_id()}: {p.get_nombre()} | {p.get_descripcion()}")

    def generar_informe_horas(self, registros):
        print("\n--- Informe de Horas ---")
        total = 0.0
        for r in registros:
            print(f"  {r.get_fecha()} - {r.get_empleado().get_nombre()} "
                  f"en {r.get_proyecto().get_nombre()}: {r.get_horas()}h")
            total += r.get_horas()
        print(f"  TOTAL: {total} horas")

    def exportar_pdf(self, contenido):
        print(f"[Simulación] Exportando a PDF: {contenido}")

    def exportar_excel(self, contenido):
        print(f"[Simulación] Exportando a Excel: {contenido}")
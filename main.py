from datetime import date
from cifrado import Cifrado
from persona import Persona
from empleado import Empleado
from departamento import Departamento
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo
from usuario import Usuario
from crear_informes import CrearInformes

def main():
    # 1. Crear empleados
    emp1 = Empleado(1, "Ana Pérez", "Av. Siempre Viva 123", "+56912345678",
                    "ana.perez@ecotech.cl", date(2023, 3, 1), 1200000)
    emp2 = Empleado(2, "Luis Gómez", "Calle Falsa 456", "+56987654321",
                    "luis.gomez@ecotech.cl", date(2022, 7, 15), 1500000)

    # 2. Crear departamento y asignar gerente
    depto = Departamento("Desarrollo Sostenible", emp1)
    emp1.asignarDepartamento(depto)
    emp2.asignarDepartamento(depto)

    # 3. Crear proyectos
    proy1 = Proyecto("Panel Solar Inteligente", "Optimización de paneles", date(2024, 1, 10))
    proy2 = Proyecto("Reciclaje de Aguas", "Sistema de filtrado", date(2024, 2, 20))

    emp1.asignarProyecto(proy1)
    emp2.asignarProyecto(proy1)
    emp2.asignarProyecto(proy2)

    # 4. Registrar horas (composición)
    reg1 = RegistroTiempo(101, date(2024, 3, 1), 8, "Desarrollo de módulo", emp1, proy1)
    reg2 = RegistroTiempo(102, date(2024, 3, 2), 6, "Pruebas de integración", emp2, proy1)
    reg3 = RegistroTiempo(103, date(2024, 3, 3), 4, "Análisis de datos", emp2, proy2)

    # 5. Usuario y autenticación
    usuario = Usuario("ana.perez", "ClaveSegura123", "admin")
    print("Autenticación exitosa:", usuario.autenticar("ana.perez", "ClaveSegura123"))
    print("Permiso de escritura:", usuario.verificarPermiso("escritura"))

    # 6. Generar informes
    generador = CrearInformes("PDF")
    informe_emp = generador.generarInformeEmpleados([emp1, emp2])
    print(informe_emp)
    generador.exportarPDF(informe_emp)

    informe_proy = generador.generarInformeProyectos([proy1, proy2])
    print(informe_proy)

    # 7. Mostrar salario descifrado y cálculo
    print(f"Salario de Ana (descifrado): {emp1.descifrarSalario()}")
    print(f"Sueldo total Ana: {emp1.calcularSueldoTotal()}")

    # 8. Validaciones
    print("¿Email de Ana válido?", emp1.validarEmail())
    print("¿Teléfono de Ana válido?", emp1.validarTelefono())

if __name__ == "__main__":
    main()
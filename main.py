"""
Punto de entrada de Eco Tech Solutions.
Prueba el modelo UML + conexión MySQL + CRUD (incluye tabla sin nombre).
"""
from datetime import date

from config.conexion import Database
from acceso_dato.crud_basedatos import CRUD_DB
from acceso_dato.persona_datos import PersonaDAO
from acceso_dato.empleado_datos import EmpleadoDAO
from acceso_dato.departamento_datos import DepartamentoDAO
from acceso_dato.proyecto_datos import ProyectoDAO
from acceso_dato.registro_tiempo_datos import RegistroTiempoDAO
from acceso_dato.usuario_datos import UsuarioDAO

from modelo.persona import Persona
from modelo.empleado import Empleado
from modelo.departamento import Departamento
from modelo.proyecto import Proyecto
from modelo.generador_informes import GeneradorInformes


def menu():
    print("""
========= Eco Tech Solutions =========
1) Probar conexión a MySQL
2) Crear Persona
3) Crear Empleado
4) Crear Departamento
5) Crear Proyecto
6) Registrar horas
7) Generar informes
8) CRUD tabla SIN NOMBRE (genérica)
0) Salir
""")


def crud_tabla_sin_nombre():
    """CRUD de la tabla cuya denominación aún no ha sido definida."""
    crud = CRUD_DB("tabla_sin_nombre")
    while True:
        print("""
--- Tabla sin nombre ---
a) Insertar
b) Listar
c) Buscar por id
d) Actualizar
e) Eliminar
f) Volver
""")
        op = input("Opción: ").lower()
        try:
            if op == "a":
                datos = {
                    "campo1": input("campo1: "),
                    "campo2": input("campo2: "),
                    "campo3": input("campo3: "),
                }
                print("Insertado con ID:", crud.insertar(datos))
            elif op == "b":
                for f in crud.listar():
                    print(f)
            elif op == "c":
                print(crud.buscar_por_id(int(input("ID: "))))
            elif op == "d":
                id_ = int(input("ID a actualizar: "))
                datos = {
                    "campo1": input("nuevo campo1: "),
                    "campo2": input("nuevo campo2: "),
                    "campo3": input("nuevo campo3: "),
                }
                print("Filas afectadas:", crud.actualizar(id_, datos))
            elif op == "e":
                print("Eliminado:", crud.eliminar(int(input("ID: "))))
            elif op == "f":
                break
        except Exception as e:
            print("Error:", e)


def main():
    while True:
        menu()
        op = input("Seleccione opción: ").strip()

        if op == "1":
            db = Database()
            if db.obtener_conexion() and db.obtener_conexion().is_connected():
                print("✅ Conexión OK a", Database.DATABASE)
            else:
                print("❌ No se pudo conectar. Revisa XAMPP.")

        elif op == "2":
            p = Persona(
                nombre=input("Nombre: "),
                direccion=input("Dirección: "),
                telefono=input("Teléfono: "),
                email=input("Email: ")
            )
            PersonaDAO().crear(p)
            print("Persona creada con ID", p.get_id())

        elif op == "3":
            emp = Empleado(
                nombre=input("Nombre: "),
                email=input("Email: "),
                fecha_inicio_contrato=date.today(),
                salario=float(input("Salario: "))
            )
            EmpleadoDAO().crear(emp)
            print("Empleado creado con ID", emp.get_id())

        elif op == "4":
            dep = Departamento(nombre=input("Nombre del departamento: "))
            DepartamentoDAO().crear(dep)
            print("Departamento creado ID", dep.get_id())

        elif op == "5":
            proy = Proyecto(
                nombre=input("Nombre proyecto: "),
                descripcion=input("Descripción: "),
                fecha_inicio=date.today()
            )
            ProyectoDAO().crear(proy)
            print("Proyecto creado ID", proy.get_id())

        elif op == "6":
            rid = RegistroTiempoDAO().crear(
                fecha=input("Fecha (YYYY-MM-DD): "),
                horas=float(input("Horas: ")),
                descripcion=input("Descripción: "),
                empleado_id=int(input("ID empleado: ")),
                proyecto_id=int(input("ID proyecto: "))
            )
            print("Registro creado ID", rid)

        elif op == "7":
            gen = GeneradorInformes()
            print("Empleados:", EmpleadoDAO().listar())
            print("Proyectos:", ProyectoDAO().listar())
            print("Registros:", RegistroTiempoDAO().listar())

        elif op == "8":
            crud_tabla_sin_nombre()

        elif op == "0":
            Database().cerrar()
            print("Conexión cerrada. Hasta pronto.")
            break


if __name__ == "__main__":
    main()
from config.conexion import Database
from modelo.empleado import Empleado
from modelo.cifrador import Cifrador


class EmpleadoDAO:
    def __init__(self):
        self.db = Database()

    def crear(self, emp: Empleado):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        try:
            conn.start_transaction()
            cursor.execute(
                "INSERT INTO persona (nombre, direccion, telefono, email) VALUES (%s,%s,%s,%s)",
                (emp.get_nombre(), emp.get_direccion(),
                 emp.get_telefono(), emp.get_email())
            )
            nuevo_id = cursor.lastrowid
            emp.set_id(nuevo_id)

            dep_id = emp.get_departamento().get_id() if emp.get_departamento() else None
            cursor.execute(
                "INSERT INTO empleado (id, fecha_inicio_contrato, salario, departamento_id) "
                "VALUES (%s,%s,%s,%s)",
                (nuevo_id, emp.get_fecha_inicio_contrato(),
                 Cifrador.cifrar_datos(emp.get_salario()), dep_id)
            )
            conn.commit()
            return emp
        except Exception as e:
            conn.rollback()
            print(f"[EmpleadoDAO] Error: {e}")
            return None
        finally:
            cursor.close()

    def listar(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.nombre, p.direccion, p.telefono, p.email,
                   e.fecha_inicio_contrato, e.salario, e.departamento_id
            FROM persona p
            JOIN empleado e ON e.id = p.id
        """)
        filas = cursor.fetchall()
        cursor.close()
        for f in filas:
            f["salario"] = Cifrador.descifrar_datos(f["salario"])
        return filas

    def asignar_departamento(self, empleado_id, departamento_id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE empleado SET departamento_id=%s WHERE id=%s",
            (departamento_id, empleado_id)
        )
        conn.commit()
        cursor.close()

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM persona WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
from modelo.cifrador import Cifrador


class Usuario:

    ROLES_VALIDOS = {"admin", "gerente", "empleado"}

    def __init__(self, id=None, nombre_usuario="", contrasena_hash="", rol="empleado"):
        self._id = id
        self._nombre_usuario = nombre_usuario
        self._contrasena_hash = contrasena_hash
        self._rol = rol
        self._sesion_activa = False

    # -------- Getters / Setters --------
    def get_id(self):
        return self._id

    def get_nombre_usuario(self):
        return self._nombre_usuario

    def get_rol(self):
        return self._rol

    def set_rol(self, rol):
        if rol not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido: {rol}")
        self._rol = rol

    # -------- Métodos del UML --------
    def autenticar(self, usuario, password):
        if usuario != self._nombre_usuario:
            return False
        return Cifrador.verificar_password(password, self._contrasena_hash)

    def verificar_permiso(self, rol_requerido):
        return self._rol == rol_requerido

    def cambiar_contrasena(self, nueva):
        self._contrasena_hash = Cifrador.hash_password(nueva)

    def generar_sesion(self):
        self._sesion_activa = True
        return self._sesion_activa

    def __str__(self):
        return f"Usuario({self._nombre_usuario}, rol={self._rol})"
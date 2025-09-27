from typing import List
from .instructor import Instructor
from .cliente import Cliente
from .clase_grupal import ClaseGrupal

class Sucursal:
    def __init__(self, codigo: str, provincia: str, canton: str,
                 correo: str, telefono: str):
        self.codigo = codigo
        self.provincia = provincia
        self.canton = canton
        self.correo = correo
        self.telefono = telefono
        self.instructores: List[Instructor] = []
        self.clientes: List[Cliente] = []
        self.clases_grupales: List[ClaseGrupal] = []

    def agregar_instructor(self, instructor: Instructor):
        self.instructores.append(instructor)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def agregar_clase_grupal(self, clase: ClaseGrupal) -> bool:
        if len(self.clases_grupales) < 8:
            self.clases_grupales.append(clase)
            return True
        return False

from datetime import date
from typing import List
from .enums import Especialidad

class Instructor:
    def __init__(self, cedula: str, nombre_completo: str, telefono: str,
                 correo: str, fecha_nacimiento: date):
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.especialidades: List[Especialidad] = []
        self.clientes_asignados = []

    def agregar_especialidad(self, especialidad: Especialidad):
        if especialidad not in self.especialidades:
            self.especialidades.append(especialidad)

    def asignar_cliente(self, cliente):
        self.clientes_asignados.append(cliente)

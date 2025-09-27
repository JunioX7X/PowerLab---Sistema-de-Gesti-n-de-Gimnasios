from .enums import Especialidad

class ClaseGrupal:
    def __init__(self, codigo: str, tipo: Especialidad, capacidad_maxima: int,
                 salon: str, instructor, horario: str):
        self.codigo = codigo
        self.tipo = tipo
        self.capacidad_maxima = capacidad_maxima
        self.salon = salon
        self.instructor = instructor
        self.horario = horario
        self.clientes_matriculados = []

    def hay_cupo(self) -> bool:
        return len(self.clientes_matriculados) < self.capacidad_maxima

    def matricular_cliente(self, cliente) -> bool:
        if self.hay_cupo():
            self.clientes_matriculados.append(cliente)
            return True
        return False

from .enums import AreaCuerpo

class Ejercicio:
    def __init__(self, codigo: str, nombre: str, area_cuerpo: AreaCuerpo,
                 descripcion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.area_cuerpo = area_cuerpo
        self.descripcion = descripcion
        self.series = 0
        self.repeticiones = 0

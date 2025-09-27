from datetime import date
from .enums import AreaCuerpo

class Rutina:
    def __init__(self, cliente, instructor, fecha_creacion: date):
        self.cliente = cliente
        self.instructor = instructor
        self.fecha_creacion = fecha_creacion
        self.ejercicios_pecho_triceps = []
        self.ejercicios_biceps = []
        self.ejercicios_piernas = []
        self.ejercicios_espalda = []

    def agregar_ejercicio(self, ejercicio):
        if ejercicio.area_cuerpo == AreaCuerpo.PECHO_TRICEPS:
            self.ejercicios_pecho_triceps.append(ejercicio)
        elif ejercicio.area_cuerpo == AreaCuerpo.BICEPS:
            self.ejercicios_biceps.append(ejercicio)
        elif ejercicio.area_cuerpo == AreaCuerpo.PIERNAS:
            self.ejercicios_piernas.append(ejercicio)
        elif ejercicio.area_cuerpo == AreaCuerpo.ESPALDA:
            self.ejercicios_espalda.append(ejercicio)

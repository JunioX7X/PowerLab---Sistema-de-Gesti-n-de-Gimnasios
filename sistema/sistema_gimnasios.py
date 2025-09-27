from typing import List, Optional
from modelos.sucursal import Sucursal
from modelos.ejercicio import Ejercicio
from modelos.enums import AreaCuerpo

class SistemaGimnasios:
    def __init__(self):
        self.sucursales: List[Sucursal] = []
        self.bateria_ejercicios: List[Ejercicio] = []

    def agregar_sucursal(self, sucursal: Sucursal) -> bool:
        if len(self.sucursales) < 30:
            self.sucursales.append(sucursal)
            return True
        return False

    def buscar_sucursal(self, codigo: str) -> Optional[Sucursal]:
        for sucursal in self.sucursales:
            if sucursal.codigo == codigo:
                return sucursal
        return None

    def cargar_ejercicios_predefinidos(self):
        ejercicios = [
            Ejercicio("E001", "Press de Banca", AreaCuerpo.PECHO_TRICEPS, "Ejercicio para pecho"),
            Ejercicio("E002", "Curl con Barra", AreaCuerpo.BICEPS, "Ejercicio para bíceps"),
            Ejercicio("E003", "Sentadillas", AreaCuerpo.PIERNAS, "Ejercicio para piernas"),
            Ejercicio("E004", "Dominadas", AreaCuerpo.ESPALDA, "Ejercicio para espalda")
        ]
        self.bateria_ejercicios = ejercicios

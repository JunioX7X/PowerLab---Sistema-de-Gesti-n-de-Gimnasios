from datetime import date
from .enums import ClasificacionIMC

class MedicionCorporal:
    def __init__(self, cliente, instructor,
                 fecha: date, peso: float, estatura: float,
                 porcentaje_grasa: float, porcentaje_musculo: float,
                 edad_metabolica: int, grasa_visceral: float):
        self.cliente = cliente
        self.instructor = instructor
        self.fecha = fecha
        self.peso = peso
        self.estatura = estatura
        self.porcentaje_grasa = porcentaje_grasa
        self.porcentaje_musculo = porcentaje_musculo
        self.edad_metabolica = edad_metabolica
        self.grasa_visceral = grasa_visceral
        self.medida_cintura = 0.0
        self.medida_cadera = 0.0
        self.medida_pecho = 0.0
        self.medida_muslo = 0.0
        self.imc = self.calcular_imc()
        self.clasificacion_imc = self.clasificar_imc()
        self.es_alto_riesgo = self.verificar_alto_riesgo()
        self.vasos_agua = self.calcular_vasos_agua()
        self.proteinas_gramos = self.calcular_proteinas()

    def calcular_imc(self) -> float:
        return self.peso / (self.estatura ** 2) if self.estatura > 0 else 0.0

    def clasificar_imc(self) -> ClasificacionIMC:
        imc = self.imc
        if imc < 16:
            return ClasificacionIMC.DELGADEZ_SEVERA
        elif 16.01 <= imc <= 16.99:
            return ClasificacionIMC.DELGADEZ_MODERADA
        elif 17 <= imc <= 18.49:
            return ClasificacionIMC.DELGADEZ_LEVE
        elif 18.5 <= imc <= 24.99:
            return ClasificacionIMC.NORMAL
        elif 25 <= imc <= 29.99:
            return ClasificacionIMC.PRE_OBESIDAD
        elif 30 <= imc <= 34.99:
            return ClasificacionIMC.OBESIDAD_LEVE
        elif 35 <= imc <= 39.99:
            return ClasificacionIMC.OBESIDAD_MEDIA
        else:
            return ClasificacionIMC.OBESIDAD_MORBIDA

    def verificar_alto_riesgo(self) -> bool:
        return self.clasificacion_imc in [
            ClasificacionIMC.OBESIDAD_LEVE,
            ClasificacionIMC.OBESIDAD_MEDIA,
            ClasificacionIMC.OBESIDAD_MORBIDA
        ]

    def calcular_vasos_agua(self) -> int:
        return int(self.peso / 7)

    def calcular_proteinas(self) -> float:
        if self.cliente.sexo.upper() == 'M':
            return self.peso * 2.1
        elif self.cliente.sexo.upper() == 'F':
            return self.peso * 1.7
        return self.peso * 0.8

    def generar_reporte(self) -> str:
        return f"""
        === REPORTE DE MEDICIÓN ===
        Cliente: {self.cliente.nombre_completo}
        IMC: {self.imc:.2f} ({self.clasificacion_imc.value})
        Alto Riesgo: {'Sí' if self.es_alto_riesgo else 'No'}
        Agua: {self.vasos_agua} vasos/día
        Proteínas: {self.proteinas_gramos:.1f} g/día
        """

from enum import Enum

class Especialidad(Enum):
    CROSSFIT = "CrossFit"
    HIIT = "HIIT"
    TRX = "TRX"
    PESAS = "Pesas"
    SPINNING = "Spinning"
    CARDIO = "Cardio"
    YOGA = "Yoga"
    ZUMBA = "Zumba"

class ClasificacionIMC(Enum):
    DELGADEZ_SEVERA = "Delgadez severa"
    DELGADEZ_MODERADA = "Delgadez moderada"
    DELGADEZ_LEVE = "Delgadez leve"
    NORMAL = "Normal"
    PRE_OBESIDAD = "Pre-obesidad"
    OBESIDAD_LEVE = "Obesidad leve"
    OBESIDAD_MEDIA = "Obesidad media"
    OBESIDAD_MORBIDA = "Obesidad mórbida"

class AreaCuerpo(Enum):
    PECHO_TRICEPS = "Pecho y Tríceps"
    BICEPS = "Bíceps"
    PIERNAS = "Piernas"
    ESPALDA = "Espalda"

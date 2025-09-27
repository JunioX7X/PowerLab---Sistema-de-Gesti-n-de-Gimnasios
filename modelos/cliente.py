from datetime import date

class Cliente:
    def __init__(self, cedula: str, nombre_completo: str, telefono: str, correo: str,
                 fecha_nacimiento: date, sexo: str, fecha_inscripcion: date):
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.telefono = telefono
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.fecha_inscripcion = fecha_inscripcion
        self.instructor = None  # Inicializa a None para permitir clientes sin instructor inicial
        self.historial_mediciones = []  # Historial de mediciones (máx 10 según spec)
        self.rutina_actual = None  # Rutina actual
        self.clases_matriculadas = []  # Clases grupales matriculadas (máx 3)

    def asignar_instructor(self, instructor):
        self.instructor = instructor

    def agregar_medicion(self, medicion):
        if len(self.historial_mediciones) < 10:
            self.historial_mediciones.append(medicion)
        else:
            print("Historial de mediciones lleno (máx 10).")

    # Otros métodos según spec, como matricular_clase con check de max 3 y cupo
    def matricular_clase(self, clase_grupal):
        if len(self.clases_matriculadas) < 3 and clase_grupal.capacidad_maxima > len(clase_grupal.matriculados):
            self.clases_matriculadas.append(clase_grupal)
            clase_grupal.matriculados.append(self)  # Asumiendo que ClaseGrupal tiene lista matriculados
        else:
            print("No se puede matricular: límite alcanzado o clase llena.")
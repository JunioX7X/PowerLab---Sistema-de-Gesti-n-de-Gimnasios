# main.py actualizado para cargar instructores y clientes

from datetime import date
from modelos.sucursal import Sucursal
from modelos.instructor import Instructor
from modelos.cliente import Cliente
from modelos.medicion import MedicionCorporal
from modelos.rutina import Rutina
from modelos.clase_grupal import ClaseGrupal
from modelos.enums import Especialidad  # Asume ClasificacionIMC si existe
from sistema.sistema_gimnasios import SistemaGimnasios
from sistema.interfaz_consola import InterfazConsola
from sistema.persistencia import cargar_datos, guardar_datos


def main():
    print("=== INICIANDO SISTEMA POWERLAB ===")

    sistema = SistemaGimnasios()
    sistema.cargar_ejercicios_predefinidos()

    # Cargar datos previos si existen
    datos = cargar_datos()
    if datos["sucursales"]:
        print("Datos cargados desde JSON.")
        for suc_data in datos["sucursales"]:
            suc = Sucursal(
                suc_data["codigo"],
                suc_data["provincia"],
                suc_data["canton"],
                suc_data["correo"],
                suc_data["telefono"]
            )
            sistema.agregar_sucursal(suc)

            # Para depuración: imprime para confirmar
            print(f"Sucursal cargada: {suc.codigo} | {suc.provincia}, {suc.canton}")

            # Cargar instructores
            instructores_dict = {}  # Mapear cedula a instructor para referencias
            for ins_data in suc_data.get("instructores", []):
                ins = Instructor(
                    ins_data["cedula"],
                    ins_data["nombre"],
                    ins_data["telefono"],
                    ins_data["correo"],
                    date.fromisoformat(ins_data["fecha_nacimiento"])
                )
                for esp in ins_data["especialidades"]:
                    try:
                        ins.agregar_especialidad(Especialidad[esp.upper()])
                    except KeyError:
                        print(f"Especialidad inválida en carga: {esp}")
                suc.agregar_instructor(ins)
                instructores_dict[ins.cedula] = ins

            # Cargar clientes (después de instructores)
            for cli_data in suc_data.get("clientes", []):
                cli = Cliente(
                    cli_data["cedula"],
                    cli_data["nombre"],
                    cli_data["telefono"],
                    cli_data["correo"],
                    date.fromisoformat(cli_data["fecha_nacimiento"]),
                    cli_data["sexo"],
                    date.fromisoformat(cli_data["fecha_inscripcion"])
                )
                # Asignar instructor si existe
                instructor_cedula = cli_data.get("instructor_cedula")
                if instructor_cedula and instructor_cedula in instructores_dict:
                    cli.asignar_instructor(instructores_dict[instructor_cedula])
                suc.agregar_cliente(cli)

                # Cargar mediciones (si implementadas)
                for med_data in cli_data.get("mediciones", []):
                    instructor = instructores_dict.get(med_data["instructor_cedula"]) if med_data.get("instructor_cedula") else None
                    med = MedicionCorporal(
                        cli,
                        instructor,
                        date.fromisoformat(med_data["fecha"]),
                        med_data["peso"],
                        med_data["estatura"],
                        med_data.get("porcentaje_grasa", 0.0),
                        med_data.get("porcentaje_musculo", 0.0),
                        med_data.get("edad_metabolica", 0),
                        med_data.get("grasa_visceral", 0.0)
                    )
                    # Si IMC se calcula en __init__, ok; sino setear:
                    # med.imc = med_data["imc"]
                    # med.clasificacion_imc = ClasificacionIMC[med_data["clasificacion"].upper()] if "clasificacion" in med_data else None
                    cli.agregar_medicion(med)

            # Cargar clases grupales (opcional)
            for cg_data in suc_data.get("clases", []):
                instructor = instructores_dict.get(cg_data.get("instructor_cedula")) if cg_data.get("instructor_cedula") else None
                cg = ClaseGrupal(
                    cg_data["codigo"],
                    Especialidad[cg_data["tipo"].upper()],
                    cg_data["capacidad"],
                    cg_data["salon"],
                    instructor,
                    cg_data["horario"]
                )
                suc.agregar_clase_grupal(cg)

    # Interfaz
    interfaz = InterfazConsola(sistema)
    interfaz.ejecutar()

    # Guardar al salir
    guardar_datos(sistema)

    # Código hardcoded (puedes remover)
    # ...

if __name__ == "__main__":
    main()
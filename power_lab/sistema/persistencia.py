# persistencia.py actualizado para guardar/cargar instructores y clientes completamente

import json
import os
from datetime import date
from modelos.enums import Especialidad  # Asume ClasificacionIMC si existe; sino, define en enums.py

RUTA_DATOS = os.path.join("data", "datos.json")

def guardar_datos(sistema):
    """Guarda todas las sucursales y sus datos en JSON."""
    datos = {
        "sucursales": []
    }

    for suc in sistema.sucursales:
        sucursal_data = {
            "codigo": suc.codigo,
            "provincia": suc.provincia,
            "canton": suc.canton,
            "correo": suc.correo,
            "telefono": suc.telefono,
            "instructores": [],
            "clientes": [],
            "clases": []
        }

        # Instructores
        for ins in suc.instructores:
            sucursal_data["instructores"].append({
                "cedula": ins.cedula,
                "nombre": ins.nombre_completo,
                "telefono": ins.telefono,
                "correo": ins.correo,
                "fecha_nacimiento": str(ins.fecha_nacimiento),
                "especialidades": [e.value for e in ins.especialidades]
            })

        # Clientes
        for cli in suc.clientes:
            cliente_data = {
                "cedula": cli.cedula,
                "nombre": cli.nombre_completo,
                "telefono": cli.telefono,
                "correo": cli.correo,
                "fecha_nacimiento": str(cli.fecha_nacimiento),
                "sexo": cli.sexo,
                "fecha_inscripcion": str(cli.fecha_inscripcion),
                "instructor_cedula": cli.instructor.cedula if cli.instructor else None,
                "mediciones": []
            }

            for med in cli.historial_mediciones:
                cliente_data["mediciones"].append({
                    "fecha": str(med.fecha),
                    "peso": med.peso,
                    "estatura": med.estatura,
                    "imc": med.imc,
                    "clasificacion": med.clasificacion_imc.value if hasattr(med, 'clasificacion_imc') else "",  # Asume enum
                    "porcentaje_grasa": med.porcentaje_grasa if hasattr(med, 'porcentaje_grasa') else 0.0,
                    "porcentaje_musculo": med.porcentaje_musculo if hasattr(med, 'porcentaje_musculo') else 0.0,
                    "edad_metabolica": med.edad_metabolica if hasattr(med, 'edad_metabolica') else 0,
                    "grasa_visceral": med.grasa_visceral if hasattr(med, 'grasa_visceral') else 0.0,
                    "instructor_cedula": med.instructor.cedula if med.instructor else None
                })

            sucursal_data["clientes"].append(cliente_data)

        # Clases (opcional, expande si implementas)
        for cg in suc.clases_grupales:
            sucursal_data["clases"].append({
                "codigo": cg.codigo,
                "tipo": cg.tipo.value,
                "capacidad": cg.capacidad_maxima,
                "salon": cg.salon,
                "horario": cg.horario,
                "instructor_cedula": cg.instructor.cedula if cg.instructor else None
            })

        datos["sucursales"].append(sucursal_data)

    os.makedirs("data", exist_ok=True)
    with open(RUTA_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_datos():
    """Carga datos desde JSON si existe."""
    if not os.path.exists(RUTA_DATOS):
        return {"sucursales": []}
    with open(RUTA_DATOS, "r", encoding="utf-8") as f:
        return json.load(f)
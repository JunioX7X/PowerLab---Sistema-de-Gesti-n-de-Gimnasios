# PowerLab - Sistema de Gestión de Gimnasios

Sistema de gestión integral para gimnasios PowerLab, desarrollado en Python, que permite administrar sucursales, instructores, clientes, mediciones corporales, rutinas de ejercicio y clases grupales.

## 📋 Características Principales

- **Gestión de Sucursales**: Administra hasta 30 sucursales en diferentes ubicaciones
- **Instructores Especializados**: Registro de instructores con especialidades (CrossFit, HIIT, TRX, etc.)
- **Gestión de Clientes**: Control completo de clientes con historial médico y rutinas
- **Mediciones Corporales**: Seguimiento de IMC, porcentajes corporales y recomendaciones personalizadas
- **Rutinas de Ejercicio**: Planificación de entrenamientos por áreas del cuerpo
- **Clases Grupales**: Organización de clases con control de cupos
- **Persistencia de Datos**: Almacenamiento automático en formato JSON

## 🏗️ Estructura del Proyecto
power_lab/
├── modelos/
│ ├── enums.py # Enumeraciones (Especialidades, IMC, Áreas del cuerpo)
│ ├── sucursal.py # Clase Sucursal
│ ├── instructor.py # Clase Instructor
│ ├── cliente.py # Clase Cliente
│ ├── medicion.py # Clase MedicionCorporal
│ ├── rutina.py # Clase Rutina
│ ├── clase_grupal.py # Clase ClaseGrupal
│ └── ejercicio.py # Clase Ejercicio
├── sistema/
│ ├── sistema_gimnasios.py # Sistema principal
│ ├── interfaz_consola.py # Interfaz de usuario
│ └── persistencia.py # Manejo de datos JSON
├── data/
│ └── datos.json # Datos persistentes (se crea automáticamente)
└── main.py # Punto de entrada

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.7 o superior
- No se requieren librerías externas

### Ejecutar el Sistema

1. Clona o descarga el repositorio
2. Navega al directorio del proyecto
3. Ejecuta:

```bash
python main.py

📖 Manual de Uso
Menú Principal
Al iniciar el sistema, se presenta un menú con las siguientes opciones:

Gestión de Sucursales

Gestión de Instructores

Gestión de Clientes

Salir

1. Gestión de Sucursales
Agregar Sucursal:

Código único identificador

Provincia y cantón

Información de contacto (correo y teléfono)

Límite: 30 sucursales máximo

Listar Sucursales: Muestra todas las sucursales registradas

2. Gestión de Instructores
Agregar Instructor:

Seleccionar sucursal destino

Datos personales (cédula, nombre, teléfono, correo, fecha nacimiento)

Especialidades (puede tener múltiples):

CrossFit, HIIT, TRX, Pesas, Spinning, Cardio, Yoga, Zumba

Listar Instructores: Muestra instructores por sucursal

3. Gestión de Clientes
Registrar Cliente:

Seleccionar sucursal

Datos personales (cédula, nombre, contacto, fecha nacimiento, sexo)

Asignación obligatoria de instructor

Fecha de inscripción automática (fecha actual)

Listar Clientes: Muestra clientes por sucursal

🔧 Funcionalidades Técnicas
Sistema de Mediciones Corporales
Cada cliente puede tener hasta 10 mediciones que incluyen:

Cálculo automático de IMC y clasificación

Porcentajes de grasa y músculo

Edad metabólica y grasa visceral

Recomendaciones personalizadas:

Vasos de agua diarios (peso/7)

Gramos de proteína diarios (varía por sexo)

Clasificación de IMC
El sistema clasifica automáticamente el IMC en:

Delgadez severa, moderada o leve

Normal

Pre-obesidad

Obesidad leve, media o mórbida

Sistema de Rutinas
Las rutinas se organizan por áreas del cuerpo:

Pecho y Tríceps

Bíceps

Piernas

Espalda

Clases Grupales
Control de capacidad máxima

Matrícula limitada a 3 clases por cliente

Asignación de instructor especializado

💾 Persistencia de Datos
Los datos se guardan automáticamente en data/datos.json con la siguiente estructura:

{
  "sucursales": [
    {
      "codigo": "S001",
      "provincia": "San José",
      "canton": "San José",
      "instructores": [...],
      "clientes": [...],
      "clases": [...]
    }
  ]
}

🎯 Especialidades Disponibles
CrossFit: Entrenamiento funcional de alta intensidad

HIIT: Entrenamiento interválico de alta intensidad

TRX: Entrenamiento en suspensión

Pesas: Musculación tradicional

Spinning: Ciclismo indoor

Cardio: Ejercicios cardiovasculares

Yoga: Disciplina física y mental

Zumba: Baile fitness

⚠️ Limitaciones y Validaciones
Máximo 30 sucursales

Máximo 10 mediciones por cliente

Máximo 3 clases grupales por cliente

Cliente requiere instructor asignado obligatoriamente

Validación de formatos de fecha y datos de contacto

🔄 Flujo de Trabajo Recomendado
Crear sucursales

Registrar instructores con sus especialidades

Registrar clientes asignándoles un instructor

Agregar mediciones corporales a los clientes

Crear rutinas personalizadas

Programar clases grupales

🆘 Solución de Problemas
Error al cargar datos: Verifique que el archivo data/datos.json tenga formato JSON válido

Especialidades no reconocidas: Use exactamente los nombres definidos en el sistema

Fechas incorrectas: Use formato YYYY-MM-DD (ej: 2024-01-15)
